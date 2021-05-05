import pymysql  # alt + Enter

'''
DAO역할 모듈: CRUD(DML)
정형데이터 => mysql, oracle, sqlite3(관계형 데이터베이스 관리 시스템, RDBMS)
파이썬  ================================  DB
            연결해주는 통로 : stream
            con : 통로 주소를 갖고 있음
            cursor : stream을 오가는 데이터를 가리키면서 작업을 할 수 있도록 해주는 객체

RDB
table : relation
row : 행, record(레코드), 튜플(touple, 여러개의 묶음)
column: 컬럼 ,열, 항목, field, item, attribute, property

'''


def create(datas):
    con = pymysql.connect(host = 'localhost', port= 3306, db='shop', user='root', password='1234')
    print(con.get_host_info())

    cur = con.cursor()
    print(cur)

    #sql = 'insert into movie(title) values (%s)'
    #sql = 'insert into movie(jumsu) values (%s)'
    sql = 'insert into movie(title, jumsu) values (%s, %s)'
    result = cur.executemany(sql, datas)
    print('처리 결과', result, '개')

    con.commit()
    con.close()