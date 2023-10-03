import unittest

from datetime import date

from Models.CreditCard import CreditCard
from Controllers import ControllerCreditCard

# All unit tests import the unittest library
import unittest
from datetime import date
from Models.CreditCard import CreditCard
from Controllers import ControllerCreditCard


class ControllerTest(unittest.TestCase):
    """
    Tests for the Controller Class of the application
    """

    # TEST FIXTURES
    # Code that runs before each test

    def setUp(self):
        """ Executed always before each test method """
        print("Invoking setUp")
        ControllerCreditCard.delete_all_rows()  # Ensure that before each test method, all data in the table is deleted

    def setUpClass():
        """ Executed at the beginning of all tests """
        print("Invoking setUpClass")
        ControllerCreditCard.create_table()  # Ensure that at the beginning of the tests, the table is created

    def tearDown(self):
        """ Executed at the end of each test """
        print("Invoking tearDown")

    def tearDownClass():
        """ Executed at the end of all tests """
        print("Invoking tearDownClass")

    def test_insert_credit_card(self):
        """Verifies that the monthly payment calculation function returns correct values"""
        amount: float = 200000
        interest_rate: float = 3.1
        number_of_payments: int = 36
        credit_card
        result: float = round(calc.calc_monthly_payment(), 2)
        expected_result: float = 9297.96
        self.assertEqual(result, expected_result)