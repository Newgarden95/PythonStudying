from 클래스만들기.사람모듈 import *
import 클래스만들기.매일 as my

class WomanDay(Person, my.Day): # 현재 Person, my.Day 다중상속받음
#  파이썬: 클래스간 다중 상속이 가능하다.
#  자바: 클래스간 단일상속만 가능하다.

    def __init__(self, doing, hour, place):
        my.Day.__init__(self,doing,hour,place) #WomanDay에서 받아온걸 my.Day로 보내서 초기화 why? 저거에 해당하는 멤버변수는 Day에 있으니까

    def free(self):
        print("쉬다!")

    def __str__(self):
        return self.doing + ',' + str(self.hour)+','+self.place
if __name__ == '__main__':
    woman_day1 = WomanDay('진짜 놀기',20,'마포구')
    woman_day1.free()
    woman_day1.eat()

    print(woman_day1)
