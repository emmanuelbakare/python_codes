# load files with count_urls method with threading
# this approach is not correct because the answers will vary because their is no thread synchronization
import json
import urllib.request
import time 
from threading import Thread

finish_count = 0
def count_urls(frequecy, url):
    response = urllib.request.urlopen(url)
    txt = str(response.read())

    for l in txt:
        letter = l.lower()
        if letter in frequecy:
            frequecy[letter] += 1
    # if this thread finishes, then add one to the finish_count
    global finish_count
    finish_count += 1

def main():
    frequency = {}
    for letter in 'abcdefghijklmnopqrstuvwxyz':
        frequency[letter]=0
    start_time = time.time()
    for num in range(1000,1003):
        thread = Thread(target=count_urls, args=(frequency,f"https://www.rfc-editor.org/rfc/rfc{num}.txt")).start()

    # check if all the threads as finished or not. 
    # there is a better way to do it though
    while finish_count < 3:
        print('not done... working on Thread', finish_count)
        time.sleep(0.5)
    
    end_time = time.time()
    
    print(json.dumps(frequency, indent=4))
    print("End Time:", end_time - start_time)

if __name__=="__main__":
    main()
    