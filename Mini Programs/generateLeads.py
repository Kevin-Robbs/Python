from faker import Faker
import random
from datetime import datetime, timedelta
from Python.scripts.mysql import connectToMySQL

fake = Faker()
now = datetime.now()

# Number of users
num_users = 10000

# List to hold all insert statements
insert_statements = []

for _ in range(num_users):
    first_name = fake.first_name()
    last_name = fake.last_name()
    dob = fake.date_of_birth(minimum_age=18, maximum_age=90).strftime('%Y-%m-%d')
    address1 = fake.street_address()
    state = fake.state_abbr()
    zipcode = fake.zipcode()
    country = "USA"
    product_type = random.randint(1, 4)
    inquiry_date = (now - timedelta(days=random.randint(0, 730))).strftime('%Y-%m-%d')

    # Create insert statement
    insert_statement = f"INSERT INTO leads (firstName, lastName, DOB, address1, state, zipcode, country, productType, inquiryDate) VALUES ('{first_name}', '{last_name}', '{dob}', '{address1}', '{state}', '{zipcode}', '{country}', {product_type}, '{inquiry_date}');"
    connectToMySQL('dlstore').query_db(insert_statement)
