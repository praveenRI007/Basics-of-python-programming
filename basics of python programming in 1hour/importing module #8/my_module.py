#this module is created separately so that it could be used for accessing functionsfor other modules
#save this module my_module in same directory as the main module accessing my_module is saved
print('Imported my_module...')

test = 'Test String'


def find_index(to_search, target):
    '''Find the index of a value in a sequence'''
    for i, value in enumerate(to_search,start =1 ):
        if value == target:
            return i

    return -1
