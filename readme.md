# **How to set up website locally and on Heroku**

## Locally

For Linux:

_for running on a server:_
_in wsgi.py change `app.run()` to `app.run(host='0.0.0.0')`_
_also change step 5 to `flask run --host 0.0.0.0`_

1. `pip install -r requirements.txt `
2. `source env/bin/activate`
3. `export FLASK_ENV=development`
4. `export FLASK_APP=main.py`
5. `flask run`
6. Open your browser and check `127.0.0.1:5000`

For Windows:

1. `pip install -r requirements.txt `
2. `python wsgi.py`
3. Open your browser and check `127.0.0.1:5000`

## On Heroku

1. `git add .`
2. `git commit`
3. `git push`
4. `git push heroku master`
5. `heroku open`

## Accessing database

`heroku psql`
`SELECT * FROM greenhouse` to see the current plant database
