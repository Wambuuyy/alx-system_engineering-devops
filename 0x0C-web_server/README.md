# ALX System Engineering & DevOps - Web Server Project

## Background Context
This project focuses on configuring a web server, particularly Nginx, on Ubuntu machines. Automation of tasks using Bash scripting is encouraged to enhance efficiency and scalability.

## Resources
- **Read/Watch:**
  - [How the web works](https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/How_the_Web_works)
  - [Nginx](https://nginx.org/en/docs/)
  - [How to Configure Nginx](https://www.digitalocean.com/community/tutorials/how-to-install-nginx-on-ubuntu-18-04)
  - [Child process concept page](https://www.tutorialspoint.com/operating_system/os_processes.htm)
  - [Root and sub domain](https://en.wikipedia.org/wiki/Subdomain)
  - [HTTP requests](https://developer.mozilla.org/en-US/docs/Web/HTTP/Overview)
  - [HTTP redirection](https://en.wikipedia.org/wiki/URL_redirection)
  - [Not found HTTP response code](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/404)
  - [Logs files on Linux](https://linuxize.com/post/bash-history-command/)

## Learning Objectives
By the end of this project, you should be able to explain the following concepts without relying on external sources:
- **General**
  - The main role of a web server
  - Understanding of child processes
  - Importance of parent and child processes in web servers
  - Key HTTP requests
- **DNS**
  - Meaning of DNS and its main role
  - Various DNS record types: A, CNAME, TXT, MX

## Requirements
- **General**
  - Allowed editors: vi, vim, emacs
  - Interpretation on Ubuntu 16.04 LTS
  - Files ending with a new line
  - Mandatory README.md at the project's root folder
  - Bash scripts must be executable and pass Shellcheck (version 0.3.7)
  - Usage of `#!/usr/bin/env bash` as the first line in Bash scripts
  - Quiz questions to reinforce learning

## Tasks Overview
- **0. Transfer a file to your server**
  - Write a Bash script to transfer a file from client to server using scp.

- **1. Install nginx web server**
  - Install Nginx on web-01 server and configure it to listen on port 80.

- **2. Setup a domain name**
  - Register a .tech domain and configure DNS records.

- **3. Redirection**
  - Configure Nginx to redirect /redirect_me to another page using a 301 redirect.

- **4. Not found page 404**
  - Customize Nginx to have a custom 404 page.

- **5. Install Nginx web server (w/ Puppet)**
  - Use Puppet to install and configure Nginx, including a 301 redirect.

## Copyright - Plagiarism
- Solution to tasks must be original.
- Plagiarism is strictly prohibited and will lead to removal from the program.

© 2024 ALX, All rights reserved.

---
*Note: Remember, automation is key to efficiency! Ensure your scripts are robust and capable of handling diverse scenarios.*
