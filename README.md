# Backend for Bahir Dar University Forum Web App

A project built under Google Developers Student Club (GDSC) Bahir Dar.

## Quick Start

To get this project up and running locally on your computer follow the following steps.

1. Clone this repository to your local machine.
2. Create a python virtual environment and activate it.
3. Open up your terminal and run the following command to install the packages used in this project.

```
$ pip install -r requirements.txt
```
4. Create `.env` file and include secret key.
6. Set up a Postgres database for the project.
7. Run the following commands to setup the database tables and create a super user.

```
$ python manage.py migrate
$ python manage.py createsuperuser
```


7. Run the development server using:

```
$ python manage.py runserver
```

8. Open a browser and go to http://localhost:8000/admin and login with your credentials.
