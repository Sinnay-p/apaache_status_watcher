<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/othneildrew/Best-README-Template">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">Apache Server Status Watcher</h3>



<!-- ABOUT THE PROJECT -->
## About The Project

This script simple checks given apache server's status page and reports if given thresholds exceeded 

### Requirements

[pip install plyer]
[pip install configparser]


<!-- GETTING STARTED -->
## Configuration structure
```
#contains a list of servers that you want to watch

[SERVERS]
local=http://localhost/server-status?auto

# Parameters to watch for and their corresponding thresholds
[THRESHOLDS]
BusyWorkers=50
Load1=2
Load5=3.5
Load15=4

[EXTRAS]
APP_NAME=APACHE STATUS WATCHER
NOTIFICATION_MESSAGE=Attention required! Server {server} {limits}
ICON=warning.ico
# Sleep interval till the next check
INTERVAL_CHECK_MINUTES=5
```

### Prerequisites

Python version 3.x+

<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.
