import sys

def roots(a, b, c):
   if (b**2)-4*(a*c) < 0:
      return None
   else:
      r1 = (-b + ((b**2) - 4*(a*c))**0.5)/(2*a)
      r2 = (-b - ((b**2) - 4*(a*c))**0.5)/(2*a)
      return [r1, r2]

def main():
   nums = [n.strip() for n in sys.stdin]
   for n in nums:
      details = n.split()
      a = float(details[0])
      b = float(details[1])
      c = float(details[2])
      r = roots(a, b, c)
      if r == None:
         print(None)
      else:
         print("r1 = {}, r2 = {}".format(r[0], r[1]))

if __name__ == "__main__":
   main()
