# Credit card manager

Web software for managing credit cards and installment purchases applying Clean Code and using PostgreSQL Database.

Recommendation: due to file import issues, I recommend opening the software in PyCharm.

By: Juan Sebastian Garcia Perez

## Database configuration

- Create an account on https://neon.tech/

- Create a database on neondb.

- Get the connection details in the dashboard of your database on neondb.

- Run the following command to install PsycoPG2 on your project:
pip install psycopg2

- Open SecretConfig-Sample.py and follow the given instructions to initialize the project with your own database.

- The "Controllers" directory contains the modules that perform the operations on the database.

- Create the tables in the database by executing the create_table() functions in ControllerCreditCard and ControllerPaymentPlan.

## Tests

Run the tests using the following command in your terminal:

tests>python -m unittest discover . -p test*.py

## Web service

- Run the following command in your teminal to install flask:
    pip install flask

- Execute the web server running the app.py module, then go to the adress given in the terminal and use the route you need (you can guide yourself with the example routes in the code comments).

## Web UI

- Run the following command in your terminal to install flask:
    pip install flask

- Execute the web user interface running the view.py module, then go to the adress given in the terminal and navigate between the different options.
