# Development setup

1. Install Python 3.5+ and create the dependencies file: `pip freeze > requirements.txt` 
2. Install requirements using: `pip install -r requirements.txt`
3. Enter the `src` folder with `cd src`
4. Create database and apply migrations: `python manage.py makemigrations` and `python manage.py migrate`
5. Run development server: `python manage.py runserver`
