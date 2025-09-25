from payment_mode import PaymentMode
from paypal_processor import PayPalProcessor
from googlepay_processor import GooglePayProcessor
from creditcard_processor import CreditCardProcessor
from unknown_processor import UnknownProcessor
from processor import PaymentProcessor

class PaymentProcessorFactory:
    @staticmethod
    def get_processor(mode: PaymentMode) -> PaymentProcessor:
        processors = {
            PaymentMode.PAYPAL: PayPalProcessor(),
            PaymentMode.GOOGLEPAY: GooglePayProcessor(),
            PaymentMode.CREDITCARD: CreditCardProcessor(),
        }
        return processors.get(mode, UnknownProcessor())