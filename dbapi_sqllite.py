# 모듈 임포트

import sqlite3, os
from sqlite3 import Error



def create_connection(db_file):
    if not os.path.exists('./database'):  # 현재 디렉터리에 아래 파일이 없을 겨우
        os.makedirs('./database')

    # 접속
    try:
        conn = sqlite3.connect(db_file)  # Connection 객체 리턴
        print(sqlite3.version)

    except Error as e:
        print(e, type(e))
        return None  # 접속 실패시 None을 리턴한다

    return conn


def test_connection(db_file):
    conn = create_connection(db_file)
    print(type(conn))
    conn.close()


def test_create_table(db_file):
    # 접속
    conn = create_connection(db_file)

    # 커서 획득
    cursor = conn.cursor()

    # sql 작성
    ddl = '''
        create table if not exists
        customer (id integer primary key autoincrement,
        name varchar(20),
        category integer,
        region varchar(10))
    '''
    # sql 실행
    cursor.execute(ddl)

    # 접속 해제
    conn.close()


# 파라미터 이용 insert
def test_insert_data(db_file, name, category, region):
    conn = create_connection(db_file)
    cursor = conn.cursor()

    # 익명 파라미터 바인딩
    sql = '''
        insert into customer(name, category, region)
        values(?,?,?)
    '''

    res = conn.execute(sql, (name, category, region))

    # insert, update, delete -> 영향 받은 레코드의 수 rowcount로 반환된다

    print("{}개의 레코드가 영향을 받음".format(res.rowcount))
    conn.commit()
    conn.close()


def test_delete_all(db_file):
    conn = create_connection(db_file)
    sql = '''
        delete from customer
    '''
    res = conn.execute(sql)
    print("{}개의 레코드가 삭제되었습니다.".format(res.rowcount))
    conn.commit()
    conn.close()


def test_insert_bulk_data(db_file):
    # 테스트 여러개 insert
    test_delete_all(db_file)
    test_insert_data(db_file, '둘리', 1, '부천')
    test_insert_data(db_file, '고길동', 2, '부천')
    test_insert_data(db_file, '남승균', 2, '서울')
    test_insert_data(db_file, '홍길동', 1, '서울')
    test_insert_data(db_file, '이수민', 2, '부산')


def test_select_data(db_file):
    with create_connection(db_file) as conn:  # with 문이 종료되면 자동으로 close
        sql = 'select * from customer'
        cursor = conn.execute(sql)

        # print(type(cursor))

        # 결과 처리하기
        print(cursor.fetchone())  # 1개 레코드 불러오기
        print(cursor.fetchmany(2))  # 현제 커서 위치에서 다중 레코드 불러오기
        print(cursor.fetchall())  # 현재 커서 위치에서 전체 레코드 불러오기


def test_search_data(db_file):
    conn = create_connection(db_file)

    # 명명된 플레이스 홀더
    # 플레이스 홀더에 :키로 명명
    # 데이터는 dict로 전달

    sql = '''
        select name, category, region from customer
        where region=:region or category=:category
    '''

    cursor = conn.execute(sql, {
        'region': '부천',
        'category': 2
    })

    for customer in cursor.fetchall():
        print(customer)


# 사용자 정의 클래스 import
from mysqlite import *

def test_mysqlite_class(db_file):
    # 새 객체 생성
    mydb = Database(db_file)
    sql = """SELECT * FROM customer 
    WHERE region=:region
    """
    res = mydb.execute_select(sql, {
        "region": "서울"
    })

    for customer in res:
        print(customer)

if __name__ == "__main__":
    db_file = './database/mysqlite.db'
    # test_connection(db_file)
    # test_create_table(db_file)
    # test_insert_data(db_file,2,'둘리','부천')
    # test_insert_bulk_data(db_file)
    # test_select_data(db_file)
    # test_search_data(db_file)
    test_mysqlite_class(db_file)
