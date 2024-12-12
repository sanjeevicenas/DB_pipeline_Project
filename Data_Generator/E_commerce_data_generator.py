import json
import random
import time
from datetime import datetime
from faker import Faker
import os

fake = Faker()

customers = []
products = []

def generate_customer():
    customer = {
        "customer_id": fake.uuid4(),
        "name": fake.name(),
        "email": fake.email(),
        "location": fake.address(),
        "age": random.randint(18, 70),
        "gender": random.choice(["Male", "Female", "Other"]),
        "account_created": fake.past_date().isoformat(),
        "last_login": fake.date_time_this_month().isoformat()
    }
    customers.append(customer["customer_id"])
    return customer

a = generate_customer()
print(a)


