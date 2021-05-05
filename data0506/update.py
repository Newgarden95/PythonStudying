import DB연결.mysql_bbs.bbs_dao as db

print("변경처리 부분입니다")
id = input("아이디를 입력하세요>>")
title = input("변경할 제목을 입력하세요>>")
content = input("변경할 내용을 입력하세요>>")

VO = (title, content, id)

db.update(VO)