import configparser
import urllib.request
import urllib.parse
from plyer import notification
import time


class ApacheServerStatus:
    def __init__(self):
        self.servers = {}
        self.server_status_raw_data = {}
        self.server_load = {}
        self.load_config()
        self.interval_repeat = int(
            self.config['EXTRAS']['INTERVAL_CHECK_MINUTES'])
        self.normalize_server_list()
        self.start_lookup()
        self.call_repeatedly(self.start_lookup)

    def load_config(self):
        file_path = 'config.ini'
        self.config = configparser.ConfigParser()
        self.config.read(file_path)
        self.config.sections()

    def call_repeatedly(self, func):
        while True:
            time.sleep(self.interval_repeat*60)
            func()

    def start_lookup(self):
        print("Looking Up")
        self.retrieve_status()
        self.parse_status_data()

    def normalize_server_list(self):
        for key in self.config["SERVERS"]:
            self.servers[key] = self.config["SERVERS"][key]

    def retrieve_status(self):
        for server, url in self.servers.items():
            try:
                req = urllib.request.Request(url)
                with urllib.request.urlopen(req) as response:
                    data = response.read()
                    encoding = response.info().get_content_charset('utf-8')
                    self.server_status_raw_data[server] = data.decode(
                        encoding).lower().split('\n')
            except Exception as e:
                self.server_status_raw_data[server] = str(e)

    def parse_status_data(self):
        self.config['EXTRAS']
        for server, response in self.server_status_raw_data.items():
            self.server_load[server] = {}

            for threshold in self.config['THRESHOLDS']:
                self.server_load[server][threshold] = 0
                self.server_load[server][threshold] = float(next(
                    (s.replace(threshold + ':', '').strip() for s in response if threshold in s), 0))
        self.check_thresholds()

    def check_thresholds(self):
        for server, server_load in self.server_load.items():
            notification_message = []
            for threshold, value in server_load.items():
                if value >= float(self.config['THRESHOLDS'][threshold]):
                    notification_message.append('{} is {} above limit {}'.format(
                        threshold, value, self.config['THRESHOLDS'][threshold]))
            if notification_message:
                self.send_notification(server, "\n".join(notification_message))

    def send_notification(self, server, message):
        notification.notify(
            title="Server {} load detected".format(server),
            message=self.config['EXTRAS']['NOTIFICATION_MESSAGE'].format(server=server, limits=message, timeout=8),
            app_icon=self.config['EXTRAS']['icon'],
            app_name =self.config['EXTRAS']['APP_NAME']
            )


instance = ApacheServerStatus()
