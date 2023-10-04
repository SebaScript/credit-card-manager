import unittest
from datetime import date

import Exceptions
from Models.CreditCard import CreditCard
from Controllers import ControllerCreditCard


class TestControllerCreditCard(unittest.TestCase):
    """Tests for the Controller Class of the credit card"""

    # TEST FIXTURES
    # Code that runs before each test

    def setUpClass():
        """ Executed at the beginning of all tests """
        print("Invoking setUpClass")
        ControllerCreditCard.create_table()  # Ensure that at the beginning of the tests, the table is created

    def tearDownClass():
        """ Executed at the end of all tests """
        print("Invoking tearDownClass")
        ControllerCreditCard.delete_all_rows()

    def test_01_insert_credit_card_1(self):
        """Verifies that the credit card is inserted succesfully in the database"""
        card_number: str = "556677"
        owner_id: str = "1010123456"
        owner_name: str = "comprador compulsivo"
        bank_name: str = "Bancolombia"
        due_date: date = date.fromisoformat("2027-12-31")
        franchise: str = "VISA"
        payment_day: int = 10
        monthly_fee: float = 24000
        interest_rate: float = 3.1

        credit_card_test = CreditCard(card_number, owner_id, owner_name, bank_name, due_date, franchise, payment_day, monthly_fee, interest_rate)

        ControllerCreditCard.insert_credit_card(credit_card_test)

        searched_credit_card = ControllerCreditCard.search_by_card_id(credit_card_test.card_number)

        self.assertEqual(credit_card_test.card_number, searched_credit_card.card_number)
        self.assertEqual(credit_card_test.owner_id, searched_credit_card.owner_id)
        self.assertEqual(credit_card_test.owner_name, searched_credit_card.owner_name)
        self.assertEqual(credit_card_test.bank_name, searched_credit_card.bank_name)
        self.assertEqual(credit_card_test.due_date, searched_credit_card.due_date)
        self.assertEqual(credit_card_test.franchise, searched_credit_card.franchise)
        self.assertEqual(credit_card_test.payment_day, searched_credit_card.payment_day)
        self.assertEqual(credit_card_test.monthly_fee, searched_credit_card.monthly_fee)
        self.assertEqual(credit_card_test.interest_rate, searched_credit_card.interest_rate)

    def test_01_insert_credit_card_2(self):
        """Verifies that the credit card is inserted succesfully in the database"""
        card_number: str = "442233"
        owner_id: str = "1010123456"
        owner_name: str = "comprador compulsivo"
        bank_name: str = "Popular"
        due_date: date = date.fromisoformat("2022-12-31")
        franchise: str = "Mastercard"
        payment_day: int = 5
        monthly_fee: float = 34000
        interest_rate: float = 3.4

        credit_card_test = CreditCard(card_number, owner_id, owner_name, bank_name, due_date, franchise, payment_day, monthly_fee, interest_rate)

        ControllerCreditCard.insert_credit_card(credit_card_test)

        searched_credit_card = ControllerCreditCard.search_by_card_id(credit_card_test.card_number)

        self.assertEqual(credit_card_test.card_number, searched_credit_card.card_number)
        self.assertEqual(credit_card_test.owner_id, searched_credit_card.owner_id)
        self.assertEqual(credit_card_test.owner_name, searched_credit_card.owner_name)
        self.assertEqual(credit_card_test.bank_name, searched_credit_card.bank_name)
        self.assertEqual(credit_card_test.due_date, searched_credit_card.due_date)
        self.assertEqual(credit_card_test.franchise, searched_credit_card.franchise)
        self.assertEqual(credit_card_test.payment_day, searched_credit_card.payment_day)
        self.assertEqual(credit_card_test.monthly_fee, searched_credit_card.monthly_fee)
        self.assertEqual(credit_card_test.interest_rate, searched_credit_card.interest_rate)

    def test_01_insert_credit_card_3(self):
        """Verifies that the credit card is inserted succesfully in the database"""
        card_number: str = "556677"
        owner_id: str = "1020889955"
        owner_name: str = "Estudiante pelao"
        bank_name: str = "Bancolombia"
        due_date: date = date.fromisoformat("2027-12-31")
        franchise: str = "VISA"
        payment_day: int = 10
        monthly_fee: float = 24000
        interest_rate: float = 3.1

        credit_card_test = CreditCard(card_number, owner_id, owner_name, bank_name, due_date, franchise, payment_day, monthly_fee, interest_rate)

        self.assertRaises(Exceptions.CreditCardAlreadyExists, ControllerCreditCard.insert_credit_card, credit_card_test)

    def test_01_insert_credit_card_4(self):
        """Verifies that the credit card is inserted succesfully in the database"""
        card_number: str = "223344"
        owner_id: str = "1010123456"
        owner_name: str = "comprador compulsivo"
        bank_name: str = "Falabella"
        due_date: date = date.fromisoformat("2025-12-31")
        franchise: str = "VISA"
        payment_day: int = 16
        monthly_fee: float = 0
        interest_rate: float = 3.4

        credit_card_test = CreditCard(card_number, owner_id, owner_name, bank_name, due_date, franchise, payment_day, monthly_fee, interest_rate)

        ControllerCreditCard.insert_credit_card(credit_card_test)

        searched_credit_card = ControllerCreditCard.search_by_card_id(credit_card_test.card_number)

        self.assertEqual(credit_card_test.card_number, searched_credit_card.card_number)
        self.assertEqual(credit_card_test.owner_id, searched_credit_card.owner_id)
        self.assertEqual(credit_card_test.owner_name, searched_credit_card.owner_name)
        self.assertEqual(credit_card_test.bank_name, searched_credit_card.bank_name)
        self.assertEqual(credit_card_test.due_date, searched_credit_card.due_date)
        self.assertEqual(credit_card_test.franchise, searched_credit_card.franchise)
        self.assertEqual(credit_card_test.payment_day, searched_credit_card.payment_day)
        self.assertEqual(credit_card_test.monthly_fee, searched_credit_card.monthly_fee)
        self.assertEqual(credit_card_test.interest_rate, searched_credit_card.interest_rate)

    def test_01_insert_credit_card_5(self):
        """Verifies that the credit card is inserted succesfully in the database"""
        card_number: str = "445566"
        owner_id: str = "1010123456"
        owner_name: str = "comprador compulsivo"
        bank_name: str = "BBVA"
        due_date: date = date.fromisoformat("2027-12-31")
        franchise: str = "Mastercard"
        payment_day: int = 5
        monthly_fee: float = 34000
        interest_rate: float = 0

        credit_card_test = CreditCard(card_number, owner_id, owner_name, bank_name, due_date, franchise, payment_day, monthly_fee, interest_rate)

        ControllerCreditCard.insert_credit_card(credit_card_test)

        searched_credit_card = ControllerCreditCard.search_by_card_id(credit_card_test.card_number)

        self.assertEqual(credit_card_test.card_number, searched_credit_card.card_number)
        self.assertEqual(credit_card_test.owner_id, searched_credit_card.owner_id)
        self.assertEqual(credit_card_test.owner_name, searched_credit_card.owner_name)
        self.assertEqual(credit_card_test.bank_name, searched_credit_card.bank_name)
        self.assertEqual(credit_card_test.due_date, searched_credit_card.due_date)
        self.assertEqual(credit_card_test.franchise, searched_credit_card.franchise)
        self.assertEqual(credit_card_test.payment_day, searched_credit_card.payment_day)
        self.assertEqual(credit_card_test.monthly_fee, searched_credit_card.monthly_fee)
        self.assertEqual(credit_card_test.interest_rate, searched_credit_card.interest_rate)

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

    # def test_02_credit_card_purchase_7(self):
    #     amount: float = 50000
    #     card_number: str = "885522"
    #     installments: int = 10
    #
    #     searched_card = ControllerCreditCard.search_by_card_id(card_number)
    #
    #     credit_card = CreditCard(searched_card.card_number, searched_card.owner_id, searched_card.owner_name,
    #                              searched_card.bank_name, searched_card.due_date, searched_card.franchise,
    #                              searched_card.payment_day, searched_card.monthly_fee, searched_card.interest_rate)
    #
    #     self.assertRaises(Exceptions.CardNotFoundError, credit_card.calc_monthly_payment, amount, installments)

