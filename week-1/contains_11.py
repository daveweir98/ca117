import sys

def contains (s, q):
   cont = True
   i = 0
   while i < len(q):
      if q[i] not in s:
         cont = False
      else:
         s = s.replace(q[i], "", 1)
      i += 1 
   
   return cont

def main():
   q = sys.argv[1]
   s = sys.argv[2]
   print( contains(s, q) )

if __name__ == "__main__":
   main()
