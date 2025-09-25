from payment_mode import PaymentMode
from factory import PaymentProcessorFactory

def checkout(mode: PaymentMode, amount: float, printer=print) -> str:
    processor = PaymentProcessorFactory.get_processor(mode)
    result = processor.process(amount)
    printer(result)
    return result