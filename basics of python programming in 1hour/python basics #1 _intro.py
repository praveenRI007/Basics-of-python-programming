#introduction to python and string operations

message = 'hello world'
print (message)                                      
print(message.upper())
print(message[0])
print(message[0].upper())
print(message[0:])
print(message[:3])
print(message[:])
print(message.count('ello'))
print(message.count('l'))
print(message.find('l'))
new_msg = message.replace('world','universe')
print(new_msg)
new_msg1 = 'is awesome'
new_msg = message + ',' + new_msg1
print(new_msg)
new_msg = '{},{} welcome'.format(message,new_msg1)
print(new_msg)
#new_msg = f'{message},{new_msg1.upper()} welcome' # f strings
print(dir(message)) #function that can be used 
print(help(str)) #string related info 
print(help(str.upper)) #gives the format for function

'''
   OUTPUTS

hello world
HELLO WORLD
h
H
hello world
hel
hello world
1
3
2
hello universe
hello world,is awesome
hello world,is awesome welcome

'''


