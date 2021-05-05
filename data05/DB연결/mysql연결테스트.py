'''
자바와 같이 db커넥션을 할 라이브러리를 설치해야함
'''

import pymysql # alt+Enter => install => 설치해줌

def create(id, pw, name, tel):
    con = pymysql.connect(host='localhost', port=3306, db='shop', user='root', password='1234')  # 연결된 주소값을 반환
    print(con.get_host_info())

    cur = con.cursor()  # rs.next처럼 레코드 하나씩 내려가면서 확인하는것 : cursor()
    print(cur)

    sql = 'insert into member values("'+id+'","'+pw+'","'+name+'","'+tel+'")'
    result = cur.execute(sql)  # sql 실행하기
    print(result)  # insert 된거 갯수
    con.commit()  # AutoCommit설정 안됨 ~> 직접 수동으로 해야함

def delete(id):
    con = pymysql.connect(host='localhost', port=3306, db='shop', user='root', password='1234')  # 연결된 주소값을 반환
    print(con.get_host_info())

    cur = con.cursor()  # rs.next처럼 레코드 하나씩 내려가면서 확인하는것 : cursor()
    print(cur)

    sql = 'delete from member where id = "'+id+'" ' # 'delete from member where id = "' : 문자열 + id(문자열) + ' "(문자) '
    result = cur.execute(sql)  # sql 실행하기
    print(result)  # insert 된거 갯수
    con.commit()  # AutoCommit설정 안됨 ~> 직접 수동으로 해야함

'''
디비연결과정!!!
'''
'''
con = pymysql.connect(host = 'localhost', port = 3306, db = 'shop', user = 'root', password= '1234') # 연결된 주소값을 반환
print(con.get_host_info())

cur = con.cursor() # rs.next처럼 레코드 하나씩 내려가면서 확인하는것 : cursor()
print(cur)

sql = 'insert into member values("python2","python1","python","python")'
result = cur.execute(sql) # sql 실행하기
print(result) #insert 된거 갯수
con.commit() # AutoCommit설정 안됨 ~> 직접 수동으로 해야함
con.close()
'''