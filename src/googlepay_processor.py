from processor import PaymentProcessor

class GooglePayProcessor(PaymentProcessor):
    def process(self, amount: float) -> str:
        return f"Processing GooglePay payment of ${amount:.2f}"