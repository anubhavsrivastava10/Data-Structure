class car:
    def __init__(self,speed):
        self.speed = 0
        print(self.speed)
    def start(self):
        self.speed = 0
    def accelerate(self):
        self.speed += 5
    def brake(self):
        self.speed -= 5
    def stop(self):
        self.speed = 0
    def get_speed(self):
        return self.speed


def main():
    speed = 0
    mycar = car(speed)
    #start
    print('Start the car')
    mycar.start()
    print(mycar.get_speed())
    #accelerate
    mycar.accelerate()
    print(mycar.get_speed())
    mycar.accelerate()
    print(mycar.get_speed())
    mycar.accelerate()
    print(mycar.get_speed())
    #brake
    mycar.brake()
    print(mycar.get_speed())
    mycar.brake()
    print(mycar.get_speed())
    #accelerate
    mycar.accelerate()
    print(mycar.get_speed())
    #stop
    mycar.stop()
    print(mycar.get_speed())
    print('Car Stopped')
main()

class car:
    def __init__(self,speed_1,speed_2):
        self.speed_1 = 0
        self.speed_2 = 0
    def accelerate(self,acc_1,acc_2):
        for i in range(3):
            self.speed_1 += acc_1
            self.speed_2 += acc_2
    def brake(self,dec_1,dec_2):
        flag = 0
        while flag == 0 :
            self.speed_1 -= dec_1
            self.speed_2 -= dec_2
            if self.speed_1<=0 and self.speed_2<=0:
                flag = 1
                return 0
            if self.speed_1<=0:
                flag = 1
                return 1
            elif self.speed_2<=0:
                flag = 1
                return 2
    def get_speed(self):
        return self.speed_1,self.speed_2


def main():
    speed_1 = 0
    speed_2 = 0
    # accelaration
    acc_1 = 5
    acc_2 = 3
    # deacceleration
    dec_1 = 2
    dec_2 = 1
    mycar = car(speed_1,speed_2)
    #start
    print('Start the car')
    # print(mycar.get_speed())
    #accelerate
    mycar.accelerate(acc_1,acc_2)
    # print(mycar.get_speed())
    #brake
    value = mycar.brake(dec_1,dec_2)
    if value==0:
        print('Both car finished at the same time')
    elif value==1:
        print('Car 1 won the race')
    else:
        print('Car 2 won the race')
    # print(mycar.get_speed())
main()
