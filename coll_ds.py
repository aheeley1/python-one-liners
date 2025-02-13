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
