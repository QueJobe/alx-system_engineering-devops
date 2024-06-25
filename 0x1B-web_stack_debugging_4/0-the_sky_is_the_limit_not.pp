# update file limit on nginx.
exec { 'thefix':
command => 'sed -i s/15/2000/ /etc/default/nginx',
path    => '/bin',
}
service { 'nginx':
ensure    => running,
subscribe => Exec['thefix'],
}
