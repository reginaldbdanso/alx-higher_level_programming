#!/usr/bin/python3
import MySQLdb
import sys

def list_states(username, password, database_name):
    # Connect to the MySQL server
    try:
        db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database_name)
        cursor = db.cursor()

        # Execute the SQL query to fetch states in ascending order by states.id
        cursor.execute("SELECT * FROM states ORDER BY id ASC")

        # Fetch all the rows
        rows = cursor.fetchall()

        # Display the results
        for row in rows:
            print(row)

        # Close the cursor and database connection
        cursor.close()
        db.close()

    except MySQLdb.Error as e:
        print("Error connecting to MySQL:", e)
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script.py <username> <password> <database_name>")
    else:
        username, password, database_name = sys.argv[1], sys.argv[2], sys.argv[3]
        list_states(username, password, database_name)
