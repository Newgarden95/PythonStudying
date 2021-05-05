print("편한 따옴표를 쓰세요")

# 파이썬은 같은 타입만 +연산가능
name = 10
print('이름은',name,'입니다')  # 를 기준으로 띄어쓰기
print('이름은'+str(name)+'입니다')  # +연산자(결합연산자) 결과는 붙여쓰김

temp = input('현재 온도는>>')  # "22.2"
print(type(temp))

temp2 = float(temp)
print(type(temp2))

if temp2>0:
    print("너무 더워요")
else:
    print("아직 안더워요")

"""
타입을 변경하는 것 : 형변환(casting, 캐스팅)
문자로 변경 : str()
정수로 변경 : int()
실수로 변경 : float()

문자
string을 의미, char를 포함하는 의미

"""
company = '메가'
print(company, end = '') # 프린트 후 마지막에 엔터 적용
print('우리 회사는', company)

# 논리
food = True
food2 = 1

if food == True:
    print("배가 부르시군요")
else:
    print("배가 고파요")