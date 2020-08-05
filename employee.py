import datetime


class Employee(object):
    percent_rise = 1.05
    """ 5% Pay rise"""
    num_employees = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        # self.email = '{}.{}@public-enemy.com'.format(self.first, self.last).lower()
        self.email = f'{self.first.lower()}.{self.last.lower()}.@public-enemy.com'
        Employee.num_employees += 1

    def __repr__(self):
        return f'{self.email} is earning £{self.pay}.'

    def fullname(self):
        return f'{self.first} {self.last}'

    def apply_raise(self):
        self.pay = int(self.pay * self.percent_rise)

    @classmethod
    def set_raise_amt(cls, amount):
        cls.percent_rise = amount

    # alternative constructor - use from_ (default) as start of func name
    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    # used when no class or instance is needed
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


class Developer(Employee):
    percent_rise = 1.10

    def __init__(self, first, last, pay, prog_lang):
        super(Developer, self).__init__(first, last, pay)
        # alternative inheritance to super()
        # Employee.__init__(self, first, last, pay)
        self.prog_lang = prog_lang


class Manager(Employee):
    def __init__(self, first, last, pay, employees=None):
        super(Manager, self).__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def list_emps(self):
        for emp in self.employees:
            print('--->', emp.fullname())


# Employee.set_raise_amt(1.05)

emp_1 = Employee('Carlos', 'Rodriguez', 50000)
emp_2 = Employee('Lucy', 'Verasamy', 70000)
emp_3 = Employee('Guido', 'Schneider', 190000)
emp_4 = Employee('Test', 'User', 70000)

emp_str_1 = 'Jason-Plato-120000'
emp_str_2 = 'Rob-Collard-230000'

new_emp_1 = Employee.from_string(emp_str_1)
new_emp_2 = Employee.from_string(emp_str_2)

emp_3.apply_raise()

new_emp_5 = Employee('Lewis', 'Hamilton', 1000000)
print(new_emp_5)

# print(emp_1.fullname(), 'earns', emp_1.pay, 'Email:', emp_1.email)
# print(emp_2.fullname(), 'earns', emp_2.pay, 'Email:', emp_2.email)
# print(emp_3.fullname(), 'earns', emp_3.pay, 'Email:', emp_3.email)

print('Number of employees =', Employee.num_employees)
print(new_emp_2.email, new_emp_2.pay)

my_date = datetime.date(2018, 7, 22)

# print(Employee.is_workday(my_date))

# dev1 = Developer('Fred', 'Titmus', 60000, 'Python')
# print(dev1.prog_lang, dev1.email)

# mgr1 = Manager('Lucy', 'Verasamy', 80000, [emp_1, emp_3])
# mgr1.add_emp(emp_2)
# print(mgr1.email)

# mgr1.remove_emp(emp_2)
# mgr1.list_emps()

# print(isinstance(mgr1, Developer))
# print(issubclass(Developer, Employee))
