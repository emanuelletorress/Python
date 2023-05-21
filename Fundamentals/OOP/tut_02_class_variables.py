# Class variables are shared between all employees of a class

class Employee:

    num_of_emps = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay): # initialize/constructor ~ self: the instance as the first argument
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

        Employee.num_of_emps += 1
    
    def fullname(self):
        return f'{self.first} {self.last}'
    
    def apply_raise(self):
        self.pay = int(float(self.pay) * self.raise_amount)

emp_1 = Employee('Arch', 'Angelic', '50000') # emp_1 is passed as self
emp_2 = Employee('Meta', 'Angel', '50000')

""" print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay) """

# when we access raise_amount, it first checks if the instance contains that attribute;
# then, it checks whether the class contains the attribute
print(Employee.raise_amount)
# ~ in the following cases, since the instance doesn't have the attribute, they're accessing the class's attribute
print(emp_1.raise_amount)
print(emp_2.raise_amount)

# Updating the class's raise amount
Employee.raise_amount = 1.05
print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

# emp_1 before raise_amount assignment
print(emp_1.__dict__)

# This assignment creates raise_amount inside emp_1
emp_1.raise_amount = 1.04

# emp_1 after raise_amount assignment
print(emp_1.__dict__)

print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)
