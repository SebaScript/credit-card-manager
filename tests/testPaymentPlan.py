import unittest
from datetime import date

from Models.PaymentPlan import PaymentPlan
from Controllers import ControllerPaymentPlan


class ControllerPaymentPlanTest(unittest.TestCase):
    """
    Tests for the Controller Class of the credit card
    """

    # TEST FIXTURES
    # Code that runs before each test

    def setUpClass():
        """ Executed at the beginning of all tests """
        print("Invoking setUpClass")
        ControllerPaymentPlan.create_table()  # Ensure that at the beginning of the tests, the table is created

    def tearDown(self):
        """ Executed at the end of each test """
        print("Invoking tearDown")

    def tearDownClass():
        """ Executed at the end of all tests """
        print("Invoking tearDownClass")
        ControllerPaymentPlan.delete_all_rows()

