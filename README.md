# Django Users Boilerplate :busts_in_silhouette:
This repo is the implementation of **Django users**. It has an app named ***users*** which can be used in any Django project so you don't have to implement Django Users from scratch.
You need to run follwing commands for app to work properly:
```
python3 manage.py makemigrations
python3 manage.py makemigrations users
python3 manage.py migrate
```

After running migrations:
```
python3 manage.py createsuperuser
python3 manage.py runserver
```

**Note:**
This project is made in python v3.8 :snake:
