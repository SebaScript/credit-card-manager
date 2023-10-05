import unittest
from datetime import date

import Exceptions
from Models.CreditCard import CreditCard


class TestPlannedSaving(unittest.TestCase):

    def test_03_planned_saving_1(self):
        amount: float = 200000
        interest_rate: float = 0.90
        monthly_amount: float = 6528.817139
        credit_card = CreditCard("sd", "asj", "asf", "afg", date.fromisoformat("2023-11-01"), "asd", 10, 2123, interest_rate)
        result = credit_card.calc_planned_saving(monthly_amount, amount)
        expected = 28
        self.assertEqual(result, expected)

    def test_03_planned_saving_2(self):
        amount: float = 850000
        interest_rate: float = 0.90
        monthly_amount: float = 39537.78219
        credit_card = CreditCard("sd", "asj", "asf", "afg", date.fromisoformat("2023-11-01"), "asd", 10, 2123, interest_rate)
        result = credit_card.calc_planned_saving(monthly_amount, amount)
        expected = 20
        self.assertEqual(result, expected)

    def test_03_planned_saving_3(self):
        amount: float = 480000
        interest_rate: float = 0.90
        monthly_amount: float = 10000
        credit_card = CreditCard("sd", "asj", "asf", "afg", date.fromisoformat("2023-11-01"), "asd", 10, 2123, interest_rate)
        result = credit_card.calc_planned_saving(monthly_amount, amount)
        expected = 41
        self.assertEqual(result, expected)

    def test_03_planned_saving_4(self):
        amount: float = 90000
        interest_rate: float = 0.90
        monthly_amount: float = 90000
        credit_card = CreditCard("sd", "asj", "asf", "afg", date.fromisoformat("2023-11-01"), "asd", 10, 2123, interest_rate)
        result = credit_card.calc_planned_saving(monthly_amount, amount)
        expected = 1
        self.assertEqual(result, expected)
