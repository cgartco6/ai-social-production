import uuid
from core.config import PAYSHAP_PROXY_ID

def generate_payshap_request(amount):
    reference = str(uuid.uuid4())[:8]
    return {
        "proxy_id": PAYSHAP_PROXY_ID,
        "amount": f"ZAR {amount}",
        "reference": reference,
        "note": "PayShap Instant Payment"
    }
