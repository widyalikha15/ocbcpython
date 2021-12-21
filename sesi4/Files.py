#https://raw.githubusercontent.com/ardhiraka/PFDS_sources/master/Hack8_Sample_Text.txt
file = open('Hack8_Sample_Text.txt')



file.close()



try:
   f = open("Hack8_Sample_Text.txt", encoding = 'utf-8')
   # perform file operations
finally:
   f.close()



open('abc.txt')

open('abc.txt', 'r')

open('abc.txt', 'w')



open('abc.txt', 'rb')

open('abc.txt', 'wb')



with open("sample.txt",'w',encoding = 'utf-8') as f:
   f.write("my first file\n")
   f.write("This file\n\n")
   f.write("contains three lines\n")



f = open("sample.txt",'r',encoding = 'utf-8')

f.read(4) # read the first 4 data

f.read(4)    # read the next 4 data

f.read()     # read in the rest till end of file

f.read()  # further reading returns empty sting



f.tell()    # get the current file position

f.seek(0)   # bring file cursor to initial position

print(f.read())  # read the entire file



f.seek(0)   # bring file cursor to initial position
for line in f:
  print(line, end = '')



f.seek(0)
f.readline()



with open('sample.txt', 'r') as reader:
     # Read & print the entire file
     print(reader.read())


#Exception
x = 10
if x > 5:
    raise Exception('x should not exceed 5. The value of x was: {}'.format(x))



x = 10
if x > 5:
    raise Exception('your custom exception')


import sys
assert ('linux' in sys.platform), "This code runs on Linux only."
assert ('windows' in sys.platform), "This code runs on Windows only."



def os_interaction():
    assert ('linux' in sys.platform), "Function can only run on Linux systems."
    assert ('windows' in sys.platform), "This code runs on Windows only."
    print('Doing something.')



try:
    os_interaction()
except:
    pass



try:
    os_interaction()
except:
    print('Windows function was not executed')



try:
    os_interaction()
except AssertionError as error:
    print(error)
    print('The os_interaction() function was not executed')



# Here’s another example where you open a file and use a built-in exception:

try:
    with open('file.log') as file:
        read_data = file.read()
except:
    print('Could not open file.log')



try:
    with open('file.log') as file:
        read_data = file.read()
except FileNotFoundError as fnf_error:
    print(fnf_error)



try:
    os_interaction()
    with open('file.log') as file:
        read_data = file.read()
except FileNotFoundError as fnf_error:
    print(fnf_error)
except AssertionError as error:
    print(error)
    print('os_interaction() function was not executed')



try:
    os_interaction()
except AssertionError as error:
    print(error)
else:
    print('Executing the else clause.')



try:
    os_interaction()
except AssertionError as error:
    print(error)
else:
    try:
        with open('file.log') as file:
            read_data = file.read()
    except FileNotFoundError as fnf_error:
        print(fnf_error)



# Have a look at the following example:

try:
    os_interaction()
except AssertionError as error:
    print(error)
else:
    try:
        with open('file.log') as file:
            read_data = file.read()
    except FileNotFoundError as fnf_error:
        print(fnf_error)
finally:
    print('Cleaning up, irrespective of any exceptions.')



