# Automating creation of custom HTTP header response with Puppet

# Install Nginx
class { 'nginx':
  ensure => 'installed',
}

# Define a custom Nginx configuration file
file { '/etc/nginx/sites-available/custom_header':
  ensure  => present,
  content => "server {
                listen 80 default_server;
                server_name _;
                location / {
                    add_header X-Served-By $hostname;
                   }
            }",
}

# Create a symbolic link to enable the custom configuration
file { '/etc/nginx/sites-enabled/custom_header':
  ensure  => link,
  target  => '/etc/nginx/sites-available/custom_header',
  require => File['/etc/nginx/sites-available/custom_header'],
}

# Remove the default Nginx default configuration
file { '/etc/nginx/sites-enabled/default':
  ensure => absent,
}

# Restart Nginx to apply changes
service { 'nginx':
  ensure    => 'running',
  enable    => true,
  subscribe => File['/etc/nginx/sites-available/custom_header'],
}
