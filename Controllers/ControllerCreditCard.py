import sys
import psycopg2
import SecretConfig
from datetime import date
from Models.CreditCard import CreditCard


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
    with open("../sql/create-credit-card.sql", "r") as f:
        sql = f.read()

    cursor = get_cursor()

    try:
        cursor.execute(sql)
        cursor.connection.commit()
        print("table created succesfully")
    except Exception as err:
        # Table already exists
        print(err)
        cursor.connection.rollback()


def delete_table():
    """
    Deletes the table completely and all its data
    """
    sql = "DROP TABLE credit_cards;"
    cursor = get_cursor()
    cursor.execute(sql)
    cursor.connection.commit()


def delete_all_rows():
    """
    Deletes all the rows of the table
    """
    sql = "DELETE FROM credit_cards"
    cursor = get_cursor()
    cursor.execute(sql)
    cursor.connection.commit()


def delete_single_credit_card(credit_card):
    """
    Deletes a single credit card from the table
    """
    sql = f"DELETE FROM credit_cards WHERE card_number = '{credit_card.card_number}'"
    cursor = get_cursor()
    cursor.execute(sql)
    cursor.connection.commit()


def insert_credit_card(credit_card: CreditCard):
    """
    Saves a credit_card in the database
    """

    cursor = get_cursor()

    try:

        cursor.execute(f"""
        INSERT INTO credit_cards (
            card_number, owner_id, owner_name, bank_name, due_date, franchise, payment_day, monthly_fee, interest_rate
        )
        VALUES (
            '{credit_card.card_number}', '{credit_card.owner_id}', '{credit_card.owner_name}', 
            '{credit_card.bank_name}', '{credit_card.due_date}', '{credit_card.franchise}', {credit_card.payment_day},
            '{credit_card.monthly_fee}', '{credit_card.interest_rate}'
        );
                        """)

        insert_credit_card(credit_card)
        cursor.connection.commit()

    except Exception as err:
        print(err)
        cursor.connection.rollback()


create_table()
creditcard = CreditCard(123, 123, "ola", "como", date.fromisoformat("2050-11-11"), "BISA", "12", 15600, 3.10)
insert_credit_card(creditcard)
