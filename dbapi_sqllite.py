# 모듈 임포트

import sqlite3, os
from sqlite3 import Error

def create_connection(db_file):
    if not os.path.exists('./database'): # 현재 디렉터리에 아래 파일이 없을 겨우
        os.makedirs('./database')

    # 접속
    try:
        conn = sqlite3.connect(db_file) # Connection 객체 리턴
        print(sqlite3.version)

    except Error as e:
        print(e, type(e))
        return None # 접속 실패시 None을 리턴한다

    return conn


def test_connection(db_file):
    conn = create_connection(db_file)
    print(type(conn))
    conn.close()

def test_create_table(db_file):
    #접속
    conn = create_connection(db_file)

    #커서 획득
    cursor = conn.cursor()

    #sql 작성
    ddl = '''
        create table if not exists
        customer (id integer primary key autoincrement,
        name varchar(20),
        category integer,
        region varchar(10))
    '''
    #sql 실행
    cursor.execute(ddl)

    #접속 해제
    conn.close()

# 파라미터 이용 insert
def test_insert_data(db_file,name,category, region):
    conn = create_connection(db_file)
    cursor = conn.cursor()

    #익명 파라미터 바인딩
    sql = '''
        insert into customer(name, category, region)
        values(?,?,?)
    '''

    res = conn.execute(sql, (name, category, region))

    # insert, update, delete -> 영향 받은 레코드의 수 rowcount로 반환된다

    print("{}개의 레코드가 영향을 받음".format(res.rowcount))
    conn.commit()
    conn.close()




if __name__=="__main__":
    db_file = './database/mysqlite.db'
    # test_connection(db_file)
    test_create_table(db_file)
