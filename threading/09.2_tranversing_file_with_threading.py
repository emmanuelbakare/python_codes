# this code just search for the occurrent of file 11.jpg from a path 
# This add threading to the code
# 1. add threading and lock module
# 2. lock and release  the update matches

import os
import threading

matches = []
lock = threading.Lock()

def file_search(root, filename):
    try:
        print("Searching file in", root)
        for file in os.listdir(root):
            full_path = os.path.join(root, file)

            if filename in file:
                with lock:
                    matches.append(full_path)

            if os.path.isdir(full_path):
                thread = threading.Thread(target=file_search, args=(full_path, filename))
                thread.start()
                thread.join()  # You can move this to manage concurrency better (see note below)
    except Exception as e:
        print(f"Error accessing {root}: {e}")

def main():
    root_dir = "c:/codes/python2"
    filename = "11.jpg"

    # Start initial search in a thread
    main_thread = threading.Thread(target=file_search, args=(root_dir, filename))
    main_thread.start()
    main_thread.join()

    print("\nSearch Results:")
    with lock:
        if matches:
            for match in matches:
                print("Match:", match)
        else:
            print("No Match")

if __name__ == "__main__":
    main()
