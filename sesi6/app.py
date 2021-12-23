'''
# Using Generators
def my_generator():
  print("Inside my generator")
  yield 'a'
  yield 'b'
  yield 'c'
my_generator()
print(my_generator())
# <generator object my_generator at 0x0000024C7BE129E0>
print(list(my_generator()))
#additional / sisipan tentang konversi
aa = '100'
int_aa = int(aa)
print(int_aa)
# function -->
def square(nums):
    result = []
 
    for num in nums:
        result.append(num * num)
 
    return result
 
 
nums = [1,2,3,4,5]
print(square(nums) )
    
# --> Generator
def square(nums):
    for num in nums:
        yield num * num
  
nums = [1,2,3,4,5].__iter__()
print(square(nums))
print(square(nums).__next__())
print(next(square(nums)))
print(next(square(nums)))
print(next(square(nums)))
print(next(square(nums)))
print(next(square(nums))) # error
# --> Generator
def square(nums):
    for num in nums:
        yield (num * num)
  
nums = [1,2,3,4,5].__iter__()
print(square(nums))
squared_generator = square(nums)
for num in squared_generator:
    #print(next(square(nums)))
    print(num)
    
# List Comprehension:
squared_nums = [y * y for y in [1, 2, 3, 4, 5]]
            
                # 1 * 1 = 1
                # 2 * 2 = 4
                # 3 * 3 = 9
                # 4 * 4 = 16
                # 5 * 5 = 25
                          
print(squared_nums)
squared_nums = [y + y for y in [1, 2, 3, 4, 5]]
squared_nums = [y * y for y in [1, 2, 3, 4, 5]]
squared_nums = [y + 4 for y in range(7) ]
print(squared_nums)
'''

'''
def my_generator():
  print("Inside my generator")
  yield 'a'
  yield 'b'
  yield 'c'
#my_generator()
#print(list(my_generator()))
#for char in my_generator():
#    print(char)
store_generator = my_generator()
print(next(store_generator))
print(next(store_generator))
print(next(store_generator))
def counter_generator(low, high):
    while low <= high:
       yield low
       low += 1
for i in counter_generator(5,10):
  print(i, end=' ')
'''

'''
def infinite_sequence():
    num = 0
    while True:
        yield num
        num += 1
for i in infinite_sequence():
      print(i, end=" ")
'''

'''
# #List comprhension  to creating generator by/using expression :
squared_nums = [y * y for y in [1,2,3,4,5] ]    # [1, 4, 9, 16, 25]
squared_nums = (y * y for y in [1,2,3,4,5] )
print(squared_nums)
print( next(squared_nums) )
print( next(squared_nums) )
print( next(squared_nums) )
print( next(squared_nums) )
print( next(squared_nums) )
# Function
def add_one(number):
    return number + 1
print(add_one(2))
print(add_one(12))
print(add_one(0))
print(add_one(0))
print(add_one(-9))
##First-Class Objects
def say_hello(name): # 3 say _hello("Bob")
    # say_hello("Bob")
    return f"Hello {name}" # 4 Hello Bob
            #Hello Bob
def be_awesome(name):
    return f"Yo {name}, together we are the awesomest!"
def greet_bob(greeter_func): # 1 greet_bob(say_hello)
    # greet_bob(say_hello)
    return greeter_func("Bob") # 2 say_hello("Bob") # 5 return
        # say_hello("Bob")  <--- function call / pemanggilan fungsi
print(greet_bob(say_hello))
# atau tampung di variable a kalau mau nge print-hasil
a = greet_bob(say_hello)
print(a)
print(greet_bob(be_awesome))
# atau tampung di variabel b jika ingin nge print hasil nya
b = greet_bob(be_awesome)
print(b)
'''

##Inner Functions
def parent():
    print("Printing from the parent() function") # 1

    def first_child(): #6
        print("Printing from the first_child() function") #7

    def second_child(): #3
        print("Printing from the second_child() function\n") #4

    second_child() #2
    first_child() #5
parent()


## Returning Functions From Functions
def parent(num): #2
    def first_child():
        return "Hi, I am Emma"

    def second_child():
        return "Call me Liam"

    if num == 1: #3
        return first_child #4
    else:
        return second_child

first = parent(1) #1 # 5 first = first_child
first() # 6 first_child()
print(first())


#Simple Decorators
def my_decorator(func): #2 my_decorator(say_whee)
    def wrapper(): #5
        print("Something is happening before the function is called.")#6
        func() # 7 say_whee() #selesai lanjut ke 9
        print("Something is happening after the function is called.") #10
    return wrapper #3 wrapper
def say_whee(): #8
    print("Whee!") #9

say_whee = my_decorator(say_whee) #1 ..selesai say_whee = print(Whee!)

say_whee() #4


#Instead, Python allows you to use decorators in a simpler way with the @ symbol, sometimes called the “pie” syntax
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper
 
@my_decorator
def say_whee():
    print("Whee!")
 
@my_decorator
def say_whee2():
    print("Whee! Whee!")
# manggil fungsi 
say_whee()
say_whee2()


## More Example
import functools
def decorator(func):
    @functools.wraps(func)
    def wrapper_decorator(*args, **kwargs):
        # Do something before
        value = func(*args, **kwargs)
        # Do something after
        return value
    return wrapper_decorator


#===================#
import functools
import time

def timer(func):
    """Print the runtime of the decorated function"""
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()    # 1
        value = func(*args, **kwargs)
        end_time = time.perf_counter()      # 2
        run_time = end_time - start_time    # 3
        print(f"Finished {func.__name__!r} in {run_time:.4f} secs")
        return value
    return wrapper_timer

@timer
def waste_some_time(num_times):
    for _ in range(num_times):
        sum([i**2 for i in range(10000)])

waste_some_time(1)
waste_some_time(999)