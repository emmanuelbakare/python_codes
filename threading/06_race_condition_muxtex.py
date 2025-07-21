# Use Lock to solve the race condition issue
#add lock.acquire and lock.release to lock a process/method from been used by thread2 when thread1 acquired it.


from threading import Thread, Lock
import time

class StingySpendy:
    amount =100
    mutex = Lock()

    def stingy(self):
        
        for i in range(10000000):
            self.mutex.acquire() # lock the thread just before updating the value
            self.amount +=100
            self.mutex.release() # release the locked thread so that others can acquire it.
        print("Stingy Done")

    def spendy(self):
        for i in range(10000000):
            self.mutex.acquire() # lock the thread just before updating the value
            self.amount -=100
            self.mutex.release() # release the locked thread so that others can acquire it.
        print("Spendy Done")

def main():
    ss = StingySpendy()
    Thread(target=ss.stingy, args=()).start()
    Thread(target=ss.spendy, args=()).start()
    
    time.sleep(5)
    print("Balance Amount: ", ss.amount)

if __name__=="__main__":
    main()
        