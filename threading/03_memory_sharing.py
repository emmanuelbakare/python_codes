# load files with count_urls without threading

import json
import urllib.request
import time 

def count_urls(frequecy, url):
    response = urllib.request.urlopen(url)
    txt = str(response.read())

    for l in txt:
        letter = l.lower()
        if letter in frequecy:
            frequecy[letter] += 1

def main():
    frequency = {}
    for letter in 'abcdefghijklmnopqrstuvwxyz':
        frequency[letter]=0
    start_time = time.time()
    for num in range(1000,1003):
        count_urls(frequency,f"https://www.rfc-editor.org/rfc/rfc{num}.txt" )
    
    end_time = time.time()
    
    print(json.dumps(frequency, indent=4))
    print("End Time:", end_time - start_time)

if __name__=="__main__":
    main()
    