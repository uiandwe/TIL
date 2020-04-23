# -*- coding: utf-8 -*-
"""
pipe - 프로세스간의 데이터 전송, 단방향
pipeout, pipein = os.pipe()
이 한쌍으로 움직임
"""
import os, sys
import multiprocessing

class ChildProcess(multiprocessing.Process):

  def __init__(self, pipein):
    super(ChildProcess, self).__init__()
    self.pipein = pipein

  def run(self):
    print("Attempting to pipein to pipe")
    self.pipein = os.fdopen(self.pipein, 'w')
    self.pipein.write("My Name is Elliot")
    self.pipein.close()

def main():
  pipeout, pipein = os.pipe()

  child = ChildProcess(pipein)
  child.start()
  child.join()

  os.close(pipein)
  pipeout = os.fdopen(pipeout)

  pipeContent = pipeout.read()
  print("Pipe: {}".format(pipeContent))

if __name__ == '__main__':
  main()
