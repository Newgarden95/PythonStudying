#for문을 사용해보세여

#1번
for i in range(20):
    print(i, end=' ')
print('\n')
#2번
for i in range(1, 101):
    print(i, end=' ')
print('\n')
#3번
for i in range(0,201):
    print(i, end = ' ')
print('\n')
#4번
for i in range(1, 101, 2):
    print(i, end =' ')
print('\n')
#5번
for i in range(100, 501, 5):
    print(i, end=' ')
print('\n')

#6번
sum = 0
for i in range(100, 501, 10):
    sum +=i
print("1~500까지 10씩 증가한 값 다 더하기:",sum)
print('\n')

#7번
a = 1
for i in range(3, 201, 8):
    a*=i
print("3~200까지 8씩 증가한 값 다 곱하기:",a)
print('\n')
#8번
food = ['감자','고구마','양파']
for food in food:
    print(food+"짱!")

food = ['감자','고구마','양파']
print('\n')
for i in food:
    print(i+"짱!", end = ' ')
print('\n')
#9번
#양파 스프 빼기
food2 = "감자 고구마 양파 스프 국수 라면"
food3 = food2.split( )
for i in food3:
    if( i != '양파' and i != '스프'):
        print(i+"맛있어!", end = " ")