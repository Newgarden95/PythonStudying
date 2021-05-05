'''
클래스의 역할 => 틀의 역할!
object(객체): 틀을 가지고 만든 실제 대상(객체, 우리가 쓸 수 있는 부품의 형태)

'''
class Dog():
    #멤버변수
    color = None
    field = ''
    
    #생성자함수(객체생성시 자동호출되는 함수, 객체 생성시 초기화를 담당)~> constructor
    def __init__(self, color, field): # 초기화 담당 함수
        self.color = color
        self.field = field
        print("생성자가 호출됨")

    #멤버함수
    def jump(self):
        print('강아지가 점프한다')

    def sleep(self):
        print('강아지가 자고있다')

    #오버라이드(재정의)
    def __str__(self):  # toString()
        return 'dog의 속성값들 > ' + str(self.color) + ',' + self.field

if __name__ == '__main__':
    dog1 = Dog('white' , '요크셔테리어')  # 참조형(정수, 실수, 논리 빼고) => 주소를 갖는 데이터타입
                  # 객체생성할 때 dog1에 대한 특성을 저장하기 위해 멤버변수(color, field)들이 복사~> 복사된 위치를 dog1에 넣어줌
    dog2 = Dog('blue' , '진돗개')
    print(dog1)
    dog1.sleep()
    print(dog2)
