import sys
import string

def count(s):
   seen = []
   for i in s: 
      sent = i.split()
      for word in sent:
         word = word.lower()
         for l in word:
            if l in string.punctuation:
               word = word.replace(l, "")
         if word not in seen:
            seen.append(word)
   return len(seen) - 1

def main():
   s = sys.stdin.readlines()
   print (count(s))

if __name__ == "__main__":
   main()
