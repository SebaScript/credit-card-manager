from datetime import date


class CreditCard:
    """
    Represents a credit card in the system
    """
    def __init__(self, card_number, owner_id, owner_name, bank_name, due_date, franchise, payment_day, monthly_fee,
                 interest_rate):
        self.card_number: int = card_number
        self.owner_id: int = owner_id
        self.owner_name: str = owner_name
        self.bank_name: str = bank_name
        self.due_date: date = due_date
        self.franchise: str = franchise
        self.payment_day: int = payment_day
        self.monthly_fee: float = monthly_fee
        self.interest_rate: float = interest_rate
        self.payment_plans: list = []
