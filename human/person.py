import datetime

class Person:
    def __init__(self, birth=None):
        self.name = "Slava" or None
        self.age = 12 or None
        self.birth = datetime.date(1971, 2, 13)
        self.id = 1234

    def get_age(self, date):
        #date_string = "2012-12-12 10:10:10"
        #dt = datetime.fromisoformat(date_string)
        #today = datetime.date.today()
        calculate = date - self.birth
        return calculate

# Declaring my Object


#person = Person(datetime.date.today())
#print(person.get_age(datetime.date.today()))

#today = datetime.date.today()
#print(today)
