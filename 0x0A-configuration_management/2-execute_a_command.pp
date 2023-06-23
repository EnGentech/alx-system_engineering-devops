#Its time to die, killme

#exec { 'killmenow_process':
#  command     => 'pkill killmenow',
#  path        => ['/usr/bin', '/usr/sbin', '/bin', '/sbin'],
#  onlyif      => 'pgrep killmenow',
#  refreshonly => true,
#}

exec{'pkill -f killmenow':
path  => '/usr/bin/:/usr/local/bin/:/bin/'
}
