from datetime import date
import Exceptions


MAXANUALINTEREST = 100


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
        self.ANUALINTEREST = self.interest_rate * 12
        self.interest_percentage = self.interest_rate/100

    def calc_monthly_payment(self, amount, installments) -> float:
        """
        Calculates the monthly payment for an installment purchase
        """
        if amount == 0:
            raise Exceptions.ZeroAmountError
        elif installments <= 0:
            raise Exceptions.NegativeNumberOfPaymentsError
        if self.interest_rate == 0:
            return amount / installments
        if installments == 1:
            return amount
        else:
            return round((amount * self.interest_percentage)/(1 - (1 + self.interest_percentage)**(-installments)), 4)

    def calc_total_interest(self, amount, installments) -> float:
        """calculates the total interest payment for an installment purchase"""
        payment_value: float = self.calc_monthly_payment(amount, installments)
        total_interest: float = round((payment_value * installments) - amount, 2)
        return total_interest

    def calc_planned_saving(self, amount, installments) -> int:
        """
        calculates the number of months that the user should save to make the same
        purchase instead of buying it in installments
        """
        monthly_payment = self.calc_monthly_payment(amount, installments)
        months_saving: int = 0
        while monthly_payment < amount:
            monthly_payment += monthly_payment
            months_saving += 1
        return months_saving
