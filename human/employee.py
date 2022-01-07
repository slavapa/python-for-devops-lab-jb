import datetime
from person import Person

class Employee(Person):
    def __init__(self):
        Person.__init__(self)
        self.id = 25


person = Person(datetime.date.today())
emp = Employee(person)