from threading import Thread
import time

def do_work():
    print("Do Working")
    # time.sleep(2)
    i=0
    for i in range(2000000): i += 1
    print("finish  Working")

def main():
    for _ in range(5):
        thread= Thread(target=do_work, args=())
        thread.start()
        

if __name__=="__main__":
    main()

    