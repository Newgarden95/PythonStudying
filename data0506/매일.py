class Day():
    # 실제값 변수 : 인스턴스 변수
    doing = ''
    hour = 0
    place = ''
    count = 0
    '''
    생성자
    '''
    def __init__(self, doing, hour, place):
        self.doing = doing  # 입력받은 값 저장하기
        self.hour = hour    # 입력받은 값 저장하기
        self.place = place  # 입력받은 값 저장하기
        Day.count += 1
        print(str(Day.count)+'개 객체가 생성되었습니다')

    def study(self):
        return self.doing+'공부를 '+str(self.hour)+'시간 하다'
    
    def where(self):
        return self.place+'에서 '+str(self.doing)+'를 하다'

    def __str__(self):
        return '매일 클래스의 속성>>'+self.doing+','+str(self.hour)+','+self.place

if __name__ == '__main__':
    day1 = Day('파이썬공부', '10', '강남')
    study = day1.study()
    print(study)
    print(day1)

    print("==========================================")

    day2 = Day('와인공부', 13, '북촌')
    study2 = day2.study()
    print(study2)
    print(day2)
