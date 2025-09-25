from processor import PaymentProcessor

class UnknownProcessor(PaymentProcessor):
    def process(self, amount: float) -> str:
        return "Invalid payment mode selected!"