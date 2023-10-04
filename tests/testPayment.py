import unittest
from datetime import date

import Exceptions
from Models.CreditCard import CreditCard
from Controllers import ControllerCreditCard
import testControllerCreditCards


class TestPayment(unittest.TestCase):
    """Tests for the calc monthly payment and calc total interest functions"""

    # TEST FIXTURES
    # Code that runs before each test

    def setUpClass():
        """ Executed at the beginning of all tests """
        print("Invoking setUpClass")
        ControllerCreditCard.create_table()
        tests_credit_cards = testControllerCreditCards.TestControllerCreditCard()  # Ensure that at the beginning of the tests, the table is created
        tests_credit_cards.test_01_insert_credit_card_1()
        tests_credit_cards.test_01_insert_credit_card_2()
        tests_credit_cards.test_01_insert_credit_card_4()
        tests_credit_cards.test_01_insert_credit_card_5()

    def tearDownClass():
        """ Executed at the end of all tests """
        print("Invoking tearDownClass")
        ControllerCreditCard.delete_all_rows()

    def test_02_credit_card_purchase_1(self):
        amount: float = 200000
        card_number: str = "556677"
        installments: int = 36

        searched_card = ControllerCreditCard.search_by_card_id(card_number)

        credit_card = CreditCard(searched_card.card_number, searched_card.owner_id, searched_card.owner_name,
                                 searched_card.bank_name, searched_card.due_date, searched_card.franchise,
                                 searched_card.payment_day, searched_card.monthly_fee, searched_card.interest_rate)
        result_monthly_payment = credit_card.calc_monthly_payment(amount, installments)
        result_total_interest = credit_card.calc_total_interest(amount, installments)
        expected_monthly_payment_output: float = 9297.9591
        expected_total_interest: float = 134726.53
        self.assertEqual(result_total_interest, expected_total_interest)
        self.assertEqual(result_monthly_payment, expected_monthly_payment_output)

    def test_02_credit_card_purchase_2(self):
        amount: float = 850000
        card_number: str = "223344"
        installments: int = 24

        searched_card = ControllerCreditCard.search_by_card_id(card_number)

        credit_card = CreditCard(searched_card.card_number, searched_card.owner_id, searched_card.owner_name,
                                 searched_card.bank_name, searched_card.due_date, searched_card.franchise,
                                 searched_card.payment_day, searched_card.monthly_fee, searched_card.interest_rate)
        result_monthly_payment = credit_card.calc_monthly_payment(amount, installments)
        result_total_interest = credit_card.calc_total_interest(amount, installments)
        expected_monthly_payment_output: float = 52377.4986
        expected_total_interest: float = 407059.97
        self.assertEqual(result_total_interest, expected_total_interest)
        self.assertEqual(result_monthly_payment, expected_monthly_payment_output)

    def test_02_credit_card_purchase_3(self):
        amount: float = 480000
        card_number: str = "445566"
        installments: int = 48

        searched_card = ControllerCreditCard.search_by_card_id(card_number)

        credit_card = CreditCard(searched_card.card_number, searched_card.owner_id, searched_card.owner_name,
                                 searched_card.bank_name, searched_card.due_date, searched_card.franchise,
                                 searched_card.payment_day, searched_card.monthly_fee, searched_card.interest_rate)
        result_monthly_payment = credit_card.calc_monthly_payment(amount, installments)
        result_total_interest = credit_card.calc_total_interest(amount, installments)
        expected_monthly_payment_output: float = 10000
        expected_total_interest: float = 0
        self.assertEqual(result_total_interest, expected_total_interest)
        self.assertEqual(result_monthly_payment, expected_monthly_payment_output)

    def test_02_credit_card_purchase_4(self):
        amount: float = 90000
        card_number: str = "445566"
        installments: int = 1

        searched_card = ControllerCreditCard.search_by_card_id(card_number)

        credit_card = CreditCard(searched_card.card_number, searched_card.owner_id, searched_card.owner_name,
                                 searched_card.bank_name, searched_card.due_date, searched_card.franchise,
                                 searched_card.payment_day, searched_card.monthly_fee, searched_card.interest_rate)
        result_monthly_payment = credit_card.calc_monthly_payment(amount, installments)
        result_total_interest = credit_card.calc_total_interest(amount, installments)
        expected_monthly_payment_output: float = 90000
        expected_total_interest: float = 0
        self.assertEqual(result_total_interest, expected_total_interest)
        self.assertEqual(result_monthly_payment, expected_monthly_payment_output)

    def test_02_credit_card_purchase_5(self):
        amount: float = 0
        card_number: str = "223344"
        installments: int = 60

        searched_card = ControllerCreditCard.search_by_card_id(card_number)

        credit_card = CreditCard(searched_card.card_number, searched_card.owner_id, searched_card.owner_name,
                                 searched_card.bank_name, searched_card.due_date, searched_card.franchise,
                                 searched_card.payment_day, searched_card.monthly_fee, searched_card.interest_rate)

        self.assertRaises(Exceptions.ZeroAmountError, credit_card.calc_monthly_payment, amount, installments)

    def test_02_credit_card_purchase_6(self):
        amount: float = 50000
        card_number: str = "556677"
        installments: int = -10

        searched_card = ControllerCreditCard.search_by_card_id(card_number)

        credit_card = CreditCard(searched_card.card_number, searched_card.owner_id, searched_card.owner_name,
                                 searched_card.bank_name, searched_card.due_date, searched_card.franchise,
                                 searched_card.payment_day, searched_card.monthly_fee, searched_card.interest_rate)

        self.assertRaises(Exceptions.NegativeNumberOfPaymentsError, credit_card.calc_monthly_payment, amount, installments)

    def test_02_credit_card_purchase_7(self):
        amount: float = 50000
        card_number: str = "885522"
        installments: int = 10

        self.assertRaises(Exceptions.CardNotFoundError, ControllerCreditCard.search_by_card_id, card_number)


if __name__ == '__main__':
    unittest.main()
