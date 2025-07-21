# this code simulate a race condition where the output comes out wrong because the system updated the amount value at the same time


from threading import Thread
import time

class StingySpendy:
    amount =100

    def stingy(self):
        for i in range(10000000):
            self.amount +=100
        print("Stingy Done")

    def spendy(self):
        for i in range(10000000):
            self.amount -=100
        print("Spendy Done")

def main():
    ss = StingySpendy()
    Thread(target=ss.stingy, args=()).start()
    Thread(target=ss.spendy, args=()).start()
    
    time.sleep(2)
    print("Balance Amount: ", ss.amount)

main()
        