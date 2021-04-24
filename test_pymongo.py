from pymongo import MongoClient
from datetime import datetime
import re


# MongoDB 접속
def connect():
    client = MongoClient('mongodb://localhost:27017')
    return client


def test_connect():
    conn = connect()
    # print(dir(conn))
    print('데이터베이스 이름')

    for db in conn.list_database_names():
        print(db)


# 컬렉션 확인
def test_collection():
    conn = connect()
    # 사용할 데이터베이스 선택
    db = conn['mydb']

    # 컬렉션 선택
    coll = db['pymongo']
    return coll


def test_insert():
    coll = test_collection()

    # 1개 문서 삽입
    x = coll.insert_one({'name': '홍길동',
                         'address': '서울'})

    # 새로 생성된 Documentdml _id를 반환
    print(x.inserted_id)


def test_insert_many():
    coll = test_collection()

    # 여러 문서 삽입시에는 []로 문서 전달
    xs = coll.insert_many([
        {'name': '고길동', 'address': '서울', 'method': 'insert_many'},
        {'name': '장길산', 'method': 'insert_many'},
        {'name': '임꺽정', 'job': '도적'}])

    # 새로 생성된 Document _ids 반환
    print(xs.inserted_ids)
    print(len(xs.inserted_ids), "개 레코드 삽입됨")


def test_update():
    # address == 서울인 문서
    # method -> update, modified_at -> 현재 시간

    coll = test_collection()

    xs = coll.update_many({'address': '서울'}, {'$set': {
        'method': 'update', 'modified_at': datetime.now()}})

    print(xs.matched_count, '개가 매칭되었습니다.')
    print(xs.modified_count, '개가 갱신되었습니다.')


def test_select_by_filter(filter={}, projection={}):
    '''

    db.collection.find({조건}, {projection})
    프로젝션 값 1: 표시, 값 0 : 표시 안함

    '''

    coll = test_collection()
    docs = coll.find(filter, projection)

    for doc in docs:
        print(doc)


def test_delete_by_filter(filter={}):

    coll = test_collection()
    xs = coll.delete_many(filter)
    print(xs.deleted_count, '개의 레코드가 삭제')
 

if __name__ == "__main__":
    # test_connect()
    # test_insert()
    # test_insert_many()
    # test_update()
    # test_select_by_filter(projection={'name':1, 'address':1, '_id':0})
    # select * from table where column like
    # 정규식을 이용 패턴 전달
    # filter = re.compile(r'길동')
    # '''
    #     db.pymongo.find({"name":/길동/},{"name":1, "_id":0)
    # '''
    # test_select_by_filter({"name": filter}, {"name": 1, "_id": 0})

    # address가 서울인 문서 삭제
    # test_delete_by_filter({"address":"서울"})
    # db.pymongo.delete({"address":"서울})과 같은 문법

    # 전체 문서 삭제
    # db.pymongo.delete({})
    test_delete_by_filter({})

