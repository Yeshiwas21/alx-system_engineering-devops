# Puppet manifest to install Flask version 2.1.0 using pip3

# Ensure the 'python3-pip' package is installed
package { 'python3-pip':
  ensure => installed,
}

# Use pip3 to install Flask with the specified version
package { 'flask':
  ensure  => '2.1.0',
  provider => 'pip3',
  require => Package['python3-pip'],
}
