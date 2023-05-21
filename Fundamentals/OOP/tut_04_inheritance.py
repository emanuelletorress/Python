
class Employee:
    
    raise_amount = 1.04

    def __init__(self, first, last, pay): # initialize/constructor ~ self: the instance as the first argument
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
    
    def fullname(self):
        return f'{self.first} {self.last}'
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

class Developer(Employee):
    # Python looks into the developer class; if it has no methods or attributes,
    # it then looks into its Parent class ~ this chain of inheritance is called
    # a Method resolution order
    raise_amount = 1.1

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang

class Manager(Employee):
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees == None:
            self.employees = []
        else:
            self.employees = employees
    
    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)
    
    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.fullname())


dev_1 = Developer('Arch', 'Angelic', 50000, 'Python') 
dev_2 = Developer('Meta', 'Angel', 50000, 'Java')

mgr_1 = Manager('Lilith', 'Matus', 90000, [dev_1])

print(mgr_1.email)
mgr_1.add_emp(dev_2)
mgr_1.print_emps()

print('After')
mgr_1.remove_emp(dev_2)
mgr_1.print_emps()

# Method resolution order
# print(help(Developer))

# Checks whether an object is an instance of a class
print('IS INSTANCE')
print(isinstance(mgr_1, Manager)) # True
print(isinstance(mgr_1, Employee)) # True
print(isinstance(mgr_1, Developer)) # False

# Checks whether a class is a subclass of another
print('IS SUBCLASS')
print(issubclass(Manager, Employee)) # True
print(issubclass(Developer, Employee)) # True
print(issubclass(Manager, Developer)) # False
