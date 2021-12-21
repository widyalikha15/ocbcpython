def my_function(p, l):
    '''Function to calculate area of a square'''
    print(p * l)


def printme( str_input ):
   '''This prints a passed string into this function'''
   print(str_input)

my_function(9, 2)
print(my_function.__doc__)

printme(100)
print(printme.__doc__)