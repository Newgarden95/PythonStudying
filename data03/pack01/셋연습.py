# 중복제거!!!! set ### 순서는 상관없음!!!
friends = ['영수','철수','철수','영진','영수','길동']
print(friends)
print(len(friends))


friends_set = set(friends)
print(friends_set)
print(len(friends_set))

friends_set.add('아이유')
print(friends_set)

friends_set.update({'재석','용만'})
print(friends_set)

friends_set.clear()
print(friends_set)

term1 = {10,20,30,40}
term2 = {11,22,33,10}
result = term1 & term2 #교집합
result1 = term1.intersection(term2) #term1과 term2의 교집합
print(result)

result2 = term1 | term2
result2 = term1.union(term2) # 합집합
print(result2)

result3 = term1 - term2
result3 = term1.difference(term2) #차집합
print(result3 )

c1 = [22,99,11,23]
c2 = [44,99,66,23]
index = []
count = 0
for i in range (4):
    if( c1[i] == c2[i] ):
        index.append(i)
        count += 1
print(index)
print(count)
