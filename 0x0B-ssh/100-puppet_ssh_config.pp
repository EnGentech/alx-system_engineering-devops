#Another puppet config option

file { '/etc/ssh/ssh_config':
  ensure => present,
  mode   => '0644',
  content => "
Host your_server_hostname
  IdentityFile ~/.ssh/school
  PasswordAuthentication no
",
}
