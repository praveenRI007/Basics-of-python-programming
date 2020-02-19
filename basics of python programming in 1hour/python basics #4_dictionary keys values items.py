
# coding: utf-8

# In[17]:

student = {'name':'john','age':24 ,'courses':['math','cs'] } #string integer list
print(student)
print(student['name']) #if phone is to be found then error arises 
print(student.get('name'))
print(student.get('phone','not found'))

student['phone'] = '555-5555'
student['name'] = 'jane'

print(student.get('phone','not found'))
print(student)

student.update({'name':'joe','age':'23','grade':'A'})
print(student)
del student['age']
print(student)
grade = student.pop('grade')
print(grade)
print(student)

print(len(student))
print(student.keys())
print(student.values())
print(student.items())

for key in student :
    print(key)

for key,value in student.items() :
    print(key,value)
    
    
'''
  OUTPUTS

{'courses': ['math', 'cs'], 'name': 'john', 'age': 24}
john
john
not found
555-5555
{'courses': ['math', 'cs'], 'name': 'jane', 'age': 24, 'phone': '555-5555'}
{'grade': 'A', 'name': 'joe', 'age': '23', 'courses': ['math', 'cs'], 'phone': '555-5555'}
{'grade': 'A', 'name': 'joe', 'courses': ['math', 'cs'], 'phone': '555-5555'}
A
{'name': 'joe', 'courses': ['math', 'cs'], 'phone': '555-5555'}
3
dict_keys(['name', 'courses', 'phone'])
dict_values(['joe', ['math', 'cs'], '555-5555'])
dict_items([('name', 'joe'), ('courses', ['math', 'cs']), ('phone', '555-5555')])
name
courses
phone
name joe
courses ['math', 'cs']
phone 555-5555


'''



