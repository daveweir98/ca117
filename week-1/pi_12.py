import sys
from math import pi

def magic(n):
   return "{:.{}f}".format(pi, n)

def main():
   print (magic(int(sys.argv[1])))

if __name__ == "__main__":
   main()
