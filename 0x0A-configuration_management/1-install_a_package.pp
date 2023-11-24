# Install the latest version of puppet-lint
package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}