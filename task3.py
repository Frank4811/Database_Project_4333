import sqlite3

def extract_and_insert_data():
    # Connect to Task 1's database
    conn_task1 = sqlite3.connect('original_db.db')
    cursor_task1 = conn_task1.cursor()

    # Connect to Task 2's database
    conn_task2 = sqlite3.connect('generated_db.db')
    cursor_task2 = conn_task2.cursor()

    # Extract and insert data for Musician table
    cursor_task1.execute("SELECT DISTINCT ssn, name, num, street, street_type FROM Notown_Records")
    rows = cursor_task1.fetchall()
    for row in rows:
        # Concatenate num, street, and street_type to form the address
        address = f"{row[2]} {row[3]} {row[4]}"
        cursor_task2.execute("INSERT INTO Musicians (SSN, Name, Address) VALUES (?, ?, ?)", (row[0], row[1], address))

    # Extract and insert data for Instrument table
    cursor_task1.execute("SELECT DISTINCT instrument_id, instrument_type, key FROM Notown_Records")
    rows = cursor_task1.fetchall()
    cursor_task2.executemany("INSERT INTO Instruments (ID, Name, MusicalKey) VALUES (?, ?, ?)", rows)

    # Extract and insert data for Album table
    cursor_task1.execute("SELECT DISTINCT album_id, album_name, date, album_type FROM Notown_Records")
    rows = cursor_task1.fetchall()
    cursor_task2.executemany("INSERT INTO Albums (AlbumID, Title, CopyrightDate, Format) VALUES (?, ?, ?, ?)", rows)

    # Extract and insert data for Participates table
    cursor_task1.execute("SELECT DISTINCT ssn, album_id FROM Notown_Records")
    rows = cursor_task1.fetchall()
    cursor_task2.executemany("INSERT INTO Participates (Musician_SSN, Album_AlbumID) VALUES (?, ?)", rows)

    # Extract and insert data for Uses table
    cursor_task1.execute("SELECT DISTINCT instrument_id, album_id FROM Notown_Records")
    rows = cursor_task1.fetchall()
    cursor_task2.executemany("INSERT INTO Uses (Instrument_ID, Album_AlbumID) VALUES (?, ?)", rows)

    # Commit changes and close connections
    conn_task2.commit()
    conn_task1.close()
    conn_task2.close()

if __name__ == "__main__":
    extract_and_insert_data()
