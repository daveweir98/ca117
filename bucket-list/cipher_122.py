import sys

def sorter(t):
    return t[1]

def main():
    alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789")
    text = [w.strip() for w in sys.stdin]
    #count = {i:0 for i in [i for i in " ".join(text)] if i.isalnum()}
    count = {}
    for i in " ".join(text):
        if i in count and i.isalnum():
            count[i] += 1
        elif i.isalnum():
            count[i] = 1

    most_common = sorted(count.items(), key=sorter, reverse=True)[0][0]
    if alphabet.index(most_common) <= alphabet.index("E"):
        cipher_num = alphabet.index("E") - alphabet.index(most_common)
    else:
        cipher_num = (alphabet.index("E")+36) - alphabet.index(most_common)

    rotated = alphabet[cipher_num:] + alphabet[:cipher_num]
    dic = {}
    for i in range(len(alphabet)):
        dic[alphabet[i]] = rotated[i]

    for line in text:
        new = ""
        for letter in line:
            if letter in dic:
                new += dic[letter]
            else:
                new += letter
        print(new)

if __name__=="__main__":
    main()
