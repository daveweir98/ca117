import re
import sys


def main():
    s = sys.stdin.read()
    dob1 = re.compile("\d{1,2}\/\d{1,2}\/\d{1,2}")
    dob2 = re.compile("\d{1,2}\-\d{1,2}\-\d{1,2}")
    dob3 = re.compile("\d{1,2}[-/]\d{1,2}[-/]\d{1,2}")
    phone = re.compile("01[ -]\d{1,8}")
    email = re.compile("(?:\w+\.)*\w+\@\w+\.\w+(?:\.\w+)*")
    date = re.compile("\d{1,2}\s\w{3}\s\d{1,4}")
    print(dob1.findall(s))
    print(dob2.findall(s))
    print(dob3.findall(s))
    print(phone.findall(s))
    print(email.findall(s))
    print(date.findall(s))

if __name__ == "__main__":
    main()
