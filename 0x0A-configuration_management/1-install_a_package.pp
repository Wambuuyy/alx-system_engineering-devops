# Puppet Manifest for Task 2: Install a package

# Use exec resource to install Werkzeug and Flask via pip3
exec { 'install_werkzeug':
  command => '/usr/bin/pip3 install Werkzeug==2.0.3',
  path    => ['/usr/bin'],
  creates => '/usr/local/lib/python3.10/site-packages/werkzeug',
}

exec { 'install_flask':
  command => '/usr/bin/pip3 install Flask==2.1.0',
  path    => ['/usr/bin'],
  creates => '/usr/local/lib/python3.10/site-packages/Flask',
}

