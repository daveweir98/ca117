import sys

def capital(s):
   return s[0].capitalize() + s[1:-1] + s[-1].capitalize()

def main():
   s = sys.argv[1]
   if len(s) > 1:
      print( capital(s) )

if __name__ == "__main__":
   main()
