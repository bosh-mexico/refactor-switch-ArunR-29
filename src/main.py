from payment_mode import PaymentMode
from checkout import checkout

if __name__ == "__main__":
    amount = 150.75
    checkout(PaymentMode.PAYPAL, amount)
    checkout(PaymentMode.GOOGLEPAY, amount)
    checkout(PaymentMode.CREDITCARD, amount)
    checkout(PaymentMode.UNKNOWN, amount)