import sys
import psycopg2
import SecretConfig

from Models.PaymentPlan import PaymentPlan


def get_cursor():
    """
    Create the connection to the database and return a cursor to execute instructions
    """
    DATABASE = SecretConfig.DATABASE
    USER = SecretConfig.USER
    PASSWORD = SecretConfig.PASSWORD
    HOST = SecretConfig.HOST
    PORT = SecretConfig.PORT
    connection = psycopg2.connect(database=DATABASE, user=USER, password=PASSWORD, host=HOST, port=PORT)
    return connection.cursor()


def create_table():
    """
    Creates  table if it does not exist
    """
    sql = ""
    with open("sql/create-payment-plan.sql", "r") as f:
        sql = f.read()

    cursor = get_cursor()

    try:
        cursor.execute(sql)
        cursor.connection.commit()
    except:
        # Table already exists
        cursor.connection.rollback()


def delete_table():
    """
    Deletes the table completely and all its data
    """
    sql = "DROP TABLE payment_plans;"
    cursor = get_cursor()
    cursor.execute(sql)
    cursor.connection.commit()


def delete_all_rows():
    """
    Deletes all the rows of the table
    """
    sql = "DELETE FROM payment_plans"
    cursor = get_cursor()
    cursor.execute(sql)
    cursor.connection.commit()


def insert_payment_plan(payment_plan: PaymentPlan):
    pass
