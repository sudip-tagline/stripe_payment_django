# stripe_payment_django

# create environment
python3 install -m venv <env_name>

# install requirements
pip install -r requirements.txt

# migrate all the database tables
1) python3 manage.py makemigrations/python manage.py makemigrations ------
2) python3 manage.py migrate/python manage.py migrate

# run python project
python3 manage.py runserver/python manage.py runserver