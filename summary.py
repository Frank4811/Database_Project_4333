import sqlite3

def get_summary_report():
    # Connect to the database
    conn = sqlite3.connect('generated_db.db')
    cursor = conn.cursor()

    # Query to get total number of musicians and list of musicians (name and ssn)
    cursor.execute("SELECT COUNT(*), Name, SSN FROM Musicians GROUP BY SSN")
    musicians_result = cursor.fetchall()
    total_musicians = len(musicians_result)
    musicians_list = [(name, ssn) for count, name, ssn in musicians_result]

    # Query to get total number of albums and list of albums (name and album id)
    cursor.execute("SELECT COUNT(*), Title, AlbumID FROM Albums GROUP BY AlbumID")
    albums_result = cursor.fetchall()
    total_albums = len(albums_result)
    albums_list = [(title, album_id) for count, title, album_id in albums_result]

    # Query to get total number of instruments and list of instruments (name, key, and id)
    cursor.execute("SELECT COUNT(*), Name, MusicalKey, ID FROM Instruments GROUP BY ID")
    instruments_result = cursor.fetchall()
    total_instruments = len(instruments_result)
    instruments_list = [(name, key, id) for count, name, key, id in instruments_result]

    # Query to get table of musicians and the total number of albums written by them
    cursor.execute("SELECT Name, COUNT(*) AS TotalAlbums FROM Musicians JOIN Participates ON Musicians.SSN = Participates.Musician_SSN GROUP BY Musicians.SSN")
    musician_albums_result = cursor.fetchall()

    # Close the connection
    conn.close()

    # Format the summary report
    summary_report = {
        "TotalMusicians": total_musicians,
        "MusiciansList": musicians_list,
        "TotalAlbums": total_albums,
        "AlbumsList": albums_list,
        "TotalInstruments": total_instruments,
        "InstrumentsList": instruments_list,
        "MusicianAlbums": musician_albums_result
    }

    return summary_report

if __name__ == "__main__":
    summary = get_summary_report()
    print(summary)
