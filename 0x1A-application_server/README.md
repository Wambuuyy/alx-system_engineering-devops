# Application Server Setup

This repository contains the steps and configurations necessary to set up an application server to serve dynamic content for the AirBnB clone project. The project involves setting up a development and production environment using Flask, Gunicorn, and Nginx on Ubuntu 16.04 LTS.

## Table of Contents

1. [Concepts](#concepts)
2. [Background Context](#background-context)
3. [Resources](#resources)
4. [Requirements](#requirements)
5. [Tasks](#tasks)
    - [Task 0: Set up development with Python](#task-0-set-up-development-with-python)
    - [Task 1: Set up production with Gunicorn](#task-1-set-up-production-with-gunicorn)
    - [Task 2: Serve a page with Nginx](#task-2-serve-a-page-with-nginx)
    - [Task 3: Add a route with query parameters](#task-3-add-a-route-with-query-parameters)
    - [Task 4: Let's do this for your API](#task-4-lets-do-this-for-your-api)
    - [Task 5: Serve your AirBnB clone](#task-5-serve-your-airbnb-clone)
    - [Task 6: Deploy it!](#task-6-deploy-it)
    - [Task 7: No service interruption](#task-7-no-service-interruption)

## Concepts

For this project, you should understand the following concepts:

- Web Server
- Server
- Web stack debugging

## Background Context

Your web infrastructure is currently serving static web pages using Nginx. This project involves adding an application server to serve dynamic content, integrating it with Nginx, and serving the AirBnB clone project.

## Resources

- [Application server vs web server](#)
- [How to Serve a Flask Application with Gunicorn and Nginx on Ubuntu 16.04](#)
- [Running Gunicorn](#)
- [Be careful with the way Flask manages slash in route - strict_slashes](#)
- [Upstart documentation](#)

## Requirements

### General

- A `README.md` file at the root of the project folder is mandatory.
- Use `python3` for all Python-related tasks.
- Comment all configuration files.
- All Bash scripts must:
  - End with a new line.
  - Be executable.
  - Pass Shellcheck (version 0.3.7-5~ubuntu16.04.1 via `apt-get`) without any error.
  - Start with `#!/usr/bin/env bash`.
  - Have a comment explaining what the script does.

### Bash Scripts

- Interpreted on Ubuntu 16.04 LTS.

### Servers

| Name          | Username | IP             | State   |
|---------------|----------|----------------|---------|
| 494470-web-01 | ubuntu   | 100.24.240.170 | running |
| 494470-web-02 | ubuntu   | 3.85.136.235   | running |
| 494470-lb-01  | ubuntu   | 54.84.78.174   | running |

## Tasks

### Task 0: Set up development with Python

Set up your development environment to serve the AirBnB clone using Flask on web-01.

**Steps:**

1. Complete task #3 of your SSH project for web-01.
2. Install `net-tools` package: `sudo apt install -y net-tools`.
3. Git clone `AirBnB_clone_v2` on web-01.
4. Configure `web_flask/0-hello_route.py` to serve content from `/airbnb-onepage/` on port 5000.

**Example:**
```sh
ubuntu@229-web-01:~/AirBnB_clone_v2$ python3 -m web_flask.0-hello_route
```

### Task 1: Set up production with Gunicorn

Set up a production environment with Gunicorn on web-01, serving the AirBnB clone on port 5000.

**Steps:**

1. Install Gunicorn and required libraries.
2. Ensure the Flask application object is named `app`.
3. Bind Gunicorn to localhost on port 5000.

**Example:**
```sh
ubuntu@229-web-01:~/AirBnB_clone_v2$ gunicorn --bind 0.0.0.0:5000 web_flask.0-hello_route:app
```

### Task 2: Serve a page with Nginx

Configure Nginx to serve the AirBnB clone from the route `/airbnb-onepage/`.

**Steps:**

1. Ensure Nginx serves the page both locally and on the public IP on port 80.
2. Proxy requests to the process on port 5000.
3. Include the Nginx config file as `2-app_server-nginx_config`.

### Task 3: Add a route with query parameters

Expand the web application to handle a new route `/airbnb-dynamic/number_odd_or_even/<int:n>`.

**Steps:**

1. Configure Nginx to proxy HTTP requests to this new route to a Gunicorn instance on port 5001.
2. Include the Nginx config file as `3-app_server-nginx_config`.

**Example:**
```sh
ubuntu@229-web-01:~/AirBnB_clone_v2$ tmux new-session -d 'gunicorn --bind 0.0.0.0:5001 web_flask.6-number_odd_or_even:app'
```

### Task 4: Let's do this for your API

Serve the AirBnB clone v3 RESTful API on web-01.

**Steps:**

1. Git clone `AirBnB_clone_v3`.
2. Setup Nginx to route `/api/` to a Gunicorn instance on port 5002.
3. Include the Nginx config file as `4-app_server-nginx_config`.

**Example:**
```sh
ubuntu@229-web-01:~/AirBnB_clone_v3$ tmux new-session -d 'gunicorn --bind 0.0.0.0:5002 api.v1.app:app'
```

### Task 5: Serve your AirBnB clone

Serve the AirBnB clone web dynamic on web-01.

**Steps:**

1. Git clone `AirBnB_clone_v4`.
2. Serve content from `web_dynamic/2-hbnb.py` on port 5003.
3. Setup Nginx to route `/` to the Gunicorn instance.
4. Ensure static assets are served correctly.
5. Reconfigure `web_dynamic/static/scripts/2-hbnb.js` with the correct IP.
6. Include the Nginx config as `5-app_server-nginx_config`.

### Task 6: Deploy it!

Configure the application server to run by default on Linux boot using `systemd`.

**Steps:**

1. Write a `systemd` script to start the Gunicorn process serving `web_dynamic/2-hbnb.py` on port 5003.
2. Ensure the process spawns 3 worker processes and logs errors and access.
3. Store the `systemd` script in the appropriate directory on web-01.
4. Start the `systemd` service and leave it running.
5. Upload `gunicorn.service` to GitHub.

**Example:**
```sh
bob@dylan:~$ curl -s 127.0.0.1:5003/2-hbnb | tail -5
```

### Task 7: No service interruption

Create a Bash script to gracefully reload Gunicorn without downtime.

**Example:**
```sh
sylvain@ubuntu$ ./4-reload_gunicorn_no_downtime
```

## Repository

- **GitHub repository:** `alx-system_engineering-devops`
- **Directory:** `0x1A-application_server`

Ensure all configurations and scripts are correctly uploaded and maintained in the specified GitHub repository.
