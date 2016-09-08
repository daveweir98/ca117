class Student(object):
    def __init__(self, surname, firstname, ID, modlist=[]):
        self.surname = surname
        self.firstname = firstname
        self.id = ID
        self.modlist = modlist

    def add_module(self, a):
        if a not in self.modlist:
            self.modlist.append(a)

    def del_module(self, a):
        if a in self.modlist:
            self.modlist.remove(a)

    def print_details(self):
        print("ID: {}".format(self.id))
        print("Surname: {}".format(self.surname))
        print("Forename: {}".format(self.firstname))
        print("Modules: {} ".format(" ".join(self.modlist)))
