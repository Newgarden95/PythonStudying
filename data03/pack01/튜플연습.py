# 튜플은 읽기 전용!!!!!
target = ('영어999','코딩마스터','ceo')
print(target[0])

# 만약 변경하고 싶은경우 list로 캐스팅하고 변경하기
target2 = list(target)
target2[0] = '일본어만점'
print(target2)
target = tuple(target2) # 다시 읽기 전용인 튜플로 변경

next = ('여행','또여행')
print(next+target) # 컬렉션 더하기
next0, next1 = next
print(next0) # next0 ~> next튜플에 들어있는 요소값