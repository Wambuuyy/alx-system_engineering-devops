---

# Web Stack Debugging #1

## Introduction

This project delves into the intricacies of debugging and resolving issues within a web stack environment, focusing particularly on Nginx configuration. Two tasks are presented, each with specific objectives and constraints, aimed at honing debugging skills and scripting proficiency.

## Tasks

### Task 0: Nginx Likes Port 80

**Objective:**  
Identify and rectify the issue preventing Nginx from listening on port 80 within the Ubuntu container. This task emphasizes diagnosing and addressing configuration discrepancies to ensure seamless operation.

**Requirements:**  
- Nginx must be operational and actively listening on port 80 across all active IPv4 addresses of the server.
- Develop a Bash script capable of configuring the server to adhere to the specified requirements.

### Task 1: Make It Sweet and Short (Advanced)

**Objective:**  
Craft a succinct Bash script to rectify the Nginx configuration issue, ensuring brevity without compromising effectiveness. This advanced task challenges participants to devise efficient solutions within a limited scope.

**Additional Requirements:**  
- The script must not utilize `;`, `&&`, or `wget`.
- Validate that the `service (init)` mechanism accurately reports Nginx's non-operation status.

## File Structure

- `0-nginx_likes_port_80`: Bash script for diagnosing and correcting Nginx's port 80 listening issue.
- `1-debugging_made_short`: Concise Bash script addressing the Nginx configuration anomaly in fewer than 5 lines.
- `README.md`: Comprehensive documentation outlining project details, tasks, usage instructions, and additional information.

## Usage

1. Clone the repository to your local environment:
   ```bash
   git clone https://github.com/your-username/alx-system_engineering-devops.git
   ```

2. Navigate to the project directory:
   ```bash
   cd alx-system_engineering-devops/0x0E-web_stack_debugging_1
   ```

3. Ensure executable permissions for all Bash scripts:
   ```bash
   chmod +x 0-nginx_likes_port_80 1-debugging_made_short
   ```

4. Execute the respective script to perform the designated task:
   ```bash
   ./0-nginx_likes_port_80
   ./1-debugging_made_short
   ```

## Author

Prudence Wambui

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Feel free to adjust any part of it according to your preferences or requirements!
