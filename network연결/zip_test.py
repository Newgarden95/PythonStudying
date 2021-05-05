names = ['홍길동','김길동','박길동']
ages = [100,200,300]

total = list(zip(names, ages)) # 타입은 무조건 리스트로 ~> 왜? 얼마나 많은 데이터가 들어올지 모르기 때문에 동적할당을 위해

print(total)
print(tuple(total))
print(len(total))