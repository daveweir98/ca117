import sys

def sumFac(n):
   nums = []
   for i in range(1,n):
      if n%i == 0:
         nums.append(i)
   return(sum(nums))

def isPerfect(n):
   return bool(n == sumFac(n))

def main():
   numbers = [int(n) for n in sys.stdin]
   for n in numbers:
      print(isPerfect(n))

if __name__ == "__main__":
   main()
