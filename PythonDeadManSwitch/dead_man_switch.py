import signal
import time
import datetime
import threading

TIMEOUT = 1440 * 60 # secs to wait for interaction (24h)

def interrupted(signum, frame): #"called when read times out"
    print('Exiting')
    signal.signal(signal.SIGALRM, interrupted)

def count(s):
    current_time = datetime.datetime.now().time()
    print ('Active since : {}'.format(datetime.datetime.now().time()))
    while True:
        print ('Hour : {}'.format(s))
        s = s + 1
        time.sleep(60 * 60)

def i_input():
    try:
        print('You have 24 hours to interact or this script will cease to execute')
        foo = input() # for only one cycle return foo
        print('Input received at {}, reseting.'.format(datetime.datetime.now().time()))
        i_input()
    except:
        return # timeout
        signal.alarm(TIMEOUT) # set alarm 
        # <WRITE FAIL-SAFE COMMANDS HERE>

threading.Thread(target = i_input).start()
countThread = threading.Thread(target=count, args=(0,)); # <- note extra ','
countThread.start();
