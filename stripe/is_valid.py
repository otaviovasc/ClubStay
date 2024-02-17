import random
import stripe
import pandas as pd

# API keys

pub_key = "pk_test_51OkU9VGMdHo5Se5ncZOBddSt9b6rrKVnjYxQDFM4KeGNvZqEQH9oQyhiwZb1nHevn0h7ViTKWzAkyKvwhnSzNuNc00MvcGHn79"
sec_key = "sk_test_51OkU9VGMdHo5Se5nkdzsG1GttjWCkvrAWEdvIi3Yz3pnTa89SeohoTQn8lF54XLHGmPILtSxokZTCr9wNrpUC9kw007mbNBDXA"


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
        stripe.PaymentMethod.attach(
            payment_method_id,
            customer=customer_id,
        )
    except stripe.error.StripeError as e:
        print(f"Error attaching payment method: {e}")
        return None

    # Set the attached payment method as the default for the customer
    try:
        customer = stripe.Customer.modify(
            customer_id,
            invoice_settings={'default_payment_method': payment_method_id},
        )
        print(f"Default payment method for customer {customer_id} has been updated.")
        return customer.id
    except stripe.error.StripeError as e:
        print(f"Error setting default payment method: {e}")
        return None

# check if credit card is valid

def is_valid(payment_id):
    payment_method = stripe.PaymentMethod.retrieve(payment_id)
    cvc = payment_method.card.checks.cvc_check
    
    if len(cvc) > 3 or len(cvc) < 3 or cvc == None:
        return False
    elif cvc == "pass":
        return True

# list all users in the database

def list_users(pm_id):
    
    max = len(stripe.Customer.list(limit=100000))

    users = stripe.Customer.list(limit=max)
    users = users.data

    def get_default_payment_method(customer_id):
        customer = stripe.Customer.retrieve(customer_id)
        default_payment_method_id = customer.invoice_settings.default_payment_method
        return default_payment_method_id

    
    users_li = []

    for user in users:
        
        user = {
            "id": user.id,
            "name": user.name,
            "email": user.email,
            "payment_method": user.invoice_settings.default_payment_method,
            "valid": is_valid(pm_id)
        }
       
        users_li.append(user)
    
    return users_li


# create random credit card object

def create_df(users_li):
    
    df = pd.DataFrame(users_li)
    # sort dataframe by valid column where valid is False
    df = df.sort_values(by="valid", ascending=False)
    print(df)
    return df

def main():

    
    card = create_card()
    stripe.api_key  = pub_key
    token_id = create_token(card)
    pm = create_payment_method_from_token(token_id)
    pm_id = pm.id
    stripe.api_key = sec_key
    customer = create_customer("John", "Doe", "", pm_id)
    customer_id = customer.id
    attach_and_set_default_payment_method(customer_id, pm_id)
    valid = is_valid(pm_id)
    users_li = list_users(pm_id)
    df = create_df(users_li)
    
    
    return df

# run the main function seamlessly
if __name__ == "__main__":
    main()
    
