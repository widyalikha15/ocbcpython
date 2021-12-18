#Integers
print(123123123123123123123123123123123123123123123123 + 1)

# Python interprets a sequence of decimal digits without any prefix to be a decimal number:

print(10)
print(type(10))

#Floating-Point Numbers
print(4.2)
print(type(4.2))

print(4.)

print(.2)

print(.4e7)

print(4.2e-4)

#Strings
print("Hacktiv8")
print(type("Hacktiv8"))

#Boolean Type, Boolean Context, and “Truthiness”
print(type(True))

print(type(False))

#Variable Assignment
n = 300
print(n)
n
    # Later, if you change the value of n and use it again, the new value will be substituted instead:
n = 1000
print(n)

n
    #Python also allows chained assignment, which makes it possible to assign the same value to several variables simultaneously:
a = b = c = 300
print(a, b, c)

#Variable Types in Python
var = 23.5
print(var)

var = "Now I'm a string"
print(var)

#Variable Names
name = "Hacktiv8"
Age = 54
has_laptops = True
print(name, Age, has_laptops)
    #Note that case is significant.
age = 1
Age = 2
aGe = 3
AGE = 4
a_g_e = 5
_age = 6
age_ = 7
_AGE_ = 8

print(age, Age, aGe, AGE, a_g_e, _age, age_, _AGE_)

#Operators and Expressions in Python
a = 10
b = 20
a + b

    #In this case, the + operator adds the operands a and b together. An operand can be either a literal value or a variable that references an object:
a = 10
b = 20
a + b - 5

#String Manipulation
    # + Operators
s = 'foo'
t = 'bar'
u = 'baz'

print(s + t)

print(s + t + u)


print('Hacktiv8 ' + 'Inalum')

    # * Operators

s = 'foo.'

s * 4

    # in Operators

s = 'foo'

print(s in 'That food for us')

print(s in 'That good for us')

    # Case Conversion
s = 'HackTIV8'

    # Capitalize
print(s.capitalize())

    # Lower
print(s.lower())

    # Swapcase
print(s.swapcase())

    # Title
print(s.title())

    # Uppercase
print(s.upper())

#Python Lists

a = ['foo', 'bar', 'baz', 'qux']

print(a)

#Python Tuples
t = ('foo', 'bar', 'baz', 'qux', 'quux', 'corge')

print(t)

print(t[0])

print(t[-1])
    # packing and unpacking

(s1, s2, s3, s4) = ('foo', 'bar', 'baz', 'qux')

s1

#Defining a Dictionary
MLB_team = {
    'Colorado': 'Rockies',
    'Boston': 'Red Sox',
    'Minnesota': 'Twins',
    'Milwaukee': 'Brewers',
    'Seattle': 'Mariners'
}

#Accessing Dictionary Values

print(MLB_team['Minnesota'])
print(MLB_team['Colorado'])

    # error
    # MLB_team['Toronto']

    #Adding an entry to an existing dictionary is simply a matter of assigning a new key and value:
MLB_team['Kansas City'] = 'Royals'
MLB_team

    # If you want to update an entry, you can just assign a new value to an existing key:
MLB_team['Seattle'] = 'Seahawks'
MLB_team

    # To delete an entry, use the del statement, specifying the key to delete:
del MLB_team['Seattle']
MLB_team

#Building a Dictionary Incrementally
person = {}
type(person)
 
person['fname'] = 'Hack'
person['lname'] = 'Inalum'
person['age'] = 51
person['spouse'] = 'Edna'
person['children'] = ['Ralph', 'Betty', 'Joey']
person['pets'] = {'dog': 'Fido', 'cat': 'Sox'}

person

print(person['fname'])
print(person['lname'])

print(person['children'])
print(person['children'][1])

print(person['pets'])
print(person['pets']['cat'])

    # Built-in Methods
d = {'a': 10, 'b': 20, 'c': 30}

    # items
print(d.items())

    # keys
print(d.keys())

    # values
print(d.values())

#Python Statements

print('Hello, World!')

x = [1, 2, 3]
print(x)

#Line Continuation
person1_age = 42
person2_age = 16
person3_age = 71

someone_is_of_working_age = (person1_age >= 18 and person1_age <= 65) or (person2_age >= 18 and person2_age <= 65) or (person3_age >= 18 and person3_age <= 65)
someone_is_of_working_age


someone_is_of_working_age = (
    (person1_age >= 18 and person1_age <= 65)
    or (person2_age >= 18 and person2_age <= 65)
    or (person3_age >= 18 and person3_age <= 65)
)

someone_is_of_working_age

