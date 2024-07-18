import mysql.connector
from faker import Faker


def generate_unique_email(fake, cursor):
  while True:
    email = fake.unique.email()
    try:
      cursor.execute("""
        INSERT INTO Users (username, email, password, first_name, last_name, phone_number, address, city, state, zip_code, country)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
      """, (fake.user_name(), email, fake.password(), fake.first_name(), fake.last_name(), 
            fake.phone_number(), fake.address(), fake.city(), fake.state(), fake.zipcode(), fake.country()))
      return email
    except mysql.connector.Error as err:
      # If there's a duplicate error, try again
      if err.errno == mysql.connector.ErrorNumber.ER_DUP_KEY:
        continue
      else:
        raise err


# Connect to the MySQL database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Salik@123",
    database="ecommerce"
)

cursor = db.cursor()
fake = Faker()

# Generate and insert 1000 users
def truncate_string(string, max_length):
  return string[:max_length]

for _ in range(1000):
  username = truncate_string(fake.user_name(), 50)
  # Call the function to generate unique email
  email = generate_unique_email(fake, cursor)
  password = truncate_string(fake.password(), 50)
  # ... rest of the user data generation

db.commit()
cursor.close()
db.close()
