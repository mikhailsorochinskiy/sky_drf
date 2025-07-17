import stripe
from config.settings import SECRET_KEY_STRIPE

stripe.api_key = SECRET_KEY_STRIPE


def create_product(name):
    product = stripe.Product.create(name=name)
    return product


def create_price(price, name):
    price = stripe.Price.create(
        currency="rub",
        unit_amount=int(price * 100),
        product_data={"name": name},
    )
    return price


def create_session(price):
    session = stripe.checkout.Session.create(
        success_url="http://127.0.0.1:8000/",
        line_items=[{"price": price.id, "quantity": 1}],
        mode="payment",
    )
    return session.id, session.url
