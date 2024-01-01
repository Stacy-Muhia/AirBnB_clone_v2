#!/usr/bin/env bash
#web servers for the deployment of web_static
sudo apt-get -y update
sudo apt-get -y install nginx
sudo ufw allow 'Nginx HTTP'
mkdir -p /data/web_static/
mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/
echo "<html>
    <head>
    </head>
    <body>
        Holberton School
    </body>
</html>" > /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test /data/web_static/current
chown -R ubuntu:ubuntu /data
sudo sed -i '/hbnb_static/ { /alias/! s_/$_\/current/; }' /etc/nginx/sites-available/default
service nginx restart
exit 0
