# Starts with Python 3.5 Apline official Docker Image
FROM python:3.5

RUN apt-get update && apt-get upgrade -y && apt-get autoremove && apt-get autoclean

# Project Files and Settings
ARG PROJECT=myPharmacy
ARG PROJECT_DIR=/var/www/${PROJECT}
ARG USER=admin
ARG PASSWORD=nimda
ARG USER_MAIL=admin@test.com
ARG DB_DIR=/database
ARG SECRET="3#&&bh^6=t&pqo&(wn3!cub+womdir2qg161ztb9q*^$=0t2)a"

# Make sure the debug is set to False
ENV DJANGO_DEBUG=False
ENV DJANGO_SECRET_KEY=${SECRET}
ENV DJANGO_SQLITE_DIR=${DB_DIR}
ENV DJANGO_USER=${USER}
ENV DJANGO_PASSWORD=${PASSWORD}
ENV DJANGO_SETTINGS_MODULE="app.settings"

RUN mkdir -p $PROJECT_DIR
WORKDIR $PROJECT_DIR
COPY dependencies.txt .
RUN pip install -r dependencies.txt

# Migrate DB
CMD ["python", "manage.py","migrate"]

# Create superuser
RUN python -c "import django; django.setup(); \
   from django.contrib.auth.management.commands.createsuperuser import get_user_model; \
   get_user_model()._default_manager.db_manager('$DJANGO_DB_NAME').create_superuser( \
   username='$DJANGO_USER', \
   email='$USER_MAIL', \
   password='$DJANGO_PASSWORD')"

# Server
EXPOSE 8000
STOPSIGNAL SIGINT
CMD ["python", "manage.py","runserver", "0.0.0.0:8000"]