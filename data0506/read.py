import DB연결.mysql_bbs.bbs_dao as db

print("검색처리 부분입니다")
id = input("아이디를 입력하세요>>")

record = db.read(id)
print("검색 결과: ", record)