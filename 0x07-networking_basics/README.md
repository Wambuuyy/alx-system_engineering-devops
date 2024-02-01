# 0x07. Networking basics #0

## DevOps
### Network
#### By: Sylvain Kalache
##### Weight: 1

- Project will start Jan 31, 2024 6:00 AM, must end by Feb 2, 2024 6:00 AM
- Checker will be released at Feb 2, 2024 6:00 AM
- An auto review will be launched at the deadline

## Resources
Read or watch:
- [OSI model](https://en.wikipedia.org/wiki/OSI_model)
- [Different types of network](https://www.youtube.com/watch?v=CjSNLqQ5E4o)
- [LAN network](https://www.ciscopress.com/articles/article.asp?p=2157753)
- [WAN network](https://www.networkworld.com/article/2690050/lan-wan-explained/how-wan-technologies-impact-wan-design.html)
- [Internet](https://web.stanford.edu/class/msande91si/www-spr04/readings/week1/InternetWhitepaper.htm)
- [MAC address](https://searchnetworking.techtarget.com/definition/MAC-address)
- [What is an IP address](https://www.lifewire.com/what-is-an-ip-address-2625920)
- [Private and public address](https://www.iplocation.net/public-vs-private-ip-address)
- [IPv4 and IPv6](https://www.webopedia.com/insights/ipv6-ipv4-difference/)
- [Localhost](https://en.wikipedia.org/wiki/Localhost)
- [TCP and UDP](https://searchnetworking.techtarget.com/definition/TCP-IP)
- [TCP/UDP ports List](https://en.wikipedia.org/wiki/List_of_TCP_and_UDP_port_numbers)
- [What is ping /ICMP](https://en.wikipedia.org/wiki/Ping_(networking_utility))
- Positional parameters

**man or help:**
- [netstat](https://man7.org/linux/man-pages/man8/netstat.8.html)
- [ping](https://man7.org/linux/man-pages/man8/ping.8.html)

## Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

### OSI Model
- What it is
- How many layers it has
- How it is organized

### LAN
- What it is
- Typical usage
- Typical geographical size

### WAN
- What it is
- Typical usage
- Typical geographical size

### Internet
- What it is

### IP address
- What is an IP address
- What are the 2 types of IP address
- What is localhost
- What is a subnet
- Why IPv6 was created

### TCP/UDP
- What are the 2 mainly used data transfer protocols for IP (transfer level on the OSI schema)
- What is the main difference between TCP and UDP
- What is a port
- Memorize SSH, HTTP and HTTPS port numbers
- What tool/protocol is often used to check if a device is connected to a network

## Copyright - Plagiarism
You are tasked to come up with solutions for the tasks below yourself to meet with the above learning objectives.
You will not be able to meet the objectives of this or any following project by copying and pasting someone else’s work.
You are not allowed to publish any content of this project.
Any form of plagiarism is strictly forbidden and will result in removal from the program.

## Requirements
### General
- Allowed editors: vi, vim, emacs
- All your Bash script files will be interpreted on Ubuntu 20.04 LTS
- All your files should end with a new line
- A README.md file, at the root of the folder of the project, is mandatory
- All your Bash script files must be executable
- Your Bash script must pass shellcheck without any error
- The first line of all your Bash scripts should be exactly `#!/usr/bin/env bash`
- The second line of all your Bash scripts should be a comment explaining what is the script doing
- The second line of all your Bash scripts should be a comment explaining what is the script doing

### For multiple choice question type tasks, just type the number of the correct answer in your answer file, add a new line for every new answer, example:
```bash
What is the most important position in a software company?

1. Project manager
2. Backend developer
3. System administrator

cat foo_answer_file
3
```
### Tasks
#### 0. OSI model
- OSI (Open Systems Interconnection) is an abstract model describing layered communication and computer network design.
- Organized from the lowest level (layer 1) for physical transmission to the highest level (layer 7) for application-specific communication.
- Focus in this project: Transport layer (TCP/UDP) and Network layer (IP and ICMP).

**Questions:**
1. What is the OSI model?
   - Set of specifications for network hardware manufacturers.
   - Conceptual model characterizing communication functions without regard to internal structure.
   - Model characterizing communication functions with a strong regard for internal structure and technology.
   
2. How is the OSI model organized?
   - Alphabetically
   - From the lowest to the highest level
   - Randomly

**Repo:**
- [GitHub repository](https://github.com/alx-system_engineering-devops/0x07-networking_basics)
- [File: 0-OSI_model](https://github.com/alx-system_engineering-devops/0x07-networking_basics/0-OSI_model)

#### 1. Types of network
- LAN connects local devices, WAN connects LANs, and WANs operate over the Internet.

**Questions:**
1. What type of network is a computer in local connected to?
   - Internet
   - WAN
   - LAN

2. What type of network connects offices in different buildings?
   - Internet
   - WAN
   - LAN

3. What network is used when browsing www.google.com from a smartphone (not connected to Wi-Fi)?
   - Internet
   - WAN
   - LAN

**Repo:**
- [GitHub repository](https://github.com/alx-system_engineering-devops/0x07-networking_basics)
- [File: 1-types_of_network](https://github.com/alx-system_engineering-devops/0x07-networking_basics/1-types_of_network)

#### 2. MAC and IP address
**Questions:**
1. What is a MAC address?
   - Name of a network interface
   - Unique identifier of a network interface
   - A network interface

2. What is an IP address?
   - Like a postal address to houses for devices connected to a network
   - Unique identifier of a network interface
   - A number that network devices use to connect to networks

**Repo:**
- [GitHub repository](https://github.com/alx-system_engineering-devops/0x07-networking_basics)
- [File: 2-MAC_and_IP_address](https://github.com/alx-system_engineering-devops/0x07-networking_basics/2-MAC_and_IP_address)

#### 3. UDP and TCP
**Questions:**
1. Which statement is correct for the TCP box?
  

 - Protocol transferring data slowly but surely
   - Protocol transferring data fast and might lose data along the way

2. Which statement is correct for the UDP box?
   - Protocol transferring data slowly but surely
   - Protocol transferring data fast and might lose data along the way

3. Which statement is correct for the TCP worker?
   - Have you received boxes x, y, z?
   - May I increase the rate at which I am sending you boxes?

**Repo:**
- [GitHub repository](https://github.com/alx-system_engineering-devops/0x07-networking_basics)
- [File: 3-UDP_and_TCP](https://github.com/alx-system_engineering-devops/0x07-networking_basics/3-UDP_and_TCP)

#### 4. TCP and UDP ports
- Write a Bash script that displays listening ports.
- Show only listening sockets.
- Show PID and name of the program to which each socket belongs.

**Example:**
```bash
sylvain@ubuntu$ sudo ./4-TCP_and_UDP_ports
Active Internet connections (only servers)
Proto Recv-Q Send-Q Local Address           Foreign Address         State       PID/Program name
tcp        0      0 *:sunrpc                *:*                     LISTEN      518/rpcbind
tcp        0      0 *:ssh                   *:*                     LISTEN      1240/sshd
tcp6       0      0 [::]:sunrpc             [::]:*                  LISTEN      518/rpcbind
udp        0      0 *:sunrpc                *:*                                 518/rpcbind
udp6       0      0 [::]:sunrpc             [::]:*                              518/rpcbind
```

**Repo:**
- [GitHub repository](https://github.com/alx-system_engineering-devops/0x07-networking_basics)
- [File: 4-TCP_and_UDP_ports](https://github.com/alx-system_engineering-devops/0x07-networking_basics/4-TCP_and_UDP_ports)

#### 5. Is the host on the network
- Write a Bash script that pings an IP address passed as an argument.
- Accepts a string as an argument.
- Displays "Usage: 5-is_the_host_on_the_network {IP_ADDRESS}" if no argument passed.
- Pings the IP 5 times.

**Example:**
```bash
sylvain@ubuntu$ ./5-is_the_host_on_the_network 8.8.8.8
PING 8.8.8.8 (8.8.8.8) 56(84) bytes of data.
64 bytes from 8.8.8.8: icmp_seq=1 ttl=63 time=12.9 ms
64 bytes from 8.8.8.8: icmp_seq=2 ttl=63 time=13.6 ms
64 bytes from 8.8.8.8: icmp_seq=3 ttl=63 time=7.83 ms
64 bytes from 8.8.8.8: icmp_seq=4 ttl=63 time=11.3 ms
64 bytes from 8.8.8.8: icmp_seq=5 ttl=63 time=7.57 ms

--- 8.8.8.8 ping statistics ---
5 packets transmitted, 5 received, 0% packet loss, time 4006ms
rtt min/avg/max/mdev = 7.570/10.682/13.679/2.546 ms
sylvain@ubuntu$ ./5-is_the_host_on_the_network
Usage: 5-is_the_host_on_the_network {IP_ADDRESS}
```

**Repo:**
- [GitHub repository](https://github.com/alx-system_engineering-devops/0x07-networking_basics)
- [File: 5-is_the_host_on_the_network](https://github.com/alx-system_engineering-devops/0x07-networking_basics/5-is_the_host_on_the_network)
