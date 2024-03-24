# Puppet Manifest for Task 2: Install a package

# Use exec resource to install Flask via pip3
exec { 'install_flask':
  command => '/usr/bin/pip3 install Flask==2.1.0',
  path    => ['/usr/bin'],
  creates => '/usr/local/lib/python3.8/dist-packages/Flask',
}

