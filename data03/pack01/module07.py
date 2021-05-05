# 반복문 while
'''
조건에 맞으면 여러번 반복(한정반복)
조건에 맞는동안 계속 반복(무한반복)
시작값, 증감값, 종료값
'''
start = 1
end = 10
plus = 1

while start <= end:
    print(start)
    start+=plus
# 반복문 for
for _ in range(start, end+1, plus):
    print('내가 반복됨')

for x in range(1, 11, 1):
    print(x)

sum2 = 0
for x in range(1,11):
    sum2+=x
print(sum2)

r = [1,2,3,4,5,6,7,8,9,10]
for x2 in r:
    print(x2)
    
r2 = [100,200,300,400,500]
for x3 in  r2:
    print("하당값>> ", x3)
    if x3 == 300:
        print('300을 찾음')
        break