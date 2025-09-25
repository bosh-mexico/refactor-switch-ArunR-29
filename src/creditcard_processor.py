from processor import PaymentProcessor

class CreditCardProcessor(PaymentProcessor):
    def process(self, amount: float) -> str:
        return f"Processing Credit Card payment of ${amount:.2f}"