import sys

def diamond(n):
    i = (-n + 1)
    while i < n :
        print(" " * abs(i), end='')
        print ("* " * (n-abs(i)))
        i += 1

def main():
    n = int(sys.argv[1])
    (diamond(n))

if __name__ == "__main__":
    main()