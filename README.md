# ledger-transactions

The api can be explored with the help of Django REST framework,
so simply run the server after installation and use a web browser.

#### Basic routes
 - /transactions: a transaction is an operation between a account and a referer
 - /balances: the balance status of an account, when adding a transaction it will affect it's balance


## install
`cd api`<br />
`pip install virtualenv`<br />
`virtualenv venv`<br />
`source venv/bin/activate`<br />
`pip install -r requirements.txt `<br />

## run migrations
`python manage.py migrate`<br />

## Run
`python manage.py runserver`<br />