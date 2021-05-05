import DB연결.mysql_bbs.bbs_dao as db

print("전체데이터 검색처리 부분입니다")

record = db.read_all()

for item in record:
    print("검색 결과:",item)