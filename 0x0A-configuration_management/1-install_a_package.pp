# Puppet Manifest for Task 2: Install a package

# Ensure Flask is installed via pip3
package { 'Flask':
  ensure   => '2.1.0',  # Version requirement
  provider => 'gem'  # Use gem provider for Python packages
}

