import sys

def main():
    numbers = list(range(1,31))
    print("Multiples of 3: {}".format([n for n in numbers if not n % 3]))
    print("Multiples of 3 squared: {}".format( [n**2 for n in numbers if not n % 3]))
    print("Multiples of 4 doubled: {}".format( [n*2 for n in numbers if not n % 4]))
    print("Multiples of 3 or 4: {}".format( [n for n in numbers if not n % 3 or not n % 4]))
    print("Multiples of 3 and 4: {}".format( [n for n in numbers if not n % 3 and not n % 4]))
    print("Multiples of 3 replaced: {}".format( [n if n % 3 else "X" for n in numbers]))

 
if __name__ == "__main__":
    main()
