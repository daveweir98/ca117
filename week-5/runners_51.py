import sys

def top_time(lines):
    top = 1000000000000
    best_time = None
    best_name = None
    for l in lines:
        details = l.split(" ")
        name = details[0]
        times = details[1:]
        try:
            for t in times:
                sec = t.split(":")
                sec = (int(sec[0])*60) + int(sec[1])
                if sec < int(top):
                    best_time = t
                    top = sec
                    best_name = name
        except:
            pass

    print("{} : {}".format(best_name, best_time))

def main():
        lines = [l for l in sys.stdin]
        top_time(lines)

if __name__ == "__main__":
    main()
