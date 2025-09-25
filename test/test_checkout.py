import unittest
from unittest.mock import Mock
from payment_mode import PaymentMode
from checkout import checkout

class TestCheckoutWithMock(unittest.TestCase):
    def test_paypal(self):
        mock_printer = Mock()
        result = checkout(PaymentMode.PAYPAL, 100, printer=mock_printer)
        mock_printer.assert_called_with("Processing PayPal payment of $100.00")
        self.assertEqual(result, "Processing PayPal payment of $100.00")

    def test_googlepay(self):
        mock_printer = Mock()
        result = checkout(PaymentMode.GOOGLEPAY, 50.5, printer=mock_printer)
        mock_printer.assert_called_with("Processing GooglePay payment of $50.50")
        self.assertEqual(result, "Processing GooglePay payment of $50.50")

    def test_creditcard(self):
        mock_printer = Mock()
        result = checkout(PaymentMode.CREDITCARD, 75, printer=mock_printer)
        mock_printer.assert_called_with("Processing Credit Card payment of $75.00")
        self.assertEqual(result, "Processing Credit Card payment of $75.00")

    def test_unknown(self):
        mock_printer = Mock()
        result = checkout(PaymentMode.UNKNOWN, 10, printer=mock_printer)
        mock_printer.assert_called_with("Invalid payment mode selected!")
        self.assertEqual(result, "Invalid payment mode selected!")

if __name__ == "__main__":
    unittest.main()