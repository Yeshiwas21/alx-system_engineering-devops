# Puppet manifest to install Flask version 2.1.0 using pip3

package { 'flask':
  ensure  => '2.1.0',
  provider => 'pip3',
  require => Package['python3-pip'],
}
