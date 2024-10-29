## Data
txt = ['lambda functions are anonymous functions.',
'anonymous functions dont have a name.',
'functions are objects in Python.']
## One-Liner
def map_implementation():
    mark = map(lambda s: (True, s) if 'anonymous' in s else (False, s), txt)
    
def comprehen_implementation():
    mark = [(True, s) if 'anonymous' in s else (False, s) for s in txt]
    return mark
## Result
print(comprehen_implementation())