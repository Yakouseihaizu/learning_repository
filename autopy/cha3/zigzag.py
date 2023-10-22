import time,sys

indent = 0 # How many spaces to indent
indentIncreasing = True

try:
    while True:  # the main program loop
        print(' '*indent,end='')
        print('********')
        time.sleep(0.1) # pause for 1/10 of a second

        if indentIncreasing:
            # Increase the number of the spaces
            indent+=1
            if indent == 5:
                indentIncreasing = False
        else:
            indent-=1
            if indent == 0:
                indentIncreasing = True
except KeyboardInterrupt:
    sys.exit()
