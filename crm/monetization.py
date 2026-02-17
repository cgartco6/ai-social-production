from payments.payfast import create_payfast_payment
from payments.cards import create_card_checkout
from payments.eft import generate_eft_instructions
from payments.payshap import generate_payshap_request

def generate_payment_options(amount, client_email):
    return {
        "payfast_url": create_payfast_payment(amount, "AI Service", client_email),
        "card_checkout_url": create_card_checkout(amount, "AI Service"),
        "eft_details": generate_eft_instructions(amount, "AI-SERVICE"),
        "payshap_details": generate_payshap_request(amount)
    }
