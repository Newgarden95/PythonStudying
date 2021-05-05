import DB연결.mysql_bbs.bbs_dao as db

print("삭제처리 부분입니다")
id = input("삭제할 아이디를 입력하세요>>")

db.delete(id)