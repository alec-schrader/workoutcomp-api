# Install or update needed software
apt-get update
apt-get install -yq git python python3-pip nginx install python3-venv
pip install --upgrade pip virtualenv

# Fetch source code
git clone https://github.com/alec-schrader/workoutcomp-api.git 

cd workoutcomp-api

python3 -m venv env
source env/bin/activate
pip install -r requirements.txt

cd workoutcomp_api

python manage.py makemigrations
python mangae.py migrate

gunicorn --bind 0.0.0.0:8000 workoutcomp_api.wsgi

systemctl start nginx
systemctl enable nginx

nano /etc/nginx/conf.d/django.conf

server {  
	listen 80;     
	server_name django.example.com;    
	location = /favicon.ico { access_log off; log_not_found off; }    
	location /static/ {         
		root /root/django_project;     
	}    
	location / {         
		include proxy_params;         
		proxy_pass http://unix:/run/gunicorn.sock;     
	}
}

# Fetch source code
git clone https://github.com/alec-schrader/workoutcomp-api.git 

cd workoutcomp-api

python3 -m venv env
source env/bin/activate
pip install -r requirements.txt

python manage.py makemigrations
python mangae.py migrate

cd workoutcomp_api

gunicorn --bind 0.0.0.0:8000 workoutcomp_api.wsgi