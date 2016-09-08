import sys
dic = {}

def dictionary():
    f = open(sys.argv[1], "r")
    text = [w for w in f]
    f.close()
    for i in text:
        details = i.split()
        dic[details[0]] = details[1], details[2]


def main():
    dictionary()
    names = [w.strip() for w in sys.stdin]
    for i in names:
        if i in dic:
            print("Phone: {}".format(dic[i][0]))
            print("Email: {}".format(dic[i][1]))
        else:
            print("No such contact")



if __name__ == "__main__":
    main()
