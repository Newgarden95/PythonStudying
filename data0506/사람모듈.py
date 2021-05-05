class Person:
    name = None
    age = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print('먹다')

    def __str__(self):
        return str(self.name) + ' ' + str(self.age)



'''상속'''
class Man(Person):
    speed = 0

    def run(self):
        print("발리 달리다")

    def __str__(self):
        return str(self.name) + ' ' + str(self.age) + ' ' +str(self.speed)


class Superman(Man):
    fly = False

    def sky(self):
        print('하늘을 날다.')

    def __str__(self):
        return str(self.name) + ' ' + str(self.age) + ' ' + str(self.speed) + ' ' + str(self.fly)