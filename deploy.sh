#!/usr/bin/env bash
git commit -am "`date`"
cd /var/www/mawkeb/mawkeb
git pull
sudo service apache2 restart
