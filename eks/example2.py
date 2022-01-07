import datetime
from app import app
from human.person import Person

myapp = app.App()

person = Person('2000-10-01')
print(person.name)

today = datetime.date.today()

print(person.get_age(today))


