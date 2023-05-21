
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
        self.pay = int(self.pay * self.raise_amount)

    def __repr__(self): # an unambiguous rep of an object, meant for debugging
        return f"Employee('{self.first}', '{self.last}', {self.pay})"

    def __str__(self): # readable rep of an object
        return f'{self.fullname()} - {self.email}'
    
    # Emulating numeric types / Operator overload
    def __add__(self, other):
        return self.pay + other.pay

emp_1 = Employee('Arch', 'Angelic', 50000) # emp_1 is passed as self
emp_2 = Employee('Meta', 'Angel', 50000)