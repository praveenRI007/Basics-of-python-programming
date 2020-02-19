#import my_module as mm # mm is for simpler usage , we could use my_module directly
import sys
import random
import math

import datetime
import calendar
import os
#sys.path.append('module location')

from my_module import find_index as fi ,test

#from my_module import * ---->in order to import fn. as well as variables
#harder to track variables and fn. when using * for import
# in order to import a function from module
# from my_module import find_index , test ....for string too
# if u import only the function then no need for mm.find_index just the function itself

courses = ['math','history','physics','CS']

index = fi(courses,'physics')
print(index)
print(test)

#print(sys.path).... tells the path

random_course = random.choice(courses)
print(random_course)

rads= math.radians(90)
print(math.sin(rads))

today = datetime.date.today()
print(today)
print(calendar.isleap(2020)) #using library module calendar

print(os.getcwd())  #print current working directory

print(os.__file__)  

'''
  OUTPUTS

Imported my_module...
3
Test String
physics
1.0
2020-02-19
True
F:\python programming\importing module #8
C:\Users\Praveen RI\AppData\Local\Programs\Python\Python35\lib\os.py

'''





