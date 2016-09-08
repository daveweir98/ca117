import sys

def anagram(i, j):
    for k in i:
        if k in list(j) and len(i)==len(j):
            return True
        else:
            return False

def main():
    l = [w.strip() for w in sys.stdin]
    for i in l:
        details = i.split()
        print(anagram(details[0], details[1]))

if __name__ == "__main__":
    main()
