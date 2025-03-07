#None - a Python constant representing the absence of a value
#like null
#if a return value for a function is not defined, None is returned by default
#None is a singleton object, only one instance of None exists in memory
#use is to check object identity with that specific None object
#must use == with a literal
def f():
    x = 2
print(f() is None)
print("" == None) #use is instead?


#list comprehensions to quickly build and modify lists


#(name,$-income)
customers = [("John", 240000), ("Alice", 120000),
             ("Ann", 1100000), ("Zach", 44000)]
#select high-value customers earning > $1M
whales = [x for x,y in customers if y > 1000000]
print(whales)

even_digits = [n for n in range(1,10) if n%2 == 0]
print(even_digits)

#__eq__()

#conditional execution of different code branches
n = int(input("Enter a number: "))

if n > 10:
    print("Greater than 10")
elif n == 10:
    print("Equal to 10")
else:
    print("Less than 10")

#loops: for repeated execution of code blocks 
#Python uses while and for loops
#loop variant
#for loop declaration
#loop variable i that iteratively takes on all values in the list
#keeps running untl it runs out of values
#for i in [0,1,2]:
    #print(i)
#while loop - same semantics
# executes while loop condition is met
#j = 0
#while (j < 3):
    #print(j)
    #j = j + 1

#loop condition for an infinite loop: ex) server awaiting and serving requests
# break or a condition that evaluates to False used for terminating loops
#a web server may csall break if it detects it is under attack, will then execute code immediately after
while True:
    break

#continue ends/skips current loop iteration and brings execution flow back to loop condition
#while True:
    #continue
    #print("Dead Code")

#functions for code reuse
#arguments can change the results of the function
#return keyword terminates the function and passes flow of execution
# to the caller of the function
# float return type: original investment + nominal interest
def appreciate(x, percentage):
    return x + x * percentage / 100

print(appreciate(10000,5))
