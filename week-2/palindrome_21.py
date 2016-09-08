import sys

def palindrome( s ):
   i = 0
   while i < len(s)/2:
      if s[i] != s[-(i + 1)]:
         return False
      i += 1 
   
   return True

def main():
   s = sys.argv[1].lower()
   for i in s:
      if i.isalpha() == False:
         s = s.replace(i, "")
 
   print ( palindrome( s ) )

if __name__ == "__main__":
   main()
