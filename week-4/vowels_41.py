import sys
import operator

def main():
    dic = {"a":0, "e":0, "i":0, "o":0, "u":0 }
    lines = [w for w in sys.stdin]
    for line in lines:
        for i in line:
            i = i.lower()
            if i in dic:
                dic[i] += 1

    sorted_dic = sorted(dic.items(), key = operator.itemgetter(1))[::-1]

    for i in sorted_dic:
        print("{:s} : {:3d}".format(i[0], i[1]))

if __name__ == "__main__":
    main()
