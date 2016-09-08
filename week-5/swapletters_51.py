import sys

def swap(w):
    for i in range(0,(len(w)-1), 2):
        tmp = w[i]
        w[i] = w[i + 1]
        w[i + 1] = tmp

    return "".join(w)

def main():
    word = list(sys.argv[1])
    print(swap(word))


if __name__ == "__main__":
    main()
