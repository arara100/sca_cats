Run the project:

python manage.py runserver

Technologies:

Python 3.x

Django

Django REST Framework

MYSQL

Install all dependencies:

pip install -r requirements.txt


To create tables in the database, run the following commands:

python manage.py makemigrations

python manage.py migrate

Available endpoints:
/api/spycats/{id}: List all agent cats (GET), create a new cat (POST),
Update information (PATCH/PUT), delete (DELETE)

/api/missions/{id}: List all missions (GET), create a new mission (POST),
Update information about a specific mission (PATCH/PUT), delete (DELETE)

/api/targets/{id}: List all targets (GET), create a new target (POST),
Update information (PATCH/PUT), delete (DELETE)

/api/missions/create_with_targets/: Creating a mission with targets (POST)
