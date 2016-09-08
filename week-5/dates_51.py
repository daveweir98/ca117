import sys
import calendar

def NumDate(d):
    details = d.split(" ")
    day, month, year = details[0], details[1], details[2]
    months = list(calendar.month_abbr)
    print("{}/{}/{}".format(day,months.index(month[0:3]),year[2:]).strip("\n"))

def main():
    for date in sys.stdin:
        NumDate(date)

if __name__ == "__main__":
    main()
