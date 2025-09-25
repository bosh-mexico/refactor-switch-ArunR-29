from processor import PaymentProcessor

class PayPalProcessor(PaymentProcessor):
    def process(self, amount: float) -> str:
        return f"Processing PayPal payment of ${amount:.2f}"