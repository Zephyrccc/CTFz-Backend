#!/bin/sh

sed -i "s/flag{flag_is_here}/$FLAG/" /var/www/html/flag.php

export FLAG=not_flag
FLAG=not_flag
