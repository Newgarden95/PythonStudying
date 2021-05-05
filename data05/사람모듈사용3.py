from 클래스만들기.사람모듈 import *

class Student(Person):

    def study(self):
        print("공부를 합니다")

    def __init__(self, name, age): #Student클래스의 생성자
        Person.__init__(self,name, age) #현재 Student는 Person으로 부터 상속받고 있기 때문에 ~ Person클래스의 생성자를 작성
class Worker(Person):
    company = ''

    def work(self):
        print("일을 합니다")

    def __init__(self, name, age, company):
        self.company = company
        Person.__init__(self,name, age)

    def __str__(self):
        return "Worker의 멤버변수>>" + self.name+', '+str(self.age) +', '+ self.company


if __name__ == '__main__':
    student = Student('홍길동',27)
    student.study()
    print(student)

    print("=============================")

    worker = Worker('김길동', 30,'더조은')
    worker.work()
    print(worker)
    