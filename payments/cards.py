import stripe
from core.config import STRIPE_SECRET_KEY

stripe.api_key = STRIPE_SECRET_KEY

def create_card_checkout(amount, description):
    product = stripe.Product.create(name=description)
    price = stripe.Price.create(
        unit_amount=int(amount * 100),
        currency="zar",
        product=product.id,
    )
    link = stripe.PaymentLink.create(
        line_items=[{"price": price.id, "quantity": 1}]
    )
    return link.url
