# util
sudo apt-get -y install python-pip
sudo apt-get -y install nginx
sudo apt-get -y install tree

# python package for flask app
pip install requests
pip install python-forecastio
pip install flask

# setting for nginx
sudo /etc/init.d/nginx start
sudo rm /etc/nginx/sites-enabled/default
sudo touch /etc/nginx/sites-available/flask_settings
sudo ln -s /etc/nginx/sites-available/flask_settings /etc/nginx/sites-enabled/flask_settings

sudo rm /etc/nginx/sites-enabled/flask_settings
sudo sh -c "echo 'server {' >> /etc/nginx/sites-enabled/flask_settings"
sudo sh -c "echo '    location / {' >> /etc/nginx/sites-enabled/flask_settings"
sudo sh -c "echo '        proxy_pass http://127.0.0.1:5000;' >> /etc/nginx/sites-enabled/flask_settings"
sudo sh -c "echo '        proxy_set_header Host \$host;' >> /etc/nginx/sites-enabled/flask_settings"
sudo sh -c "echo '        proxy_set_header X-Real-IP \$remote_addr;' >> /etc/nginx/sites-enabled/flask_settings"
sudo sh -c "echo '    }' >> /etc/nginx/sites-enabled/flask_settings"
sudo sh -c "echo '}' >> /etc/nginx/sites-enabled/flask_settings"

sudo /etc/init.d/nginx restart
