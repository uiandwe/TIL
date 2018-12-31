import _thread
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
    _thread.start_new_thread(buzzer1, ())
    _thread.start_new_thread(buzzer2, ())

    while 1:
        pass
