#Ensure that the file contains the same content as class-wp-locale.php
#This is a solution for resolving the 500 status error code
file { '/var/www/html/wp-includes/class-wp-locale.phpp':
ensure => present,
source => '/var/www/html/wp-includes/class-wp-locale.php',
}
