# workoutcomp-api
REST api for the workoutcomp project
---
## Setup
1. Setup virtual environment.
```
python3 -m venv env

//(MacOS/Linux)
source env/bin/activate
//(Windows)
env/Scripts/activate
```

2. Install dependencies
`pip install -r requirements.txt`

3. Run DB Migrations
```
python manage.py makemigrations
python manage.py migrate
```

4. Run the server
```
cd workoutcomp_api
python manage.py runserver
```