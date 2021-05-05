from builtins import list

list1 = '123,456'
list = ['123,456', '567,890']

l = list1.replace(',', '') #replace : 컴마(,)를 공백('')으로 대체해준다

def comma(data):
    return data.replace(',','')

list2 = []

list2 = list(map(comma,list))
print(list2)
'''
def comma(list):
    return list.replace(',','')

list2 = list(map(comma,list)) #map(함수, 리스트) : 리스트에서 하나씩 추출해서 함수를 실행시켜라
print(list2)'''