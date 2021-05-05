from tkinter import *
import threading
import time
import random
# 스레드 실행 클래스
class Thread:
    car = None
    thread = None
    def __init__(self, w,name,x1,y1):
        # 레이블
        self.car = Label(w,text=name) #문자열(자동차1, 2, 3)을 표시할 레이블 설정
        # 스레드 설정
        self.thread = threading.Thread(target = self.run, args=(self.car,name,x1,y1)) # 스레드 설정
        self.thread.start()  #스레드 시작
    # 스레드 실행 함수
    def run(self, car,name,x1,y1):
        speed = 0
        while True:
            speed = random.randrange(10,50) # 한 번에 10~50 사이로 움직임
            if x1 >= 450: # 최대값
                self.car.config(text=name + ' 골인', fg='red') # 최대값 도달시 텍스트 변경
                break
            x1 = x1 + speed 
            self.car.place(x=x1,y=y1) #절대 위치 배치
            time.sleep(0.5) # 대기 시간
# 자동차 배치
def Cars():
    # 창, 텍스트, x좌표, y좌표
    car1 = Thread(w,'자동차1',10,50)
    car2 = Thread(w,'자동차2',10,100)
    car3 = Thread(w,'자동차3',10,150)
# 메인코드
if __name__ == '__main__':
    # 윈도우 배치
    w = Tk() #윈도우창 생성
    w.title('자동자 경주') #윈도우창 제목 
    w.geometry('500x200') # 윈도우창 크기 설정
    # 버튼 배치
    startbutton = Button(w,text='경기 시작', command=Cars) #버튼 설정
    startbutton.pack(side=TOP, fill=X, ipadx=3, ipady=3,padx=5, pady=5) ## .pack() 을 통해 위젯(버튼) 배치
    w.mainloop()