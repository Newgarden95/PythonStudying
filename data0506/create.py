import DB연결.mysql_bbs.bbs_dao as db

print("입력처리 부분입니다")
id = input("아이디를 입력하세요>>")
title = input("제목을 입력하세요>>")
content = input("내용을 입력하세요>>")
writer = input("작성자를 입력하세요>>")

VO = (id, title, content, writer)

db.create(VO)