

if True :
   print('condition was true')
language = 'python'

if language == 'java':
   print('language is java')
elif language =='python':
   print('language is python')
else :
   print('no match')
 

# and or not  

user = 'admin'
logged_in = True



#and

if user == 'admin' and logged_in:
   print('admin page')
else:
   print('bad credits')


#or

if user == 'admin' or logged_in:
   print('admin page')
else:
   print('bad credits')

#not 
   
logged_in = False

if not logged_in:
   print('please login')
else:
   print('welcome')
   
a=[1,2,3]
b=a

print(id(a))
print(id(b))
print(a is b)
print(a == b)
print(id(a)==id(b))

condition = None

if condition:
   print('evaluated to true')
else :
   print('evaluated to false')

condition = 0

if condition:
   print('evaluated to true')
else :
   print('evaluated to false')

condition = []

if condition:
   print('evaluated to true')
else :
   print('evaluated to false')
   
condition = 10

if condition:
   print('evaluated to true')
else :
   print('evaluated to false')
   
   
condition = {}

if condition:
   print('evaluated to true')
else :
   print('evaluated to false') #empty value correspond to false 



   ''' OUTPUT
condition was true
language is python
admin page
admin page
please login
2079305220808
2079305220808
True
True
True
evaluated to false
evaluated to false
evaluated to false
evaluated to true
evaluated to false
'''


