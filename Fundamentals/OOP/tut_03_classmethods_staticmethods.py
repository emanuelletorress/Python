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

    # ~~~~~~~~~~~~ CLASS METHODS

    @classmethod # Decorator
    def set_raise_amount(cls, amount): # the class is the first argument
        cls.raise_amount = amount

    @classmethod 
    # a method that takes a string and splits it into three parts, and returns an object
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay) # returns a new class object
    
    # ~~~~~~~~~~~~ STATIC METHODS
    
    @staticmethod # it doesn't depend on a specific instance or class method
    def is_workday(day): # takes neither instance nor class as an argument
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


emp_1 = Employee('Arch', 'Angelic', 50000) # emp_1 is passed as self
emp_2 = Employee('Meta', 'Angel', 50000)

# we're changing the raise_amount value through this class method
Employee.set_raise_amount(1.05)
print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

emp_1_str = 'Mich-Ael-50000' # string with employee info
new_emp_1 = Employee.from_string(emp_1_str) # assigning the class object to new_emp_1
print(new_emp_1.email)
print(new_emp_1.pay)

