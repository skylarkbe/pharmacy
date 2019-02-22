# My Web Pharmacy

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://raw.githubusercontent.com/skylarkbe/pharmacy/master/LICENSE)
[![GitHub All Releases](https://img.shields.io/github/downloads/skylarkbe/pharmacy/total.svg)](https://github.com/skylarkbe/pharmacy/archive/master.zip)

Stock system for personal pharmacy tracking.

This software is built with the [Django](https://www.djangoproject.com/) Framework and distributed under GPLv3. Framework documentation is available on the [official website](https://docs.djangoproject.com).

## Dependencies
The following dependencies are required to run the project properly:
* [Django core](https://pypi.org/project/Django/) ( Run `pip install django` to install )
* [Django model utils](https://pypi.org/project/django-model-utils/) ( Run `pip install django-model-utils` to install )

## Tips and tricks
* Run `py manage.py makemigrations` to create database migrations, then `py manage.py migrate` to apply them
* First user (superadmin) can be created by `py manage.py createsuperuser`
* Development server is started by `py manage.py runserver`

## URLs and paths

Once the server is started, application is available at [localhost:8000](http://localhost:8000/) and admin panel is available at [localhost:8000/admin](http://localhost:8000/admin/).

## Credits

This project utilises the following projects and technologies:
* Django - https://www.djangoproject.com/
* Bootstrap - https://getbootstrap.com/
* Bootstrap Date Picker plugin - https://github.com/uxsolutions/bootstrap-datepicker
* IonIcon - https://ionicons.com/