import sys
dic = {}

def dictionary():
    f = open(sys.argv[1], "r")
    text = [w for w in f]
    f.close()
    for i in text:
        dic[i[:-12].strip()] = i[-12:].strip()

    return dic

def main():
    dictionary()
    names = [w.strip() for w in sys.stdin]
    for i in names:
        if i in dic:
            print("Phone: {}".format(dic[i]))
        else:
            print("No such contact")



if __name__ == "__main__":
    main()