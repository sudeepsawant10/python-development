"""
Thread=> Running several different programs concurrently.
"""

import _thread
import time

# define function of thead


def print_time(threadName, delay,):
    count = 0
    while count < 5:
        time.sleep(delay)
        count += 1
    print("%s:%s" % (threadName, time.ctime(time.time())))


# create two thread
try:
    _thread.start_new_thread(print_time("Thread-1", 2))
    _thread.start_new_thread(print_time("Thread-2", 4))
except:
    print("Error: Unable to start thead")
while 1:
    pass
