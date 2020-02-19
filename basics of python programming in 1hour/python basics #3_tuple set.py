
# coding: utf-8

# In[8]:

# Mutable  modifiable
list_1 = ['History', 'Math', 'Physics', 'CompSci']
list_2 = list_1
print(list_1)
print(list_2)
list_1[0] = 'Art'
print(list_1)
print(list_2)
 
    #Immutable  loop thru and access...non modifiable
tuple_1 = ('History', 'Math', 'Physics', 'CompSci')
tuple_2 = tuple_1
print(tuple_1)
print(tuple_2)

'''
tuple_1[0] = 'Art'
print(tuple_1)
print(tuple_2)  operation doesnt happen immutable
'''

# Sets
cs_courses = {'History', 'Math', 'Physics', 'CompSci','Math'}
print(cs_courses)
art_courses = {'History', 'Math', 'art', 'chemistry'}
print(cs_courses.intersection(art_courses))
print(cs_courses.difference(art_courses))
print(cs_courses.union(art_courses))





# Empty Lists
empty_list = []
empty_list = list()

# Empty Tuples
empty_tuple = ()
empty_tuple = tuple()

# Empty Sets
empty_set = {} # This isn't right! It's a dict
empty_set = set()

'''
   OUTPUTS
   
['History', 'Math', 'Physics', 'CompSci']
['History', 'Math', 'Physics', 'CompSci']
['Art', 'Math', 'Physics', 'CompSci']
['Art', 'Math', 'Physics', 'CompSci']
('History', 'Math', 'Physics', 'CompSci')
('History', 'Math', 'Physics', 'CompSci')
{'CompSci', 'Physics', 'History', 'Math'}
{'History', 'Math'}
{'CompSci', 'Physics'}
{'CompSci', 'Physics', 'History', 'chemistry', 'art', 'Math'}

'''


