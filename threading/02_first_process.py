# from threading import Thread
import multiprocessing
from multiprocessing import Process
import time

def do_work():
    print("Do Working")
    # time.sleep(2)
    i=0
    for i in range(2000000): i += 1
    print("finish  Working")

def main():
    multiprocessing.set_start_method('spawn')
    for _ in range(5):
        p= Process(target=do_work, args=())
        p.start()
        

if __name__=="__main__":
    main()

    
