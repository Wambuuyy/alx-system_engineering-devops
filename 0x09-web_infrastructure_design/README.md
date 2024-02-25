# Web Infrastructure Design Project


## Concepts
- **DNS**
- **Monitoring**
- **Web Server**
- **Network basics**
- **Load balancer**
- **Server**

## Resources
Read or watch:
- Network basics concept page
- Server concept page
- Web server concept page
- DNS concept page
- Load balancer concept page
- Monitoring concept page
- What is a database
- What’s the difference between a web server and an app server?
- DNS record types
- Single point of failure
- How to avoid downtime when deploying new code
- High availability cluster (active-active/active-passive)
- What is HTTPS
- What is a firewall

## Learning Objectives
- Ability to draw a diagram covering the web stack built with the sysadmin/devops track projects
- Explanation of each component's role
- Understanding of system redundancy
- Knowledge of acronyms: LAMP, SPOF, QPS

## Copyright - Plagiarism
- Original solutions for meeting the learning objectives
- No plagiarism tolerated
- Content not to be published

## Requirements
- **General**
  - README.md file is mandatory
  - Whiteboard each task and take screenshots
  - Manual review for each task completion
  - Task completion status indicated by turning task names green
  - Upload screenshots to an image hosting service
  - GitHub submission with repository link

### Task 0: Simple Web Stack

#### Description:
Design a one-server web infrastructure with components including Nginx web server, application server, MySQL database, and a domain name configured with DNS. The website should be reachable via www.foobar.com.

#### Requirements:
- **Components**:
  - 1 server
  - 1 Nginx web server
  - 1 application server
  - 1 MySQL database
- **Domain Configuration**:
  - Domain name: foobar.com
  - www record pointing to server IP 8.8.8.8
- **Explanation**:
  - Server role
  - Domain name role
  - Type of DNS record for www.foobar.com
  - Web server role
  - Application server role
  - Database role
  - Communication between server and user's computer
- **Issues**:
  - Single point of failure (SPOF)
  - Downtime during maintenance
  - Scalability issues with high traffic

### Task 1: Distributed Web Infrastructure

#### Description:
Design a three-server web infrastructure hosting www.foobar.com with additional components like a load balancer and HAproxy. 

#### Requirements:
- **Components**:
  - 2 servers
  - 1 Nginx web server
  - 1 application server
  - 1 HAproxy load balancer
  - 1 MySQL database
- **Explanation**:
  - Justification for additional elements
  - Load balancer distribution algorithm
  - Active-Active or Active-Passive setup explanation
  - Primary-Replica (Master-Slave) cluster operation
  - Difference between Primary and Replica nodes in application context
- **Issues**:
  - Single point of failure (SPOF)
  - Security vulnerabilities (no firewall, no HTTPS)
  - Lack of monitoring

### Task 2: Secured and Monitored Web Infrastructure

#### Description:
Design a three-server web infrastructure hosting www.foobar.com with enhanced security measures, serving encrypted traffic, and monitored using monitoring clients.

#### Requirements:
- **Components**:
  - 3 firewalls
  - SSL certificate for HTTPS
  - 3 monitoring clients
- **Explanation**:
  - Justification for additional elements
  - Role of firewalls, HTTPS, and monitoring
  - Monitoring tool data collection process
  - Monitoring web server QPS
- **Issues**:
  - SSL termination at load balancer level
  - Single MySQL server for writes
  - Homogeneity of server components

### Task 3: Scale Up

#### Description:
Expand the infrastructure with separate servers for each component and configure load balancer clustering.

#### Requirements:
- **Components**:
  - 1 server
  - 1 HAproxy load balancer configured as a cluster
  - Split components on separate servers (web server, application server, database)
- **Explanation**:
  - Justification for additional elements
- **Issues**:
  - Not specified, but likely related to scalability and complexity
  
## Copyright
© 2024 ALX, All rights reserved.


