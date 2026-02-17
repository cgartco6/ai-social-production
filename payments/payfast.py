import hashlib
import urllib.parse
from core.config import (
    PAYFAST_MERCHANT_ID,
    PAYFAST_MERCHANT_KEY,
    PAYFAST_PASSPHRASE,
    PAYFAST_RETURN_URL,
    PAYFAST_CANCEL_URL,
    PAYFAST_NOTIFY_URL
)

PAYFAST_URL = "https://www.payfast.co.za/eng/process"

def generate_signature(data):
    encoded = urllib.parse.urlencode(data)
    string = f"{encoded}&passphrase={PAYFAST_PASSPHRASE}"
    return hashlib.md5(string.encode()).hexdigest()

def create_payfast_payment(amount, item_name, email):
    data = {
        "merchant_id": PAYFAST_MERCHANT_ID,
        "merchant_key": PAYFAST_MERCHANT_KEY,
        "return_url": PAYFAST_RETURN_URL,
        "cancel_url": PAYFAST_CANCEL_URL,
        "notify_url": PAYFAST_NOTIFY_URL,
        "amount": f"{amount:.2f}",
        "item_name": item_name,
        "email_address": email,
    }
    data["signature"] = generate_signature(data)
    return f"{PAYFAST_URL}?{urllib.parse.urlencode(data)}"
