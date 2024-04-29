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

    country_name = input("Enter Country name to find: ")

    cur.execute('''SELECT c.country_id
                   FROM countries c
                   WHERE c.country_name = %s''', (country_name,))
    country_id_row = cur.fetchone()

    if not country_id_row:
        print("Country not found.")
    else:
        country_id = country_id_row[0]

        cur.execute('''SELECT l.location_id, l.street_address, l.city, l.state_province, l.postal_code
                       FROM locations l
                       WHERE l.country_id = %s''', (country_id,))
        rows = cur.fetchall()

        if not rows:
            print("No locations found for the country:", country_name)
        else:
            print("Locations for", country_name)
            for row in rows:
                print("Location ID:", row[0])
                print("Street Address:", row[1])
                print("City:", row[2])
                print("State/Province:", row[3])
                print("Postal Code:", row[4])
                print()

except mysql.connector.Error as err:
    print("MySQL Error:", err)

finally:
    # Close cursor and connection
    if 'cur' in locals() and cur is not None:
        cur.close()
    if 'conn' in locals() and conn is not None:
        conn.close()
