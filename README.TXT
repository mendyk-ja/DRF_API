1. Install pip first
	sudo apt-get install python3-pip
2. Then install virtualenv using pip3
	sudo pip3 install virtualenv 
3. Now create a virtual environment
	virtualenv venv 
4. Active your virtual environment:
	source venv/bin/activate
5. Copy source  code into directions, which contains virtual environment.
6. Install requirements
	pip install -r /path/to/requirements.txt
7. Make migrations
	python manage.py makemigrations snippets
	python manage.py migrate
8. Create superuser
	python manage.py createsuperuser
9. Start project server and log in with your credentials.
	python manage.py runserver
10. Go to http://127.0.0.1:8000/images/ and you are ready to create thumbnails.


	Sorry to tell,  but I be able to  do only simple link to the stored thumnail
(which is based on posted foto of course). I didn't have much time and it was my first
time to play with Django Rest Framework. I now that is propably not even close what you are expected, but it was pleasure to learn something new through it. It  tooks  me about 4/5 hours to figure it out, but I'm not including doing official tutorial. Thank you for this opportunity
and have a great day!
