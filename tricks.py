#trick: a way of accomplising a task in a surprisingly fast or easy manner
#effective code using Python functionality, concise, boosting speed of implementation
#quick and easy adoption, enhancing coding productivity

#output: a list of tuples of employees and salary if salary > 100000
def get_high_earners_1():
    employees = {'Alice':100000, 
                 'Bob': 99817,
                 'Carol': 122908,
                 'Frank': 88123,
                 'Eve': 93121}

    top_earners = []

    for k,v in employees.items():
        if v >= 100000:
            top_earners.append((k,v))

    return top_earners

he = get_high_earners_1()
print(he)

#list comprehensions create new lists in a concise, efficient, powerful and readble way
#all things being equal, a shorter solution with less lines can be more readable
#[expression + context], 
#context = which elements to select
#context can consist of one or many variables defines using one or many for loops
#the context can be restricted by using if statements
#expression defines how to modify each list element before adding the result to the list

#expression doubles values generated in the context
some_doubles = [x*2 for x in range(3)]
print(some_doubles)

#expression: identity function (does not change the context variable x)
#context: variable takes all the values returned by the range function
lst1 = [x for x in range(5)]
print(lst1)

#expression: create a new tuple from the context variables x and y
#context variable x iterates over all values returned by range function
#context variable y iterates over all values returned by range function
#the two for loops are nested
#context variable y repeats its iteration procedure for every single value of the context variable x
#thus 3x3=9 combinations of context variables
lot = [(x,y) for x in range(3) for y in range(3)]
print(lot)

#expression: square function of the context variable x
#context: context variable x iterates over all values returned by range function
#but only if they are off values
odd_squares = [x**2 for x in range(10) if x % 2 > 0]
print(odd_squares)