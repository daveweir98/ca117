from collections import namedtuple


Student = namedtuple("Student", ["firstname", "surname", "id"])

def show_student(s):
    print("{0:>11s} {1:<}".format("First name:", s.firstname))
    print("{0:>11s} {1:<}".format("Surname:", s.surname))
    print("{0:>11s} {1:<}".format("ID:", s.id))

