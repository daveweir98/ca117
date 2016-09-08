import sys 

def tmark(f):

    tops = ""
    topm = 0
    for s in f:
        try:
           details = s.split()
           mark = int(details[0])
           name = " ".join(details[1:])
           if mark > topm:
                topm = mark
                tops = name
           elif mark == topm:
               tops = tops + ", " + name

        except(ValueError):
            print ("Invalid mark {:s} encountered. Skipping.".format(details[0]))
            

    print( "Best student(s): {}".format(tops))
    print( "Best mark: {}".format(topm))
    

def main():
    try:
        students = sys.argv[1]
        f = open(students, "r")
        tmark(f)
        f.close()

    except(FileNotFoundError):
        print("The file {:s} could not be opened".format(students))

        

if __name__ == "__main__":
    main()
