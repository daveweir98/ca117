import sys

def count(s):
   total = 0
   for i in s:
      details = i.split()
      total = total + len(details)
   return total

def main():
   s = sys.stdin.readlines()
   print (count(s))

if __name__ == "__main__":
   main()
