# ledger-transactions

The api can be explored with the help of Django REST framework,
so simply run the server after installation and use a web browser.

#### Basic routes
 - /transactions: a transaction is an operation between a account and a referer
 - /balances: the balance status of an account, when adding a transaction it will affect it's balance
 - /transactions-csv: trigger process from a csv file (read Redis section) <br>
   ex: `curl -X POST --data "path=/tmp/test.txt" http://127.0.0.1:8000/transactions-csv`

## install
`cd api`<br />
`pip install virtualenv`<br />
`virtualenv venv`<br />
`source venv/bin/activate`<br />
`pip install -r requirements.txt `<br />

## Redis
this is necessary to process csv files in batch.<br />
Start a redis on docker <br />
`docker run -d -p 6379:6379 redis`<br />
Then start a celery worker (inside the virtual env)<br />
`celery -A tasks worker --loglevel=info`

## run migrations
`python manage.py migrate`<br />

## Run
`python manage.py runserver`<br />