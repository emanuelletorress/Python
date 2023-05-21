
class Employee:

    def __init__(self, first, last, pay): # initialize/constructor ~ self: the instance as the first argument
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
    
    def fullname(self):
        return f'{self.first} {self.last}'

emp_1 = Employee('Arch', 'Angelic', '8888') # emp_1 is passed as self
emp_2 = Employee('Meta', 'Angel', '8888')

print(emp_1.fullname()) # emp_1 gets automatically passed as self
print(Employee.fullname(emp_1)) # in this way you have to specify which instance the method is working with