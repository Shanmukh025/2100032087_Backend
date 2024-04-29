import mysql.connector

try:
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="vachi_46",
        database="safertech",
        auth_plugin='mysql_native_password'
    )

    cur = conn.cursor()

    cur.execute('''CREATE TABLE IF NOT EXISTS locations (
                    location_id INT PRIMARY KEY,
                    street_address VARCHAR(255),
                    city VARCHAR(255),
                    state_province VARCHAR(255),
                    postal_code VARCHAR(10),
                    country_id VARCHAR(2)
                )''')

    cur.execute('''CREATE TABLE IF NOT EXISTS countries (
                    country_id VARCHAR(2) PRIMARY KEY,
                    country_name VARCHAR(255),
                    region_id VARCHAR(255)
                )''')

    print("Enter Location table data:")
    print()

    location_id = int(input("Enter location ID: "))
    street_address = input("Enter street address: ")
    postal_code = input("Enter postal code: ")
    city = input("Enter city: ")
    state_province = input("Enter state/province: ")
    country_id = input("Enter country code: ")

    print()

    sql = "INSERT INTO locations (location_id, street_address, city, state_province, postal_code, country_id) VALUES (%s, %s, %s, %s, %s, %s)"
    val = (location_id, street_address, city, state_province, postal_code, country_id)
    cur.execute(sql, val)

    print("Enter Countries table data:")
    print()

    country_id = input("Enter country ID:")
    country_name = input("Enter country Name:")
    region_id = input("Enter region id:")

    sql = "INSERT INTO countries (country_id, country_name,region_id) VALUES (%s, %s, %s)"
    val = (country_id, country_name, region_id)
    cur.execute(sql, val)

    conn.commit()

    print("Data inserted successfully!")
    print()

    print("==============================================Join Condition======================================================")

    country_name = input("Enter country name to apply join condition on that country name: ")

    cur.execute('''SELECT l.location_id, l.street_address, l.city, l.state_province, l.postal_code, c.country_name, c.country_id
                   FROM locations l
                   JOIN countries c ON l.country_id = c.country_id
                   WHERE c.country_name = %s ''', (country_name,))
    rows = cur.fetchall()

    # Display results
    for row in rows:
        print(row)

except mysql.connector.Error as err:
    print("MySQL Error:", err)

finally:
    if 'cur' in locals() and cur is not None:
        cur.close()
    if 'conn' in locals() and conn is not None:
        conn.close()
