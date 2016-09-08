import sys

vowel = ["a", "e", "i", "o" , "u"]
singles = ["x", "s", "z", "o"]
doubles = ["ch", "sh"]

def plural(s):
   if s[-1] in singles:
      return s + "es"
   elif s[-2:] in doubles:
      return s + "es"
   elif s[-1] == "f":
      return s[:len(s)-1] + "ves"
   elif s[-2:] == "fe":
      return s[:len(s)-2] + "ves" 
   elif s[-2] not in vowel and s[-1] == "y":
      return s[:-1] + "ies"
   else: 
      return s + "s"
     

def main():
   print(plural(sys.argv[1]))

if __name__ == "__main__":
   main()
