from datetime import date, datetime, timedelta
from Models.CreditCard import CreditCard


class PaymentPlan:
    """
    Represents a payment plan in the system
    """
    def __init__(self, card_number, purchase_date, purchase_amount):
        self.card_number = card_number
        self.purchase_date: date = purchase_date
        self.purchase_amount: float = purchase_amount
        self.payment_date: date = self.purchase_date
        self.interest_amount: float = 0
        self.capital_amount: float = 0
        self.balance: float = 0
        self.payment_amount: float = 0

    def calc_payment_plan(self, credit_card: CreditCard, installments) -> list:
        """Creates a payment plan"""
        payment_value: float = round(credit_card.calc_monthly_payment(self.purchase_amount, installments), 2)
        self.balance: float = self.purchase_amount
        self.payment_date = self.purchase_date.replace(day=credit_card.payment_day)
        amortization_table: list = []
        if installments == 1:
            self.capital_amount = payment_value
            row = [1, self.purchase_date, self.purchase_amount, self.purchase_date, 0, self.capital_amount, 0]
            amortization_table.append(row)
        else:
            for payment in range(1, installments + 1):
                payment_number = payment
                self.interest_amount: float = round(credit_card.interest_percentage * self.balance, 2)
                self.capital_amount: float = round(payment_value - self.interest_amount, 2)
                self.balance: float = round(self.balance - self.capital_amount, 2)
                if self.payment_date.month == 12:
                    self.payment_date = self.payment_date.replace(year=self.payment_date.year + 1, month=1)
                else:
                    self.payment_date = self.payment_date.replace(month=self.payment_date.month + 1)
                if 0 > self.balance > -0.1:
                    self.balance = 0
                self.payment_amount = self.interest_amount + self.capital_amount
                row: list = [payment_number, self.card_number, self.purchase_date, self.purchase_amount, self.payment_date,
                             self.payment_amount, self.interest_amount, self.capital_amount, self.balance]
                amortization_table.append(row)
        return amortization_table
