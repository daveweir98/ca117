import sys

def converter(n, base):
   n = n[::-1]
   total = 0 
   i = 0 
   while i < len(n):
      total = total + ((base**i)*int(n[i]))
      i += 1 
   return total

def main():
   n = sys.argv[1]
   base = int(sys.argv[2])
   print (converter(n, base))

if __name__ == "__main__":
   main()
