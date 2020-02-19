


def hello_func():
    pass   #not using the function ,doesnt show error while executing

print(hello_func)
print(hello_func())

def bello_func():
    print('hello')
    
print(bello_func())
bello_func()


def world(greetings,name = 'you'):
    return '{},{}'.format(greetings,name)

print(world('hi',name ='praveen').upper())

def student_info(*args,**kwargs):
    print(args)
    print(kwargs)
    
courses = ['arts','maths','history']
info = { 'name':'praveen','age':21}

student_info(*courses, **info)               # * unpacks for a list ,** unpacks for a dictionary


# Number of days per month. First value placeholder for indexing purposes.
month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def is_leap(year):
    """Return True for leap years, False for non-leap years."""

    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def days_in_month(year, month):
    """Return number of days in that month in that year."""

    # year 2017
    # month 2
    if not 1 <= month <= 12:
        return 'Invalid Month'

    if month == 2 and is_leap(year):
        return 29

    return month_days[month]

print(days_in_month(2017, 2))


'''
  OUTPUTS

None
hello
None
hello
HI,PRAVEEN
('arts', 'maths', 'history')
{'name': 'praveen', 'age': 21}
28

'''






