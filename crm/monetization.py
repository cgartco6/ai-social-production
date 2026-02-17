from payments.payfast import create_payfast_payment
from payments.cards import create_card_checkout
from payments.eft import generate_eft_instructions
from payments.payshap import generate_payshap_request

import stripe
from core.config import STRIPE_SECRET_KEY

stripe.api_key = STRIPE_SECRET_KEY

def create_payment_link(amount_zar, description):
    product = stripe.Product.create(name=description)
    price = stripe.Price.create(
        unit_amount=int(amount_zar * 100),
        currency="zar",
        product=product.id,
    )
    link = stripe.PaymentLink.create(
        line_items=[{"price": price.id, "quantity": 1}]
    )
    return link.url

def generate_payment_options(amount, client_email):
    return {
        "payfast_url": create_payfast_payment(amount, "AI Service", client_email),
        "card_checkout_url": create_card_checkout(amount, "AI Service"),
        "eft_details": generate_eft_instructions(amount, "AI-SERVICE"),
        "payshap_details": generate_payshap_request(amount)
    }

