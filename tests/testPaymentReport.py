import unittest
from datetime import date

from Controllers import ControllerPaymentPlan
from Controllers import ControllerCreditCard
import testControllerCreditCards


class TestPaymentReport(unittest.TestCase):
    """Tests for the calc total payment in x interval"""

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

    def test_05_payment_report_1(self):
        pass
