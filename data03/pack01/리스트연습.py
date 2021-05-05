food = ['감자','양파','고구마']
food[2] = '국수'

print(food)
print('리스트의 개수',len(food))
print('요소, element의 글자수',len(food[1]))


#########################
# 리스트 형식
hobby = []
tour = list()

hobby.append('코딩')
hobby.append('등산')
hobby.append('독서')
hobby.append('글쓰기')
print(hobby)
print(len(hobby))

tour.append('제주도')
tour.append('울산')
tour.append('서울')
tour.append('강남')
print(tour)
print(len(tour))
del tour[0]
print(tour)
tour.insert(0, '신촌')
print(tour)

for x in tour:
    print(x, end=' ')
print()
for x in range(len(tour)):
    print(tour[x], end = ' ')
print()


####################################################
buy = []
wish = []
'''1. 사고 싶은것 5개를 입력받아서, 리스트에 넣으세요(for문사용) 전체 프린트

'''
for i in range(5):
   buy.append(input("사고 싶은것을 입력하세요>>"))
print(buy)

'''2. wish에 들어갈 입력을 다음과 같이 하나의 스트링으로 입력받아서 리스트에 넣어서
아래와 같이 출력되게 해보세여'''

wish_string = input("문장입력")
wish = wish_string.split(',')
for i in wish:
    print("나는 "+i+"가 되고 싶어요!")