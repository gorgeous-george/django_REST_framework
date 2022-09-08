# Django REST framework DIY API

## Basic API written in Django REST framework

This web application creates a very basic browsable API using Django REST Framework. 
The site allows GET/POST/PUT/PATCH/DELETE requests for two models: POST and COMMENT

- any user can view posts and comments
- only logged in users are able to add posts and comments
- only appropriate posts' and comments' owners are able to modify the posts or comments
- when deleting a post, all comments are deleted regardless of their owners

## Quick Start

To get this project up and running locally on your computer:

- Set up the Python development environment. We recommend using a Python virtual environment.
- Assuming you have Python setup, run the following commands (if you're on Windows you may use py or py -3 instead of python3 to start Python):

```
pip3 install -r requirements.txt
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py createsuperuser # Create a superuser (skip this if using proposed fixture)
python3 manage.py loaddata db.json # to fill the database with proposed fixture
python3 manage.py runserver
```

- Open a browser to http://127.0.0.1:8000/ to open the admin site
