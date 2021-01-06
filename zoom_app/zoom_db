import sqlite3


class ZoomDataBase:

    def __init__(self):
        """ Create the table """
        conn = sqlite3.connect('db.zoom')
        c = conn.cursor()
        try:
            c.execute('CREATE TABLE meetings (meeting_id INTEGER NOT NULL UNIQUE, participants INTEGER)')
            print("create table")
        except Exception as err:
            if str(err) == 'table meetings already exists':
                c.execute('delete from meetings;')
                print('table delete')
                conn.commit()
        conn.close()

    @staticmethod
    def delete_row(meeting_id):
        conn = sqlite3.connect('db.zoom')
        c = conn.cursor()
        c.execute('DELETE FROM meetings WHERE meeting_id=?', [meeting_id])
        conn.commit()
        conn.close()

    @staticmethod
    def add_rows(data):
        if not data:
            return
        meetings_data = list(map(lambda meeting: (meeting['id'], meeting['participants']), data))
        conn = sqlite3.connect('db.zoom')
        c = conn.cursor()
        try:
            c.executemany('INSERT INTO meetings VALUES (?,?)', meetings_data)
        except Exception as err:
            if 'UNIQUE' in str(err):
                pass
        conn.commit()
        conn.close()

    @staticmethod
    def get_all():
        conn = sqlite3.connect('db.zoom')
        c = conn.cursor()
        rows = list(c.execute('SELECT * FROM meetings'))
        conn.close()
        rows = list(map(lambda row: {'id': row[0], 'participants': row[1]}, rows))
        return rows
