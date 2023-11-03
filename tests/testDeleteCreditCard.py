import unittest
from datetime import date

import Exceptions
from Models.CreditCard import CreditCard
from Controllers import ControllerCreditCard
import testControllerCreditCards


class TestPayment(unittest.TestCase):
    """Test for the delete credit card function"""

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

    def test_07_delete_credit_card_01(self):
        card_number: str = "556677"

        ControllerCreditCard.delete_credit_card(card_number)

        self.assertRaises(Exceptions.CardNotFoundError, ControllerCreditCard.search_by_card_id, card_number)
