import sqlite3

class Database:

    def __init__(self, db=None):
        self.conn = None
        self.cursor = None

        if db:
            self.open(db)


    #접속 메서드
    def open(self, db):
        try:
            self.conn = sqlite3.connect(db)
            self.cursor = self.conn.cursor()

        except sqlite3.Error as e:
            print('Database 접속 실패다옹')

    #닫기 메서드
    def close(self):
        if self.conn:
            self.conn.commit()
            self.cursor.close()
            self.conn.close()

    #with과 함께 사용했을 때 호출되는 생명 주기
    def __enter__(self):
        return self

    #with절이 끝났을 때 호출되는 생명 주기
    def __exit__(self, exc_type, exc_val, exc_tb):
        return self

    def execute_select(self, sql, parameter=None):
        if parameter is not None:
            self.cursor.execute(sql,parameter)

        else:
            self.cursor.execute(sql)

        data = list(self.cursor.fetchall())
        return data

    def execute_cud(self, sql, parameter=None):
        if parameter is not None:
            self.cursor.execute(sql,parameter)

        else:
            self.cursor.execute(sql)

        #영향 받은 레코드 개수

        return self.cursor.rowcount


