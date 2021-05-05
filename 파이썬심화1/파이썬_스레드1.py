from tkinter import *
import threading
import time
import random
# 스레드 클래스
class Thread:
    car = None
    thread = None
    def __init__(self, w,img,x1,y1): # Thread 클래스 생성자(초기화부분) :
        # 이미지 할당
        self.car = Label(w) # 이미지를 표시할 레이블 설정
        icon = PhotoImage(file = img) #위젯에 표시할 이미지의 경로를 설정
        self.car.configure(image = icon) #레이블 위젯 속성을 이미지로 변경
        self.car.image = icon # 이미지를 레이블에 넣어주기
        # 스레드 설정
        self.thread = threading.Thread(target = self.run, args=(self.car,x1,y1)) # threading 클래스에 있는 Thread함수 사용
                                        # target : 실행하고자 하는 함수 
                                        # args : 쓰레드가 실행하는 함수에 입력 파라미터를 전달
        self.thread.start() # 스레드 실행
    # 스레드 실행 함수
    def run(self, car,x1,y1):
        speed = 0
        while True:
            speed = random.randrange(10,50) # 한 번에 10~50 사이로 움직임
            if x1 >= 500: # 골인 지점
                break
            x1 = x1 + speed
            self.car.place(x=x1,y=y1) # 절대위치에 배치
            time.sleep(0.5) # 대기시간
# 자동차 배치
def Cars():
    # 창, 파일명, x좌표, y좌표
    car1 = Thread(w,'carimage1.PNG',10,70) #Thread클래스 초기화
    car2 = Thread(w,'carimage2.PNG',10,180)
    car3 = Thread(w,'carimage1.PNG',10,300)
# 메인코드
if __name__ == '__main__':
    # 윈도우 배치
    w = Tk() #윈도우창 생성
    w.title('자동자 경주') # 윈도우 창 제목 설정
    w.geometry('500x400') # 윈도우 창 크기 설정
    # 버튼 배치
    startbutton = Button(w,text='경기 시작', command=Cars) # 버튼 생성 => command=Cars 버튼 누를 시 Cars() 함수 실행
    startbutton.pack(side=TOP, fill=X, ipadx=3, ipady=3,padx=5, pady=5) # .pack() 을 통해 위젯(버튼) 배치
    w.mainloop()