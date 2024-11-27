import csv
import sqlite3

def create_database():
    # Connect to the database
    conn = sqlite3.connect('original_db.db')
    cursor = conn.cursor()

    # Create a single table
    cursor.execute('''CREATE TABLE IF NOT EXISTS Notown_Records (
                        num INT,
                        street VARCHAR,
                        street_type VARCHAR,
                        name VARCHAR,
                        ssn VARCHAR PRIMARY KEY,
                        album_id INT,
                        album_name VARCHAR,
                        date INT,
                        album_type VARCHAR,
                        instrument_id INT,
                        instrument_type VARCHAR,
                        key VARCHAR
                    )''')

    conn.commit()
    conn.close()

def import_data():
    # Connect to the database
    conn = sqlite3.connect('original_db.db')
    cursor = conn.cursor()

    # Read CSV file and insert data into the single table
    with open('no_town.csv', 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvreader)  # Skip header
        for row in csvreader:
            cursor.execute("INSERT OR IGNORE INTO Notown_Records VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", row)

    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_database()
    import_data()
