#How to Define a Class
""" class Dog:
    pass """
#Instantiate an Object in Python
""" class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age """

""" class Dog:
    # Class attribute
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age """

""" 

Dog()
buddy = Dog("Buddy", 9)
miles = Dog("Miles", 4) """

#Instance Methods
""" 
class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Instance method
    def description(self):
        return f"{self.name} is {self.age} years old"

    # Another instance method
    def speak(self, sound):
        return f"{self.name} says {sound}"

miles = Dog("Miles", 4)
buddy = Dog("Buddy", 1)
miles.description()



print(miles.description())
print(buddy.description())

print(miles.speak("Woof Woof"))
print(buddy.speak("Bow Wow")) """

#Inherit From Other Classes in Python
""" class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed

    # Instance method
    def description(self):
        return f"{self.name} is {self.age} years old"

    # Another instance method
    def speak(self, sound):
        return f"{self.name} says {sound}"

miles = Dog("Miles", 4, "Jack Russell Terrier")
buddy = Dog("Buddy", 9, "Dachshund")
jack = Dog("Jack", 3, "Bulldog")
jim = Dog("Jim", 5, "Bulldog")

class Buldogs(Dog):
    def speak(self):
        return f"{self.name} says Woof Woof"

class Dashshunds(Dog):
    def speak(self):
        return f"{self.name} says yap yap"

class JackRussel(Dog):
    pass

hike = Buldogs('hike', 9, 'bulldogs')
miles = JackRussel("miles", 4, 'jack')
dachs = Dashshunds('dach', 9, 'buldog')

print(hike.speak())
print(miles.speak("arf"))
print(dachs.speak())


print(1 + 1)
print('1' + '1')
print(hike + miles) """

'''
raka = ["Raka Ardhi", 28, "CurDev", 2265]
spock = ["Spock", 35, "Science Officer", 2254]
mccoy = ["Leonard McCoy", "Chief Medical Officer", 2266]
#0                       1                           2                       3
#["Raka Ardhi"              28                          Curdev                2265]
#["Spock"                   35                          Science Office        2254]
#["Leonard McCoy"           "Chief Medical Officer"     2266                      ]
print("Daftar Nama : ", raka[0], spock[0], mccoy[0])
print("Daftar Nama : ", raka[1], spock[1], mccoy[1])
print("Daftar jabatan : ", raka[2], spock[2], mccoy[2])
#print("Daftar tahun mulai : ", raka[3], spock[3], mccoy[3])
'''
## How to Define a Class
'''
class Dog:
    pass
'''
""" class Dog:
    # Class attribute
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age
##Instantiate an Object in Python
#Dog() --->Python raises a TypeError:

buddy = Dog("Buddy", 9)
miles = Dog("Miles", 4)
print(buddy.name)
print(buddy.age)
print(buddy.species) """

#Instance Methods
""" class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Instance method
    def description(self):
        return f"{self.name} is {self.age} years old"

    # Another instance method
    def speak(self, sound):
        return f"{self.name} says {sound}"

miles = Dog("Miles", 4)
print(miles.description())

print(miles.speak("Woof Woof"))
print(miles.speak("Bow Wow")) """

##Inherit From Other Classes in Python
#Dog Park Example
""" class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed

    # Instance method
    def description(self):
        return f"{self.name} is {self.age} years old"

    # Another instance method
    def speak(self, sound):
        return f"{self.name} says {sound}"

miles = Dog("Miles", 4, "Jack Russell Terrier")
buddy = Dog("Buddy", 9, "Dachshund")
jack = Dog("Jack", 3, "Bulldog")
jim = Dog("Jim", 5, "Bulldog")

print(buddy.speak("Yap"))
print(jim.speak("Woof")) """

#Parent Classes vs Child Classes
class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old"

    def speak(self, sound):
        return f"{self.name} says {sound}"

#Remember, to create a child class, you create new class with its own name and then put the name of the parent class in parentheses.
class JackRussellTerrier(Dog):
    pass

class Dachshund(Dog):
    pass

class Bulldog(Dog):
    pass

#With the child classes defined, you can now instantiate some dogs of specific breeds in the interactive window:
miles = JackRussellTerrier("Miles", 4)

buddy = Dachshund("Buddy", 9)
jack = Bulldog("Jack", 3)
jim = Bulldog("Jim", 5)

#Instances of child classes inherit all of the attributes and methods of the parent class:
print(miles.species)
print(buddy.name)
print(jack)
print(jim.speak("Woof"))

#Extend the Functionality of a Parent Class
class JackRussellTerrier(Dog):
    def speak(self, sound="Arf"):
        return f"{self.name} says {sound}"

miles = JackRussellTerrier("Miles", 4)
print (miles.speak())
print(miles.speak("Grrr"))


# Tambahan
class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed

    # Instance method
    def description(self):
        return f"{self.name} is {self.age} years old"

    # Another instance method
    def speak(self, sound):
        return f"{self.name} says {sound}"

miles = Dog("Miles", 4, "Jack Russell Terrier")
buddy = Dog("Buddy", 9, "Dachshund")
jack = Dog("Jack", 3, "Bulldog")
jim = Dog("Jim", 5, "Bulldog")

print(buddy.speak("Yap"))
print(jim.speak("Woof"))

#Parent Classes vs Child Classes
class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age,breed):
        self.name = name
        self.age = age
        self.breed = breed


    def description(self):
        return f"{self.name} is {self.age} years old"

    def speak(self, sound):
        return f"{self.name} says {sound}"

    def __repr__(self):
        return f"to create instance :: Dog(name = {self.name}, age = {self.age}, breed = {self.breed}"  #REPR
    def __str__(self):
        return f"clean info ::{self.name} is  {self.age} years old {self.breed}"  #STR
miles = Dog("Miles", 4, "Jack Russell Terrier")
#buddy = Dog("Buddy", 9, "Dachshund")
#jack = Dog("Jack", 3, "Bulldog")
#jim = Dog("Jim", 5, "Bulldog")

#sebelum __repr__or__str__ada
print(miles)

print(repr(miles))
print(miles.__repr__())

print(str(miles))
print(miles.__str__())



##tambahan
#parent class
class Dog:
    species = "Canis familiaris"
 
    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed
 
    # Instance method
    def description(self):
        return f"{self.name} is {self.age} years old"
 
    # Another instance method
    def speak(self, sound):
        return f"{self.name} says {sound}"
 
    def __repr__(self):
        return f"to create instance :: Dog( name={self.name}, age={self.age}, breed={self.breed} ) #REPR"
 
    def __str__(self):
        return f"clean info :: {self.name} is {self.age} years old {self.breed}  #STR"
 
       
class Bulldogs(Dog):
 
    def __init__(self, name, age, breed, weight_in_lbs):
        self.name = name
        self.age = age
        self.breed = breed
        self.weight_in_lbs = weight_in_lbs
 
    # Another instance method
    def speak(self):
        return f"{self.name} says Woof Woof"
 
    def __add__(self,other):
        return(self.weight_in_lbs + other.weight_in_lbs)
 
scooby = Bulldogs('Scooby', 2, 'Bulldogs', 15)
scooby_jr = Bulldogs('Scooby JR', 1, 'Bulldogs', 8)
print("Scooby : ", scooby.weight_in_lbs)
print("Scooby JR : ", scooby_jr.weight_in_lbs)