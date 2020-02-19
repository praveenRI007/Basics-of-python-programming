

nums = [1,2,3,4,5]

for num in nums:
    if num==3:
        print('found')
        break                  #comes out of loop 
    print(num)                 
    
print('\n')
    
for num in nums:
    if num==3:
        print('found')
        continue           #goes for next iteration of loop
    print(num)
    
print('\n')

for num in nums:
    for letter in'abc':
        print(num,letter)
        
        
print('\n')

for i in range(1,11):
    print(i)
    
print('\n')

x=0
while x<10 :
    if x==5:
        break
    print(x)
    x+=1

#while True:
#    print('1')  //prints infinite ones    press cntrl + C to interrrupt the process
 
    
'''
   OUTPUTS
   
   1
2
found


1
2
found
4
5


1 a
1 b
1 c
2 a
2 b
2 c
3 a
3 b
3 c
4 a
4 b
4 c
5 a
5 b
5 c


1
2
3
4
5
6
7
8
9
10


0
1
2
3
4

'''
    






