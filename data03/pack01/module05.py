# 문자열 포맷팅

p = '이름: %s 나이: %d' %('홍길동',100)
print(p)

p2 = 'X = %0.3f, Y = %10.2f' %(3.1456, 555.6666)
print(p2)

###################################################
# 문자열 추출
name = '홍길동'
print(name[0])
print(name[1])
print(name[2])
print(name[0:2]) #0~1
print(name[0:]) #0~끝까지
print(type(name[0]))

hobby = '달리기,등산,자전거,코딩'
result = hobby.split(',')
print(result)
print(type(result))
print(result[0])

s = "이름: {0}, 나이: {1}"
sf = s.format("신화원", 27)
print(sf)
print("=============================")
s2 = "이름: {name}, 나이:{age}"
sf2 = s2.format(name = "신화원", age = 27)
print(sf2)
print("=============================")

data = (10,20,30)
s3 = "길이: {data[0]}, 높이: {data[1]}, 면적: {data[2]}"
sf3 = s3.format(data = data)
print(sf3)
