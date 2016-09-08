class Employee(object):
    next_employee_number = 1
    def __init__(self, forename, surname, ssn):
        self.forename = forename
        self.surname = surname
        self.ssn = ssn
        self.employee_number = self.next_employee_number
        Employee.next_employee_number +=1

    def __str__(self):
        return "Name: {}\nSSN: {}\nNumber: {}".format((self.forename + " " + self.surname), self.ssn, self.employee_number)

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
        line2 = "Earnings: {:.2f}".format(self.earnings())
        return "\n".join([line1, super().__str__(), line2])

class HourlyEmployee(Employee):
    employee_type = "Hourly"
    tax_rate = 0.1
    def __init__(self, forename, surname, ssn, rate=0, hours=0):
        super().__init__(forename, surname, ssn)
        self.rate = rate
        self.hours = hours

    def earnings(self):
        return (self.hours * self.rate) * (1 - self.tax_rate)

    def __str__(self):
        line1 = "Type: {}".format(self.employee_type)
        line2 = "Earnings: {:.2f}".format(self.earnings())
        return "\n".join([line1, super().__str__(), line2])

class CommissionEmployee(Employee):
    employee_type = "Commission"
    tax_rate = 0.05
    def __init__(self, forename, surname, ssn, total=0, percent=0):
        super().__init__(forename, surname, ssn)
        self.total = total
        self.percent = percent

    def earnings(self):
        return (self.total / self.percent) * (1 - self.tax_rate)

    def __str__(self):
        line1 = "Type: {}".format(self.employee_type)
        line2 = "Earnings: {:.2f}".format(self.earnings())
        return "\n".join([line1, super().__str__(), line2])
