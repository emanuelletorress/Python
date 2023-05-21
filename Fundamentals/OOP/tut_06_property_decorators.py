class Employee:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    @property
    def email(self):
        return f'{self.first}.{self.last}@email.com'

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

emp_1 = Employee('Arch', 'Angelic', 50000)
emp_2 = Employee('Meta', 'Angel', 50000)

print(emp_1.email)
print(emp_1.fullname)
print('~~~~~~~~')
emp_1.fullname = 'FKA Twigs'
print(emp_1.fullname)