# Networking Basics #1 Project

## Introduction
This project, authored by Sylvain Kalache, is part of the ALX System Engineering and DevOps curriculum. The focus of this project is on networking basics, with an emphasis on understanding localhost, IP addresses, hosts file, and network interfaces.

## Project Details
### Learning Objectives
After completing this project, you should be able to:

1. Explain what localhost/127.0.0.1 is.
2. Understand the purpose of 0.0.0.0.
3. Explain the role of the /etc/hosts file.
4. Display your machine's active network interfaces.
5. Write Bash scripts to configure network settings and perform network-related tasks.

### Copyright and Plagiarism
It is crucial to adhere to the copyright and plagiarism rules outlined in the project guidelines. Do not copy and paste solutions; come up with your own to meet the learning objectives.

### Requirements
Make sure to follow these requirements for all Bash scripts:

- Use vi, vim, or emacs as your editors.
- Scripts should be interpreted on Ubuntu 20.04 LTS.
- End all files with a new line.
- Include a README.md file at the root of the project folder.
- Bash scripts must be executable.
- Pass Shellcheck without errors.
- The first line of each Bash script should be `#!/usr/bin/env bash`.
- The second line should be a comment explaining the script's purpose.

### Tasks
1. **Change Your Home IP (0-change_your_home_IP)**
   - Write a Bash script to configure an Ubuntu server.
   - Ensure that localhost resolves to 127.0.0.2, and facebook.com resolves to 8.8.8.8.

   **Example:**
   ```bash
   $ sudo ./0-change_your_home_IP
   $ ping localhost
   PING localhost (127.0.0.2) 56(84) bytes of data.
   ...
   $ ping facebook.com
   PING facebook.com (8.8.8.8) 56(84) bytes of data.
   ...
   ```

2. **Show Attached IPs (1-show_attached_IPs)**
   - Write a Bash script to display all active IPv4 IPs on the machine.

   **Example:**
   ```bash
   $ ./1-show_attached_IPs | cat -e
   10.0.2.15$
   127.0.0.1$
   ...
   ```

3. **Port Listening on Localhost (100-port_listening_on_localhost)**
   - Write a Bash script to listen on port 98 on localhost.
   - Demonstrate using telnet to connect and send text.

   **Example:**
   ```bash
   Terminal 0: $ sudo ./100-port_listening_on_localhost
   Terminal 1: $ telnet localhost 98
   ...
   ```

## Conclusion
This project provides practical exercises to deepen your understanding of networking basics on Ubuntu. Follow the requirements and complete the tasks to enhance your skills in network configuration and scripting.
