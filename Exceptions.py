class ZeroAmountError(Exception):
    """The amount must be greater than zero"""


class NegativeNumberOfPaymentsError(Exception):
    """The number of installments must be greater than zero"""


class CardNotFoundError(Exception):
    """The indicated card does not exist"""


class CreditCardAlreadyExists(Exception):
    """The credit card already exists"""
