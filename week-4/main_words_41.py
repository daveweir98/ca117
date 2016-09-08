import sys
from string import punctuation


def main():
    dic = {}
    words = [w.strip().lower().rstrip(punctuation) for w in sys.stdin.read ().split()]
    a = []
    for i in words:
        if i in dic:
            dic[i] += 1
        else:
            a.append(i)
            a = sorted(a)
            dic[i] = 1

    for i in a:
        if len(i) > 3 and dic[i] > 2:
            print(i, ":", dic[i])
if __name__ == "__main__":
    main()