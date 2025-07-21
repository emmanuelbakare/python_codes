# when parent thread is running join helps it to pass control to child thread and pause for the child thread to finish running 
# before continueing. the join can also stipulate how long it has to wait to resume running.

import time
from threading import Thread

def child():
    print("Child thread doing work")
    time.sleep(5)
    print("Child thread FINISH work")

def parent():
    print("Parent Thread start work")

    t = Thread(target=child, args=())
    t.start()
    print("Parent Thread is waiting...")
    t.join()  # this stops the parent thread while the child thread processes
    print("Parent Thread Continue Working...")


parent()