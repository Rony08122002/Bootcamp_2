#1
#class Currency:
#    def __init__(self, currency, amount):
#        self.currency = currency
#        self.amount = amount
#    def __str__(self):
#        return f"{self.amount} {self.currency}s"

#    def __repr__(self):
#        return f"{self.amount} {self.currency}s"

#    def __int__(self):
#        return self.amount

#    def __add__(self, other):
#        if isinstance(other, Currency):
#            if self.currency != other.currency:
#                raise TypeError(f"Cannot add between Currency type <{self.currency}> and <{other.currency}>")
#            return Currency(self.currency, self.amount + other.amount)
#        elif isinstance(other, int):
#            return Currency(self.currency, self.amount + other)
#        else:
#            raise TypeError("Unsupported type for addition")

#    def __iadd__(self, other):
#        if isinstance(other, Currency):
#            if self.currency != other.currency:
#                raise TypeError(f"Cannot add between Currency type <{self.currency}> and <{other.currency}>")
#            self.amount += other.amount
#        elif isinstance(other, int):
#            self.amount += other
#        else:
#            raise TypeError("Unsupported type for addition")
#        return self


#c1 = Currency('dollar', 5)
#c2 = Currency('dollar', 10)
#c3 = Currency('shekel', 1)
#c4 = Currency('shekel', 10)

#print(str(c1))
#print(int(c1))
#print(repr(c1))

#print(c1 + 5) 
#print(c1 + c2)

#c1 += 5
#print(c1)

#c1 += c2
#print(c1)

#try:
#    print(c1 + c3)
#except TypeError as e:
#    print(e)

#2
#3
#import string
#import random
#letters = string.ascii_letters
#random_string = ''.join(random.choices(letters, k=5))
#print(random_string)

#4
# import datetime
# current_date = datetime.date.today()
# def display_current_date():
#     current_date = datetime.date.today()
#     print("Today's date is:", current_date)
# import datetime

# def display_current_date():
#     current_date = datetime.date.today()
#     print("Today's date is:", current_date)
# display_current_date()

#5
# import datetime

# def time_until_january():
#     now = datetime.datetime.now()
#     next_year = now.year + 1 if now.month == 12 and now.day > 1 else now.year
#     january_first = datetime.datetime(next_year, 1, 1)
#     time_left = january_first - now
#     days = time_left.days
#     hours, remainder = divmod(time_left.seconds, 3600)
#     minutes, seconds = divmod(remainder, 60)
#     print(f"The 1st of January is in {days} days and {hours}:{minutes}:{seconds} hours.")

# time_until_january()

#6
# from datetime import datetime

# def minutes_lived(birthdate):
#     birth_date = datetime.strptime(birthdate, "%Y-%m-%d")
#     now = datetime.now()
#     time_lived = now - birth_date
#     minutes = time_lived.total_seconds() / 60
#     print(f"You have lived approximately {int(minutes):,} minutes.")
# birthdate = "2002-12-08"
# minutes_lived(birthdate)

#7

from faker import Faker
fake = Faker()
users = []
def add_fake_user():
    user = {
        "name": fake.name(),
        "address": fake.address(),
        "language_code": fake.language_code()
    }
    users.append(user)
for _ in range(5):
    add_fake_user()
for user in users:
    print(user)