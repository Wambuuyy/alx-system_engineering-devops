To tackle the tasks outlined in your project, you will need to create two Puppet manifests that address the specific requirements: improving the Nginx server's performance and resolving the "Too many open files" error for the `holberton` user. Here's a step-by-step guide to achieve this:

### Task 0: Improve Nginx Server Performance

The goal is to optimize the Nginx server configuration to handle high load efficiently. Here is a possible Puppet manifest (`0-the_sky_is_the_limit_not.pp`) that could help resolve the issue:

```puppet
# 0-the_sky_is_the_limit_not.pp
# This manifest configures Nginx to handle more concurrent connections efficiently.

exec { 'increase-worker-connections':
  command => 'sed -i "s/worker_connections 768;/worker_connections 4096;/" /etc/nginx/nginx.conf',
  path    => ['/bin', '/usr/bin', '/sbin', '/usr/sbin'],
  onlyif  => 'grep -q "worker_connections 768;" /etc/nginx/nginx.conf',
  require => Service['nginx'],
}

exec { 'increase-worker-processes':
  command => 'sed -i "s/worker_processes 1;/worker_processes auto;/" /etc/nginx/nginx.conf',
  path    => ['/bin', '/usr/bin', '/sbin', '/usr/sbin'],
  onlyif  => 'grep -q "worker_processes 1;" /etc/nginx/nginx.conf',
  require => Service['nginx'],
}

service { 'nginx':
  ensure => 'running',
  enable => true,
  subscribe => Exec['increase-worker-connections', 'increase-worker-processes'],
}
```

### Task 1: Resolve "Too many open files" Error for `holberton` User

The goal here is to adjust the system configuration to allow the `holberton` user to open more files. Here is a Puppet manifest (`1-user_limit.pp`) that modifies the limits:

```puppet
# 1-user_limit.pp
# This manifest adjusts the file descriptor limits for the holberton user.

file { '/etc/security/limits.d/holberton.conf':
  ensure  => file,
  content => "holberton soft nofile 65535\nholberton hard nofile 65535\n",
  owner   => 'root',
  group   => 'root',
  mode    => '0644',
}

exec { 'apply-limits':
  command => 'sysctl -p',
  path    => ['/bin', '/usr/bin', '/sbin', '/usr/sbin'],
  subscribe => File['/etc/security/limits.d/holberton.conf'],
}
```

### Steps to Implement and Test

1. **Create the Puppet Manifests**: Create the `0-the_sky_is_the_limit_not.pp` and `1-user_limit.pp` files with the above contents in your project directory (`0x1B-web_stack_debugging_4`).

2. **Apply the Manifests**:
    - Log in to your server.
    - Navigate to the project directory.
    - Run the Puppet manifests:
      ```sh
      puppet apply 0-the_sky_is_the_limit_not.pp
      puppet apply 1-user_limit.pp
      ```

3. **Verify the Changes**:
    - For Task 0, re-run the ApacheBench command to ensure there are no failed requests:
      ```sh
      ab -c 100 -n 2000 localhost/
      ```
    - For Task 1, switch to the `holberton` user and check if you can open files without encountering the "Too many open files" error:
      ```sh
      su - holberton
      head /etc/passwd
      ```

By following these steps, you should be able to resolve the performance issue with your Nginx server and fix the file descriptor limit issue for the `holberton` user. Ensure you test thoroughly to confirm the changes have the desired effect.
