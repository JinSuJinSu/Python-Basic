import sqlite3

class Database:

    def __init__(self, db=None):
        self.conn = None
        self.curosr = None

        if db:
            self.open(db)


    #접속 메서드
    def open(self, db):
        try:
            self.conn = sqlite3.connect(db)
            self.curosr = self.conn.cursor()

        except sqlite3.Error as e:
            print('Database 접속 실패다옹')

    #닫기 메서드
    def close(self):
        if self.conn:
            self.conn.commit()
            self.curosr.close()
            self.conn.close()