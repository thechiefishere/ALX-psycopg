import psycopg2;

connection = psycopg2.connect('dbname=test')

cursor = connection.cursor()

# cursor.execute("INSERT INTO person (first_name, last_name, email, gender, date_of_birth, country_of_birth) VALUES ('Funmi', 'Toriola', 'funmi.toriola@fake.gmail', 'Female', '2000-01-20', 'Nigeria');"); 

cursor.execute("SELECT * FROM person")
result = cursor.fetchall()
print("result", result)

connection.commit()

cursor.close()
connection.close()