import unittest
from datetime import date

from Controllers import ControllerPaymentPlan
from Controllers import ControllerCreditCard
import testControllerCreditCards
from testPaymentPlan import ControllerPaymentPlanTest


class TestPaymentReport(unittest.TestCase):
    """Tests for the calc total payment in x interval"""

    # TEST FIXTURES
    # Code that runs before each test

    def setUp(self):
        card_number: str = "556677"
        purchase_date: date = date.fromisoformat("2023-09-22")
        amount: float = 200000
        installments: int = 36
        payment_plan = ControllerPaymentPlan.insert_payment_plan(card_number, amount, purchase_date, installments)
        card_number: str = "223344"
        purchase_date: date = date.fromisoformat("2023-09-25")
        amount: float = 850000
        installments: int = 24
        payment_plan = ControllerPaymentPlan.insert_payment_plan(card_number, amount, purchase_date, installments)
        card_number: str = "445566"
        purchase_date: date = date.fromisoformat("2023-09-29")
        amount: float = 480000
        installments: int = 48
        payment_plan = ControllerPaymentPlan.insert_payment_plan(card_number, amount, purchase_date, installments)
        card_number: str = "445566"
        purchase_date: date = date.fromisoformat("2023-11-17")
        amount: float = 90000
        installments: int = 1
        payment_plan = ControllerPaymentPlan.insert_payment_plan(card_number, amount, purchase_date, installments)

    def setUpClass():
        """ Executed at the beginning of all tests """
        print("Invoking setUpClass")
        ControllerPaymentPlan.create_table()  # Ensure that at the beginning of the tests, the table is created
        ControllerCreditCard.delete_all_rows()
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
        ControllerPaymentPlan.delete_all_rows()

    def test_05_payment_report_1(self):

        initial_date: date = date.fromisoformat("2023-10-01")
        final_date: date = date.fromisoformat("2023-10-31")

        total: float = ControllerPaymentPlan.calc_total_payment_in_x_interval(initial_date, final_date)
        expected: float = 71675
        ControllerPaymentPlan.delete_all_rows()

        self.assertEqual(total, expected)

    def test_05_payment_report_2(self):

        initial_date: date = date.fromisoformat("2023-10-01")
        final_date: date = date.fromisoformat("2023-12-31")

        total: float = ControllerPaymentPlan.calc_total_payment_in_x_interval(initial_date, final_date)
        expected: float = 305026
        ControllerPaymentPlan.delete_all_rows()

        self.assertEqual(total, expected)

    def test_05_payment_report_3(self):

        initial_date: date = date.fromisoformat("2026-01-01")
        final_date: date = date.fromisoformat("2026-12-31")

        total: float = ControllerPaymentPlan.calc_total_payment_in_x_interval(initial_date, final_date)
        expected: float = 203682
        ControllerPaymentPlan.delete_all_rows()

        self.assertEqual(total, expected)
