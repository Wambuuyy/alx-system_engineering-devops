# HTTPS SSL Curriculum

## Background Context

In today's digital landscape, securing website traffic is paramount. Failure to do so can result in various security vulnerabilities, compromising the integrity and confidentiality of data transmitted over the web. 

## Resources

### Read/Watch:
- [What is HTTPS?](https://www.cloudflare.com/learning/ssl/what-is-https/)
- [What are the 2 main elements that SSL is providing?](https://www.ibm.com/support/knowledgecenter/SSFKSJ_7.5.0/com.ibm.mq.sec.doc/q010780_.htm)
- [HAProxy SSL termination on Ubuntu 16.04](https://www.digitalocean.com/community/tutorials/how-to-secure-haproxy-with-let-s-encrypt-on-ubuntu-16-04)
- [SSL termination](https://www.nginx.com/blog/terminating-ssl-http-nginx/)
- [Bash function](https://www.gnu.org/software/bash/manual/html_node/Shell-Functions.html)

### Man/Help:
- [awk](https://linux.die.net/man/1/awk)
- [dig](https://linux.die.net/man/1/dig)

## Learning Objectives

Upon completion of this curriculum, learners are expected to:

### General
- Define HTTPS SSL and its two main roles
- Explain the purpose of encrypting traffic
- Understand SSL termination and its significance in web security

## Requirements

### General
- Allowed editors: vi, vim, emacs
- Interpretation environment: Ubuntu 16.04 LTS
- Files end with a newline
- Mandatory `README.md` file at the root of the project folder
- All Bash script files must be executable
- Bash scripts must pass Shellcheck (version 0.3.7) without any error
- The first line of all Bash scripts should be `#!/usr/bin/env bash`
- The second line of all Bash scripts should be a comment explaining the script's purpose

## Quiz Questions

Congratulations on completing the quiz successfully! Keep up the good work!

## Your Servers

| Name          | Username | IP              | State   |
|---------------|----------|-----------------|---------|
| 494470-web-01 | ubuntu   | 100.25.156.254 | running |
| 494470-web-02 | ubuntu   | 54.85.20.151   | running |
| 494470-lb-01  | ubuntu   | 52.23.245.155  | running |

## Tasks

### 0. World Wide Web

**Mandatory**

Configure your domain zone to point various subdomains to specific IPs. Write a Bash script to display information about subdomains.

#### Requirements:

- Add subdomains www, lb-01, web-01, and web-02 to your domain.
- Bash script must accept 2 arguments: domain and subdomain.
- Output format: "The subdomain [SUB_DOMAIN] is a [RECORD_TYPE] record and points to [DESTINATION]".
- When only domain parameter is provided, display info for www, lb-01, web-01, and web-02.
- Use `awk` and at least one Bash function.

### 1. HAProxy SSL Termination

**Mandatory**

Configure HAProxy to handle encrypted traffic for the subdomain www.

#### Requirements:

- HAProxy must listen on port TCP 443.
- HAProxy must serve encrypted traffic returning the / of your web server.
- Page returned when querying root domain should contain "Holberton School".
- Share HAProxy config as `haproxy.cfg`.
- Install HAProxy 1.5 or higher.

### 2. No Loophole in Your Website Traffic

**Advanced**

Configure HAProxy to automatically redirect HTTP traffic to HTTPS.

#### Requirements:

- HAProxy should transparently redirect HTTP traffic to HTTPS.
- HAProxy should return a 301 status for redirection.
- Share HAProxy config as `haproxy.cfg`.

## Repo

**GitHub Repository:** [alx-system_engineering-devops](https://github.com/Wambuuyy/alx-system_engineering-devops)

**Directory:** 0x10-https_ssl

**Files:**
- 0-world_wide_web
- 1-haproxy_ssl_termination
- 100-redirect_http_to_https

## Copyright

Copyright © 2024 ALX, All rights reserved.
