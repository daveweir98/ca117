#Darraghs file_112.py
class File(object):
    FILE_PERMISSIONS = "rwx"

    def __init__(self, name, owner, size=0, permissions=""):
        self.name = name
        self.owner = owner
        self.size = size
        self.permissions = permissions

    def enable_permission(self, user, mode):
        if self.owner != user:
            print("Access Denied")
            return
        if mode not in self.FILE_PERMISSIONS:
            return
        if mode in self.permissions:
            return
        self.permissions = mode

    def disable_permissions(self, user, mode):
        if self.owner != user:
            print("Access Denied")
            return
        if mode in self.permissions:
            self.permissions = self.permissions.replace(mode, "")

    def has_access(self, user, mode):
        if user == self.owner and mode in self.permissions:
            return "Access Granted"
        return "Access Denied"

    def get_permissions(self):
        if not self.permisssions:
            return "null"
        return "".join(sorted(self.permissions))

    def get_size(self):
        return(self.size)

    def __str__(self):
        return "File: {}\nOwner: {}\nPermissions: {}\nSize: {}".format(self.name, self.owner,self.get_permissions(), self.size)

#Darraghs folder_111.py
class Folder(object):
    #d is a dictionary that maps from file names to file objects
    def __init__(self):
        self.d = {}

    def add_file(self, f):
        if f.name in self.d:
            print("File already exists")
            return
        self.d[f.name] = f

    def del_file(self, user, name):
        if f.name not in self.d:
            print("No such file")
            return
        if self.d[name].owner != user:
            print("Access Denied")
            return
        del self.d[name]

    def get_size(self):
        return sum([f.get_size() for f in self.d.values()])

    def __str__(self):
        heading = "folder contents"
        uline = "-"*len(heading)
        slist = [heading, uline]
        for k in self.d.keys():
            slist.append(sorted(self.d[k].__str__()))
        slist.append("Folder size: {} bytes".format(self.get_size()))
        return "\n".join(slist)

#Darraghs Weight_11.py, not complete but should be able to finish from this
class Weight(object):
    OUNCES_PER_POUND = 16
    def __init__(self, pounds=0, ounces=0):
        self.ounces = ounces
        self.pounds = pounds

    def to_ounces(self):
        ounces = self.ounces
        ounces += self.pounds * self.OUNCES_PER_POUND
        return ounces

    def __eq__(self, other):
        return self.to_ounces() == other.to_ounces()

    def __gt__(self, other):
        return self.to_ounces() > other.to_ounces()

    def __ge__(self, other):
        return self.to_ounces() >= other.to_ounces()

    def __add__(self, other):
        return from_ounces(self.to_ounces() + other.to_ounces())

    def __iadd__(self, other):
        z = self + other
        self.pounds = z.pounds
        self.ounces = z.ounces
        return z

    @classmethod
    def from_ounces(cls, ounces):
        pounds, ounces = divmod(cls.ounces, cls.OUNCES_PER_POUND)
        return cls(pounds, ounces)

#Darraghs employee_111.py, again have to finish
class Employee(object):
    next_employee_number = 1
    def __init__(self, forename, surname, ssn):
        self.forename = forename
        self.surname = surname
        self.ssn = ssn
        self.emplyee_number = self.next_employee_number
        Employee.next_employee_number +=1

    def __str__(self):
        return "Name: {}\nSSN: {}\nNumber: {}\nType: {}".format((self.forename + self.surname), self.ssn)

class SalariedEmployee(Employee):
    employee_type = "Salaried"
    tax_rate = 0.2
    def __init__(self, forename, surname, ssn, salary=0):
        super().__init__(forename, surname, ssn)
        self.salary = salary

    def earnings(self):
        return self.salary * (1-self.tax_rate)

    def __str__(self):
        line1 = "Type: {}".format(self.employee_type)
        line2 = "Earnings: {}".format(self.earnings())
        return "\n".join([line1, super().__init__(), line2])

#Darraghs match.py
name = r""

ip_address = r"(?:(?:[0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.){3}(?:[0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\b"
