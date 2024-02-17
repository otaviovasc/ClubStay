import random
import stripe
import pandas as pd

# API keys

pub_key = "pk_test_51OkU9VGMdHo5Se5ncZOBddSt9b6rrKVnjYxQDFM4KeGNvZqEQH9oQyhiwZb1nHevn0h7ViTKWzAkyKvwhnSzNuNc00MvcGHn79"
sec_key = "sk_test_51OkU9VGMdHo5Se5nkdzsG1GttjWCkvrAWEdvIi3Yz3pnTa89SeohoTQn8lF54XLHGmPILtSxokZTCr9wNrpUC9kw007mbNBDXA"


# create random credit card object
def create_card():
    
    card = {
        "number": "4242424242424242",
        "exp_month": random.randint(1, 12),
        "exp_year": random.randint(2025, 2045),
        "cvc": random.randint(100, 1400),
    }
    
    number = card["number"]
    exp_month = card["exp_month"]
    exp_year = card["exp_year"]
    cvc = card["cvc"]
    
    return card


stripe.api_key = pub_key

# create tokens from fake credit cards to pass create payment method id
def create_token(card):
    token = stripe.Token.create(
        card={
            "number": card["number"],
            "exp_month": card["exp_month"],
            "exp_year": card["exp_year"],
            "cvc": card["cvc"],
        },
    )
    return token.id

# create payment method object

def create_payment_method_from_token(token_id):
    """
    Creates a payment method from a given token ID.

    :param token_id: The ID of the token created for a card.
    :return: A Stripe payment method object.
    """
    payment_method = stripe.PaymentMethod.create(
        type="card",
        card={"token": token_id},
    )
    return payment_method
    
    
stripe.api_key  = sec_key
    
# create customer object

def create_customer(name, surname, email, payment_method):
    
    # create fullname
    name = name + " " + surname
    
    user = stripe.Customer.create(
        name=name,
        email=email,
        payment_method=payment_method,
    )
    
    return user

# attached payment method to user and set it as default invoice settings

def attach_and_set_default_payment_method(customer_id, payment_method_id):
    # Attach the payment method to the customer
    try:
        attached_pm = stripe.PaymentMethod.attach(
            payment_method_id,
            customer=customer_id,
        )
    except stripe.error.StripeError as e:
        print(f"Error attaching payment method: {e}")
        return None, None

    # Set the attached payment method as the default for the customer
    try:
        customer = stripe.Customer.modify(
            customer_id,
            invoice_settings={'default_payment_method': payment_method_id},
        )
        print(f"Default payment method for customer {customer_id} has been updated.")
        
        return attached_pm, customer
    except stripe.error.StripeError as e:
        print(f"Error setting default payment method: {e}")
        return None, None
# check if credit card is valid

def is_valid(pm):
    try:
        cvc_check = pm.card.checks.cvc_check

        if cvc_check == "pass":
            return True
        else:
            return False
    except stripe.error.StripeError as e:
        print(f"Stripe API error: {e}")
        return False

# create payment intent 

def create_and_confirm_payment_intent(amount_cents, customer_id, payment_method_id):

    try:
        # Create a PaymentIntent with the specified amount and currency
        payment_intent = stripe.PaymentIntent.create(
            amount=amount_cents,
            currency='brl',
            customer=customer_id,
            payment_method=payment_method_id,
            off_session=True,  # Indicates that the customer is not present
            confirm=True,  # Automatically confirm the payment intent
            use_stripe_sdk=True,  # Optimize for using Stripe’s SDKs
        )
        return payment_intent  # Return the status of the payment intent
    except stripe.error.StripeError as e:
        print(f"Stripe error: {e}")
        return None

# list all users in the database

def list_customers():

    max = len(stripe.Customer.list(limit=100000))
    customers = stripe.Customer.list(limit=max)
    customers = customers.data

    return customers

# get pm_id

def get_pm_id(customer_id):
    customer = stripe.Customer.retrieve(customer_id)
    pm_id = customer.invoice_settings.default_payment_method
    return pm_id


def create_df(customers):

    data = []
    
    for c in customers:

        pm_id = get_pm_id(c.id)
        pm = stripe.PaymentMethodConfiguration.retrieve(pm_id)

    
        user = {
            "id": c.id,
            "name": c.name,
            "email": c.email,
            "payment_method": c.invoice_settings.default_payment_method,
            "valid": is_valid(pm),
            "status": create_and_confirm_payment_intent(50, c.id, pm_id).status
        }

        data.append(user)

    df = pd.DataFrame(data)
    
    df = df.sort_values(by="status", ascending=False)

    return df

def main():

    
    card = create_card()
    stripe.api_key  = pub_key
    token_id = create_token(card)
    pm = create_payment_method_from_token(token_id)
    pm_id = pm.id
    stripe.api_key = sec_key
    customer = create_customer("Regis", "E2E", "", pm_id)
    customer_id = customer.id
    pm, customer = attach_and_set_default_payment_method(customer_id, pm_id)
    valid = is_valid(pm)

    customers = list_customers()
    
    df = create_df(customers)
    
    return df


# run the main function seamlessly
if __name__ == "__main__":
    main()
    
