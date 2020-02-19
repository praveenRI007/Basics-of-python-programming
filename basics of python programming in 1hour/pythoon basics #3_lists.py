


# lists tuples sets

#LISTS
courses = ['history','maths','cS','physics']
courses1 = ['history','maths','cS','physics']

print(courses)
print(courses[0])
print(courses[-1])
print(courses[0:2])
courses.append('art')
print(courses)
courses.insert(1,'biology')
print(courses)

courses2 =['art','education']
courses1.insert(0,courses2)
print(courses1)
print(courses)
print(courses[0])
courses.extend(courses2) #list size is extended
print(courses)
courses.remove('maths')
courses.remove('art')

print(courses)
popped=courses.pop()
print(popped)
print(courses)

courses.reverse()
print(courses)


#sort

courses.sort()
print(courses)

num  = [1,4,2,6,3,5,7,20]
num.sort()
print(num)
num.sort(reverse=True)
print(num)

sorted_courses = sorted(courses)
print(sorted_courses)

print(min(num))  # min / max  
print(sum(num))

print(courses.index('art'))
print('art' in courses)


# for loop

for item in courses:
    print(item)
    
for index,course in enumerate(courses,start=1):
    print(index,course)
    

#string version of courses

course_str = ','.join(courses)
print(course_str)
course_str = '-'.join(courses)
print(course_str)

new_list = course_str.split('-')
print(new_list)

'''
['history', 'maths', 'cS', 'physics']
history
physics
['history', 'maths']
['history', 'maths', 'cS', 'physics', 'art']
['history', 'biology', 'maths', 'cS', 'physics', 'art']
['history', 'biology', 'maths', 'cS', 'physics', 'art']
history
['history', 'biology', 'maths', 'cS', 'physics', 'art', 'art', 'education']
['history', 'biology', 'cS', 'physics', 'art', 'education']
education
['history', 'biology', 'cS', 'physics', 'art']
['art', 'physics', 'cS', 'biology', 'history']
['art', 'biology', 'cS', 'history', 'physics']
[1, 2, 3, 4, 5, 6, 7, 20]
[20, 7, 6, 5, 4, 3, 2, 1]
['art', 'biology', 'cS', 'history', 'physics']
1
48
0
True
art
biology
cS
history
physics
1 art
2 biology
3 cS
4 history
5 physics
art,biology,cS,history,physics
art-biology-cS-history-physics
['art', 'biology', 'cS', 'history', 'physics']
    
'''



