#effective code, concise, boosting speed of implementation

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

#list comprehensions create new lists in a concise and readble way
#[expression + context], context = which elements to select
#expression defines how to modify each list element before adding the result to the list

#expression doubles values selected in the context
some_doubles = [x*2 for x in range(3)]
print(some_doubles)