c.execute('''CREATE TABLE user(
    first_name text,
    last_name text,
    address text,
    age integer,
    password text,
    fathername text,
    city text,
    zip_code integer
    )''')
print("Table created")