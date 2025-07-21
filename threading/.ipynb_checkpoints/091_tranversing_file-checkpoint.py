import os 

matches= []
def  file_search(root, filename):
    print("searching file in ", root)

    for file in os.listdir(root):
        full_path = os.path.join(root, file)
        print(f"Filename: {filename}, FILE: {file}")
        if filename in file:
            matches.append(full_path)
        if os.path.isdir(full_path):
            file_search(full_path, filename)

def main():
    file_search("c:/codes/python2","*.jpg")
    print()
    if len(matches) >0:
        for match in matches:
            print("Matche: ", match)
    else:
        print("No Match")

main()

