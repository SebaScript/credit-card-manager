from datetime import date


class PaymentPlan:
    """
    Represents a payment plan in the system
    """
    def __init__(self, purchase_date, purchase_amount, payment_date, payment_amount, interest_amount, capital_amount, balance):
        self.purchase_date: date = purchase_date
        self.purchase_amount: float = purchase_amount
        self.payment_date: date = payment_amount
        self.interest_amount: float = interest_amount
        self.capital_amount: float = capital_amount
        self.balance: float = balance

