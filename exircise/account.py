# http://hplgit.github.io/primer.html/doc/pub/class/._class-readable002.html

class Account(object):
    def __init__(self, name, account_number, initial_amount):
        self.__name = name
        self.__no = account_number
        self.__balance = initial_amount

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        self.__balance -= amount

    def dump(self):
        s = '%s, %s, balance: %s' % \
            (self.__name, self.__no, self.__balance)
        print(s)
