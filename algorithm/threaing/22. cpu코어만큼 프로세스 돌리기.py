# -*- coding: utf-8 -*-
import multiprocessing
import os


class MyProcess(multiprocessing.Process):

    def __init__(self):
        super(MyProcess, self).__init__()

    def run(self):
        print("Child Process PID: {}".format(multiprocessing.current_process().pid))


def main():
    print("Main Process PID: {}".format(multiprocessing.current_process().pid))
    myProcess = MyProcess()
    myProcess.start()
    myProcess.join()
    myProcess.run()

    processes = []

    for i in range(os.cpu_count()):
        process = MyProcess()
        processes.append(process)
        process.start()

    for process in processes:
        process.join()
        process.run()


if __name__ == '__main__':
    main()
