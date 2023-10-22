# stopwatch.py - A simple stopwatch program.

import time,sys

print('Press ENTER to begin. Afterward, press ENTER to "click" the stopwatch.Press Ctrl-C to quit')
input()
print('Start!!')
startTime = time.time()
lastTime = startTime
lapNum = 1

while True:
    try:
        input()
        # lastTime = time.time()
        newTime = time.time()
        print(f'lap {lapNum} #      '+str(round(newTime-lastTime,2)))
        lastTime = newTime
        lapNum+=1
    except KeyboardInterrupt:
        finalTime = time.time()
        print(f'Total time: {finalTime-startTime}\nTotal lap:{lapNum}')
        sys.exit()

    