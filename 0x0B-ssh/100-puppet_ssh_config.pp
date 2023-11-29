#!/usr/bin/env bash

# SSH client configuration file to connect to a server without typing a password

file { '/etc/ssh/ssh_config':
  ensure => present,
}
file_line { 'Turn off passwd auth':
  Path  => '/etc/ssh/ssh_config',
  line  => 'PasswordAuthentication no',
  match => '^#PasswordAuthentication',
}
file_line { 'Declare identity file':
  Path  => '/etc/ssh/ssh_config',
  line  => 'IdentityFile ~/.ssh/school',
  match => '^#IdentityFile',
}
