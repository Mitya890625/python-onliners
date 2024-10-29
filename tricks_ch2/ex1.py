employees = {'Alice' : 100000,
    'Bob' : 99817,
    'Carol' : 122908,
    'Frank' : 88123,
    'Eve' : 93121}


def retrive_old():
    top_earners = []
    for key, val in employees.items():
        if val >= 100000:
            top_earners.append((key,val))
    print(top_earners)
    
def retrieve_comprehensions():
    top_earners = [(k,v) for k,v in employees.items() if v >= 100000]
    print(top_earners)
    
    
retrieve_comprehensions()