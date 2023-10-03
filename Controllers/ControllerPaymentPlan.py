import sys
import psycopg2
import SecretConfig
from datetime import date
from ControllerCreditCard import CreditCard

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
    with open("../sql/create-payment-plan.sql", "r") as f:
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


def insert_payment_plan(card_number, purchase_amount, purchase_date, installments):
    """Inserts a payment plan in the database, where each row is an installment"""
    cursor = get_cursor()
    sql = f"""SELECT card_number, owner_id, owner_name, bank_name, due_date, franchise, payment_day, monthly_fee, 
    interest_rate FROM credit_cards WHERE card_number = '{card_number}'"""
    cursor.execute(sql)
    row = cursor.fetchone()

    if row is None:
        raise Exception(f"record with card number: {card_number} was not found")

    credit_card = CreditCard(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8])

    payment_plan = PaymentPlan(card_number, purchase_date, purchase_amount)

    table = payment_plan.calc_payment_plan(credit_card, installments)

    for row in table:
        sql = f"""INSERT INTO payment_plans(
            Number, card_number, purchase_date, purchase_amount, payment_date, payment_amount, interest_amount,
            capital_amount, balance
            )
            VALUES(
                '{row[0]}','{row[1]}','{row[2]}','{row[3]}','{row[4]}','{row[5]}','{row[6]}','{row[7]}', '{row[8]}'
            );"""
        cursor.execute(sql)
    cursor.connection.commit()


def calc_total_payment_in_x_months(months) -> float:
    """Calculates the sum of the monthly payments in a specified range of months"""
    cursor = get_cursor()
    sum: float = 0
    for i in range(months+1):
        if i == 0:
            continue
        print(i)
        cursor.execute(f"SELECT payment_amount FROM payment_plans WHERE number = '{i}'")
        result = cursor.fetchone()
        sum += result[0]
    return sum


delete_table()
create_table()
insert_payment_plan(556677, 200000, date.fromisoformat("2023-09-02"), 36)
print(calc_total_payment_in_x_months(2))
