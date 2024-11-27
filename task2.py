import sqlite3

def create_database():
    # Connect to the database
    conn = sqlite3.connect('generated_db.db')
    cursor = conn.cursor()

    # Create tables
    cursor.execute('''CREATE TABLE IF NOT EXISTS Musicians (
                        SSN VARCHAR PRIMARY KEY,
                        Name VARCHAR,
                        Address VARCHAR
                    )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS Instruments (
                        ID INT PRIMARY KEY,
                        Name VARCHAR,
                        MusicalKey VARCHAR
                    )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS Albums (
                        AlbumID INT PRIMARY KEY,
                        Title VARCHAR,
                        CopyrightDate DATE,
                        Format VARCHAR
                    )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS Participates (
                        Musician_SSN VARCHAR,
                        Album_AlbumID INT,
                        PRIMARY KEY (Musician_SSN, Album_AlbumID),
                        FOREIGN KEY (Musician_SSN) REFERENCES Musicians (SSN),
                        FOREIGN KEY (Album_AlbumID) REFERENCES Albums (AlbumID)
                    )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS Uses (
                        Instrument_ID INT,
                        Album_AlbumID INT,
                        PRIMARY KEY (Instrument_ID, Album_AlbumID),
                        FOREIGN KEY (Instrument_ID) REFERENCES Instruments (ID),
                        FOREIGN KEY (Album_AlbumID) REFERENCES Albums (AlbumID)
                    )''')

    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_database()