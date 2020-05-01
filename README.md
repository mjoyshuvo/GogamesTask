# DjangoWith-Bootstrap
Basic django structure with Login, Logout, Pagination, Model Permission, Custom User Management and Bootstrap Integration 

## Prerequisites
* Python
* Virtualenv
* Postgres

## Getting Started
1. Clone the repository.
2. Create virtual environment. 
```
virtualenv -p python3 envname --no-site-packages
```
3. Go to project folder
4. Install requirements 
```
pip install -r requirements.txt
```
5. Create Database and credentials in conf/settings.py file
6. Migrate 
```
python manage.py migrate
```
7. Run project 
```
python manage.py runserver
```
8. Create Super User
```
python manage.py createsuperuser
```
9. Description:
In home page you can find 2 links of Admin url and Game url.
```
admin url : 0.0.0.0:8000/admin
game url : 0.0.0.0:8000/api/v1/game
filter with category : 0.0.0.0:8000/api/v1/game/?category=<category_id>
```
## Built With

* [Django](https://www.djangoproject.com/) - The web framework used.
* [Django Rest Framework](http://www.django-rest-framework.org/) - Rest Api.
* [Bootstrap 4](https://getbootstrap.com/) - HTML Template.
