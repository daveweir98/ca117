import sys

def cont(w):
    test = list("evil")
    check = ""
    for i in w.lower():
        if i in test:
            check = check+i
    if check == "evil":
        print (w.strip("\n"))

def main():
    for words in sys.stdin:
        cont(words)

if __name__ == "__main__":
    main()
