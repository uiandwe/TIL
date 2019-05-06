# -*- coding: utf-8 -*-
import subprocess
proc = subprocess.Popen(['echo', 'hello'], stdout=subprocess.PIPE)

out, err = proc.communicate()
print(out.decode('utf-8'))


proc = subprocess.Popen(['sleep', '0.3'])
while proc.poll() is None:
    print('working...')

print('exit ', proc.poll())

def run_sleep(period):
    proc = subprocess.Popen(['sleep', str(period)])
    return proc

from time import time
start = time()
procs = []
for _ in range(10):
    proc = run_sleep(0.1)
    procs.append(proc)

for proc in procs:
    proc.communicate()

end = time()

# 10번을 반복했지만 0.1초가 걸림 
print(end - start)

