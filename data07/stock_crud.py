import pymysql

def create(datas):
    '''
    #1. mysql과 연결
    con = pymysql.connect(host='localhost', port=3306, db='shop', user='root', password='1234')  # 연결된 주소값을 반환
    print(con.get_host_info())

    #2. 스트림(stream)안의 데이터를 다룰 수 있는 부품인 cursor를 흭득
    cur = con.cursor()  # rs.next처럼 레코드 하나씩 내려가면서 확인하는것 : cursor()
    print(cur)

    #3. sql문을 만들어 전송
    sql = 'insert into stock(name, cost) values (%s, %s)'
    result = cur.executemany(sql, datas)  # sql 실행하기
    print('처리결과', result + '개')  # insert 된거 갯수

    #4. Auto-commit이 안된다. 수동으로 반영시켜야 한다.
    con.commit()  # AutoCommit설정 안됨 ~> 직접 수동으로 해야함
    con.close()'''

    con = pymysql.connect(host='localhost', port=3306, db='shop', user='root', password='1234')
    print(con.get_host_info())

    cur = con.cursor()
    print(cur)

    # sql = 'insert into movie(title) values (%s)'
    # sql = 'insert into movie(jumsu) values (%s)'
    sql = 'insert into stock(name, cost) values (%s, %s)'
    result = cur.executemany(sql, datas)
    print('처리 결과', result, '개')

    con.commit()
    con.close()