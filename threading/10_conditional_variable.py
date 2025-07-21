from threading import Thread, Condition
import time

class StingySpendy:
    amount =100
    cv = Condition()

    def stingy(self):
        
        for i in range(1000000):
            self.cv.acquire() # lock the thread just before updating the value
            self.amount +=100
            self.cv.notify()  # after adding 100 to amount, notify spendy that there is money added to the account
            self.cv.release() # release the locked thread so that others can acquire it.
        print("Stingy Done")

    def spendy(self):
        for i in range(500000):
            self.cv.acquire() # lock the thread just before updating the value
            while self.amount < 20: # if the amount is less than 20 then spendy should wait until it is notified that the condition may have changed
                self.cv.wait()
            self.amount -=200
            while self.amount < 0:
                print(self.amount)
            self.cv.release() # release the locked thread so that others can acquire it.
        print("Spendy Done")

def main():
    ss = StingySpendy()
    Thread(target=ss.stingy, args=()).start()
    Thread(target=ss.spendy, args=()).start()
    
    time.sleep(5)
    print("Balance Amount: ", ss.amount)

if __name__=="__main__":
    main()
        