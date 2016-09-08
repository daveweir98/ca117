import sys

def counter(s):
    count = [0, 0, 0, 0]
    for i in s:
        if i.isupper():
            count[0] = 1
        elif i.isdigit():
            count[1] = 1
        elif i.islower():
            count[2] = 1
        else:
            count[3] = 1
      
    return sum(count)

def main():
   print(counter(sys.argv[1]))

if __name__ == "__main__":
   main()
