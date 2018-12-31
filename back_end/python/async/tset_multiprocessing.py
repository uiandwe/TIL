from multiprocessing import Process
import time

def buzzer1():
    for i in range(10):
        print("beep 1")
        time.sleep(2)

def buzzer2():
    for i in range(10):
        print("beep 2")
        time.sleep(3)


if __name__ == '__main__':
    p1 = Process(target=buzzer1)
    p2 = Process(target=buzzer2)
    p1.start()
    p2.start()
