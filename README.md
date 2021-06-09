
<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/othneildrew/Best-README-Template">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">Best-README-Template</h3>

  <p align="center">
    An awesome README template to jumpstart your projects!
    <br />
    <a href="https://github.com/othneildrew/Best-README-Template"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/othneildrew/Best-README-Template">View Demo</a>
    ·
    <a href="https://github.com/othneildrew/Best-README-Template/issues">Report Bug</a>
    ·
    <a href="https://github.com/othneildrew/Best-README-Template/issues">Request Feature</a>
  </p>
</p>


<!-- ABOUT THE PROJECT -->
## About The Project

This script simple checks given apache server's status page and reports if given thresholds exceeded 

### Requirements

[pip install plyer]
[pip install configparser]


<!-- GETTING STARTED -->
## Configuration structure

[SERVERS]
# contains a list of servers that you want to watch
local=http://localhost/server-status?auto

[THRESHOLDS]
# Parameters to watch for and their corresponding thresholds
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


### Prerequisites

Python version 3.x+

<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.
