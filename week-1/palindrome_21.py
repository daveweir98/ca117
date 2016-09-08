import sys

def main():
    l = sys.argv[1]
    for i in l:
        if not i.isalnum():
            l = l.replace(i, "")

    print(l == l[::-1])

if __name__ == "__main__":
    main()
