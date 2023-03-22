import os
import psycopg2

up.uses_netloc.append("postgres")
url = up.urlparse(os.environ["DATABASE_URL"])
connection = psycopg2.connect(database=url.path[1:],
user=url.username,
password=url.password,
host=url.hostname,
port=url.port
)

cursor = connection.cursor()

results = cursor.fetchall()

connection.close()

for result in results:
    print(result)