import unittest
from datetime import date
import datetime

from Models.PaymentPlan import PaymentPlan
from Controllers import ControllerPaymentPlan
from Controllers import ControllerCreditCard
from Models.PaymentPlan import PaymentPlan
import testControllerCreditCards


class ControllerPaymentPlanTest(unittest.TestCase):
    """Tests for the Controller Class of the payment plan"""

    # TEST FIXTURES
    # Code that runs before each test

    def setUp(self):
        ControllerPaymentPlan.delete_all_rows()

    def setUpClass():
        """ Executed at the beginning of all tests """
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

    def test_04_payment_plan_1(self):
        card_number: str = "556677"
        purchase_date: date = date.fromisoformat("2023-09-22")
        amount: float = 200000
        installments: int = 36

        payment_plan = ControllerPaymentPlan.insert_payment_plan(card_number, amount, purchase_date, installments)
        expected = [[1, '556677', datetime.date(2023, 9, 22), 200000, datetime.date(2023, 10, 10), 9297.96, 6200.0, 3097.96, 196902.04], [2, '556677', datetime.date(2023, 9, 22), 200000, datetime.date(2023, 11, 10), 9297.96, 6103.96, 3194.0, 193708.04], [3, '556677', datetime.date(2023, 9, 22), 200000, datetime.date(2023, 12, 10), 9297.96, 6004.95, 3293.01, 190415.03], [4, '556677', datetime.date(2023, 9, 22), 200000, datetime.date(2024, 1, 10), 9297.96, 5902.87, 3395.09, 187019.94], [5, '556677', datetime.date(2023, 9, 22), 200000, datetime.date(2024, 2, 10), 9297.96, 5797.62, 3500.34, 183519.6], [6, '556677', datetime.date(2023, 9, 22), 200000, datetime.date(2024, 3, 10), 9297.96, 5689.11, 3608.85, 179910.75], [7, '556677', datetime.date(2023, 9, 22), 200000, datetime.date(2024, 4, 10), 9297.96, 5577.23, 3720.73, 176190.02], [8, '556677', datetime.date(2023, 9, 22), 200000, datetime.date(2024, 5, 10), 9297.96, 5461.89, 3836.07, 172353.95], [9, '556677', datetime.date(2023, 9, 22), 200000, datetime.date(2024, 6, 10), 9297.96, 5342.97, 3954.99, 168398.96], [10, '556677', datetime.date(2023, 9, 22), 200000, datetime.date(2024, 7, 10), 9297.96, 5220.37, 4077.59, 164321.37], [11, '556677', datetime.date(2023, 9, 22), 200000, datetime.date(2024, 8, 10), 9297.96, 5093.96, 4204.0, 160117.37], [12, '556677', datetime.date(2023, 9, 22), 200000, datetime.date(2024, 9, 10), 9297.96, 4963.64, 4334.32, 155783.05], [13, '556677', datetime.date(2023, 9, 22), 200000, datetime.date(2024, 10, 10), 9297.96, 4829.27, 4468.69, 151314.36], [14, '556677', datetime.date(2023, 9, 22), 200000, datetime.date(2024, 11, 10), 9297.96, 4690.75, 4607.21, 146707.15], [15, '556677', datetime.date(2023, 9, 22), 200000, datetime.date(2024, 12, 10), 9297.96, 4547.92, 4750.04, 141957.11], [16, '556677', datetime.date(2023, 9, 22), 200000, datetime.date(2025, 1, 10), 9297.96, 4400.67, 4897.29, 137059.82], [17, '556677', datetime.date(2023, 9, 22), 200000, datetime.date(2025, 2, 10), 9297.96, 4248.85, 5049.11, 132010.71], [18, '556677', datetime.date(2023, 9, 22), 200000, datetime.date(2025, 3, 10), 9297.96, 4092.33, 5205.63, 126805.08], [19, '556677', datetime.date(2023, 9, 22), 200000, datetime.date(2025, 4, 10), 9297.96, 3930.96, 5367.0, 121438.08], [20, '556677', datetime.date(2023, 9, 22), 200000, datetime.date(2025, 5, 10), 9297.96, 3764.58, 5533.38, 115904.7], [21, '556677', datetime.date(2023, 9, 22), 200000, datetime.date(2025, 6, 10), 9297.96, 3593.05, 5704.91, 110199.79], [22, '556677', datetime.date(2023, 9, 22), 200000, datetime.date(2025, 7, 10), 9297.96, 3416.19, 5881.77, 104318.02], [23, '556677', datetime.date(2023, 9, 22), 200000, datetime.date(2025, 8, 10), 9297.96, 3233.86, 6064.1, 98253.92], [24, '556677', datetime.date(2023, 9, 22), 200000, datetime.date(2025, 9, 10), 9297.96, 3045.87, 6252.09, 92001.83], [25, '556677', datetime.date(2023, 9, 22), 200000, datetime.date(2025, 10, 10), 9297.96, 2852.06, 6445.9, 85555.93], [26, '556677', datetime.date(2023, 9, 22), 200000, datetime.date(2025, 11, 10), 9297.96, 2652.23, 6645.73, 78910.2], [27, '556677', datetime.date(2023, 9, 22), 200000, datetime.date(2025, 12, 10), 9297.96, 2446.22, 6851.74, 72058.46], [28, '556677', datetime.date(2023, 9, 22), 200000, datetime.date(2026, 1, 10), 9297.96, 2233.81, 7064.15, 64994.31], [29, '556677', datetime.date(2023, 9, 22), 200000, datetime.date(2026, 2, 10), 9297.96, 2014.82, 7283.14, 57711.17], [30, '556677', datetime.date(2023, 9, 22), 200000, datetime.date(2026, 3, 10), 9297.96, 1789.05, 7508.91, 50202.26], [31, '556677', datetime.date(2023, 9, 22), 200000, datetime.date(2026, 4, 10), 9297.96, 1556.27, 7741.69, 42460.57], [32, '556677', datetime.date(2023, 9, 22), 200000, datetime.date(2026, 5, 10), 9297.96, 1316.28, 7981.68, 34478.89], [33, '556677', datetime.date(2023, 9, 22), 200000, datetime.date(2026, 6, 10), 9297.96, 1068.85, 8229.11, 26249.78], [34, '556677', datetime.date(2023, 9, 22), 200000, datetime.date(2026, 7, 10), 9297.96, 813.74, 8484.22, 17765.56], [35, '556677', datetime.date(2023, 9, 22), 200000, datetime.date(2026, 8, 10), 9297.96, 550.73, 8747.23, 9018.33], [36, '556677', datetime.date(2023, 9, 22), 200000, datetime.date(2026, 9, 10), 9297.96, 279.57, 9018.39, 0]]
        result = ControllerPaymentPlan.get_payment_plan()

        self.assertEqual(expected, result)

    def test_04_payment_plan_2(self):
        card_number: str = "223344"
        purchase_date: date = date.fromisoformat("2023-09-25")
        amount: float = 850000
        installments: int = 24

        payment_plan = ControllerPaymentPlan.insert_payment_plan(card_number, amount, purchase_date, installments)
        expected = [[1, '223344', datetime.date(2023, 9, 25), 850000, datetime.date(2023, 10, 16), 52377.5, 28900.0, 23477.5, 826522.5], [2, '223344', datetime.date(2023, 9, 25), 850000, datetime.date(2023, 11, 16), 52377.5, 28101.77, 24275.73, 802246.77], [3, '223344', datetime.date(2023, 9, 25), 850000, datetime.date(2023, 12, 16), 52377.5, 27276.39, 25101.11, 777145.66], [4, '223344', datetime.date(2023, 9, 25), 850000, datetime.date(2024, 1, 16), 52377.5, 26422.95, 25954.55, 751191.11], [5, '223344', datetime.date(2023, 9, 25), 850000, datetime.date(2024, 2, 16), 52377.5, 25540.5, 26837.0, 724354.11], [6, '223344', datetime.date(2023, 9, 25), 850000, datetime.date(2024, 3, 16), 52377.5, 24628.04, 27749.46, 696604.65], [7, '223344', datetime.date(2023, 9, 25), 850000, datetime.date(2024, 4, 16), 52377.5, 23684.56, 28692.94, 667911.71], [8, '223344', datetime.date(2023, 9, 25), 850000, datetime.date(2024, 5, 16), 52377.5, 22709.0, 29668.5, 638243.21], [9, '223344', datetime.date(2023, 9, 25), 850000, datetime.date(2024, 6, 16), 52377.5, 21700.27, 30677.23, 607565.98], [10, '223344', datetime.date(2023, 9, 25), 850000, datetime.date(2024, 7, 16), 52377.5, 20657.24, 31720.26, 575845.72], [11, '223344', datetime.date(2023, 9, 25), 850000, datetime.date(2024, 8, 16), 52377.5, 19578.75, 32798.75, 543046.97], [12, '223344', datetime.date(2023, 9, 25), 850000, datetime.date(2024, 9, 16), 52377.5, 18463.6, 33913.9, 509133.07], [13, '223344', datetime.date(2023, 9, 25), 850000, datetime.date(2024, 10, 16), 52377.5, 17310.52, 35066.98, 474066.09], [14, '223344', datetime.date(2023, 9, 25), 850000, datetime.date(2024, 11, 16), 52377.5, 16118.25, 36259.25, 437806.84], [15, '223344', datetime.date(2023, 9, 25), 850000, datetime.date(2024, 12, 16), 52377.5, 14885.43, 37492.07, 400314.77], [16, '223344', datetime.date(2023, 9, 25), 850000, datetime.date(2025, 1, 16), 52377.5, 13610.7, 38766.8, 361547.97], [17, '223344', datetime.date(2023, 9, 25), 850000, datetime.date(2025, 2, 16), 52377.5, 12292.63, 40084.87, 321463.1], [18, '223344', datetime.date(2023, 9, 25), 850000, datetime.date(2025, 3, 16), 52377.5, 10929.75, 41447.75, 280015.35], [19, '223344', datetime.date(2023, 9, 25), 850000, datetime.date(2025, 4, 16), 52377.5, 9520.52, 42856.98, 237158.37], [20, '223344', datetime.date(2023, 9, 25), 850000, datetime.date(2025, 5, 16), 52377.5, 8063.38, 44314.12, 192844.25], [21, '223344', datetime.date(2023, 9, 25), 850000, datetime.date(2025, 6, 16), 52377.5, 6556.7, 45820.8, 147023.45], [22, '223344', datetime.date(2023, 9, 25), 850000, datetime.date(2025, 7, 16), 52377.5, 4998.8, 47378.7, 99644.75], [23, '223344', datetime.date(2023, 9, 25), 850000, datetime.date(2025, 8, 16), 52377.5, 3387.92, 48989.58, 50655.17], [24, '223344', datetime.date(2023, 9, 25), 850000, datetime.date(2025, 9, 16), 52377.5, 1722.28, 50655.22, 0]]
        result = ControllerPaymentPlan.get_payment_plan()

        self.assertEqual(expected, result)

    def test_04_payment_plan_3(self):
        card_number: str = "445566"
        purchase_date: date = date.fromisoformat("2023-09-29")
        amount: float = 480000
        installments: int = 48

        payment_plan = ControllerPaymentPlan.insert_payment_plan(card_number, amount, purchase_date, installments)
        expected = [[1, '445566', datetime.date(2023, 9, 29), 480000, datetime.date(2023, 10, 5), 10000.0, 0.0, 10000.0, 470000.0], [2, '445566', datetime.date(2023, 9, 29), 480000, datetime.date(2023, 11, 5), 10000.0, 0.0, 10000.0, 460000.0], [3, '445566', datetime.date(2023, 9, 29), 480000, datetime.date(2023, 12, 5), 10000.0, 0.0, 10000.0, 450000.0], [4, '445566', datetime.date(2023, 9, 29), 480000, datetime.date(2024, 1, 5), 10000.0, 0.0, 10000.0, 440000.0], [5, '445566', datetime.date(2023, 9, 29), 480000, datetime.date(2024, 2, 5), 10000.0, 0.0, 10000.0, 430000.0], [6, '445566', datetime.date(2023, 9, 29), 480000, datetime.date(2024, 3, 5), 10000.0, 0.0, 10000.0, 420000.0], [7, '445566', datetime.date(2023, 9, 29), 480000, datetime.date(2024, 4, 5), 10000.0, 0.0, 10000.0, 410000.0], [8, '445566', datetime.date(2023, 9, 29), 480000, datetime.date(2024, 5, 5), 10000.0, 0.0, 10000.0, 400000.0], [9, '445566', datetime.date(2023, 9, 29), 480000, datetime.date(2024, 6, 5), 10000.0, 0.0, 10000.0, 390000.0], [10, '445566', datetime.date(2023, 9, 29), 480000, datetime.date(2024, 7, 5), 10000.0, 0.0, 10000.0, 380000.0], [11, '445566', datetime.date(2023, 9, 29), 480000, datetime.date(2024, 8, 5), 10000.0, 0.0, 10000.0, 370000.0], [12, '445566', datetime.date(2023, 9, 29), 480000, datetime.date(2024, 9, 5), 10000.0, 0.0, 10000.0, 360000.0], [13, '445566', datetime.date(2023, 9, 29), 480000, datetime.date(2024, 10, 5), 10000.0, 0.0, 10000.0, 350000.0], [14, '445566', datetime.date(2023, 9, 29), 480000, datetime.date(2024, 11, 5), 10000.0, 0.0, 10000.0, 340000.0], [15, '445566', datetime.date(2023, 9, 29), 480000, datetime.date(2024, 12, 5), 10000.0, 0.0, 10000.0, 330000.0], [16, '445566', datetime.date(2023, 9, 29), 480000, datetime.date(2025, 1, 5), 10000.0, 0.0, 10000.0, 320000.0], [17, '445566', datetime.date(2023, 9, 29), 480000, datetime.date(2025, 2, 5), 10000.0, 0.0, 10000.0, 310000.0], [18, '445566', datetime.date(2023, 9, 29), 480000, datetime.date(2025, 3, 5), 10000.0, 0.0, 10000.0, 300000.0], [19, '445566', datetime.date(2023, 9, 29), 480000, datetime.date(2025, 4, 5), 10000.0, 0.0, 10000.0, 290000.0], [20, '445566', datetime.date(2023, 9, 29), 480000, datetime.date(2025, 5, 5), 10000.0, 0.0, 10000.0, 280000.0], [21, '445566', datetime.date(2023, 9, 29), 480000, datetime.date(2025, 6, 5), 10000.0, 0.0, 10000.0, 270000.0], [22, '445566', datetime.date(2023, 9, 29), 480000, datetime.date(2025, 7, 5), 10000.0, 0.0, 10000.0, 260000.0], [23, '445566', datetime.date(2023, 9, 29), 480000, datetime.date(2025, 8, 5), 10000.0, 0.0, 10000.0, 250000.0], [24, '445566', datetime.date(2023, 9, 29), 480000, datetime.date(2025, 9, 5), 10000.0, 0.0, 10000.0, 240000.0], [25, '445566', datetime.date(2023, 9, 29), 480000, datetime.date(2025, 10, 5), 10000.0, 0.0, 10000.0, 230000.0], [26, '445566', datetime.date(2023, 9, 29), 480000, datetime.date(2025, 11, 5), 10000.0, 0.0, 10000.0, 220000.0], [27, '445566', datetime.date(2023, 9, 29), 480000, datetime.date(2025, 12, 5), 10000.0, 0.0, 10000.0, 210000.0], [28, '445566', datetime.date(2023, 9, 29), 480000, datetime.date(2026, 1, 5), 10000.0, 0.0, 10000.0, 200000.0], [29, '445566', datetime.date(2023, 9, 29), 480000, datetime.date(2026, 2, 5), 10000.0, 0.0, 10000.0, 190000.0], [30, '445566', datetime.date(2023, 9, 29), 480000, datetime.date(2026, 3, 5), 10000.0, 0.0, 10000.0, 180000.0], [31, '445566', datetime.date(2023, 9, 29), 480000, datetime.date(2026, 4, 5), 10000.0, 0.0, 10000.0, 170000.0], [32, '445566', datetime.date(2023, 9, 29), 480000, datetime.date(2026, 5, 5), 10000.0, 0.0, 10000.0, 160000.0], [33, '445566', datetime.date(2023, 9, 29), 480000, datetime.date(2026, 6, 5), 10000.0, 0.0, 10000.0, 150000.0], [34, '445566', datetime.date(2023, 9, 29), 480000, datetime.date(2026, 7, 5), 10000.0, 0.0, 10000.0, 140000.0], [35, '445566', datetime.date(2023, 9, 29), 480000, datetime.date(2026, 8, 5), 10000.0, 0.0, 10000.0, 130000.0], [36, '445566', datetime.date(2023, 9, 29), 480000, datetime.date(2026, 9, 5), 10000.0, 0.0, 10000.0, 120000.0], [37, '445566', datetime.date(2023, 9, 29), 480000, datetime.date(2026, 10, 5), 10000.0, 0.0, 10000.0, 110000.0], [38, '445566', datetime.date(2023, 9, 29), 480000, datetime.date(2026, 11, 5), 10000.0, 0.0, 10000.0, 100000.0], [39, '445566', datetime.date(2023, 9, 29), 480000, datetime.date(2026, 12, 5), 10000.0, 0.0, 10000.0, 90000.0], [40, '445566', datetime.date(2023, 9, 29), 480000, datetime.date(2027, 1, 5), 10000.0, 0.0, 10000.0, 80000.0], [41, '445566', datetime.date(2023, 9, 29), 480000, datetime.date(2027, 2, 5), 10000.0, 0.0, 10000.0, 70000.0], [42, '445566', datetime.date(2023, 9, 29), 480000, datetime.date(2027, 3, 5), 10000.0, 0.0, 10000.0, 60000.0], [43, '445566', datetime.date(2023, 9, 29), 480000, datetime.date(2027, 4, 5), 10000.0, 0.0, 10000.0, 50000.0], [44, '445566', datetime.date(2023, 9, 29), 480000, datetime.date(2027, 5, 5), 10000.0, 0.0, 10000.0, 40000.0], [45, '445566', datetime.date(2023, 9, 29), 480000, datetime.date(2027, 6, 5), 10000.0, 0.0, 10000.0, 30000.0], [46, '445566', datetime.date(2023, 9, 29), 480000, datetime.date(2027, 7, 5), 10000.0, 0.0, 10000.0, 20000.0], [47, '445566', datetime.date(2023, 9, 29), 480000, datetime.date(2027, 8, 5), 10000.0, 0.0, 10000.0, 10000.0], [48, '445566', datetime.date(2023, 9, 29), 480000, datetime.date(2027, 9, 5), 10000.0, 0.0, 10000.0, 0.0]]
        result = ControllerPaymentPlan.get_payment_plan()

        self.assertEqual(expected, result)

    def test_04_payment_plan_4(self):
        card_number: str = "445566"
        purchase_date: date = date.fromisoformat("2023-11-17")
        amount: float = 90000
        installments: int = 1

        payment_plan = ControllerPaymentPlan.insert_payment_plan(card_number, amount, purchase_date, installments)
        expected = [[1, '445566', datetime.date(2023, 11, 17), 90000, datetime.date(2023, 12, 5), 90000.0, 0.0, 90000.0, 0.0]]
        result = ControllerPaymentPlan.get_payment_plan()
        self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()
