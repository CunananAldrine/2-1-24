def decorator_func(decorated_func):
    def wrapper_func(*args, **kwargs):
        print(f'there are {len(args)} positional arguments and {len(kwargs)} keyword arguments')
        return decorated_func(*args, **kwargs)
        
    return wrapper_func

@decorator_func
def names_and_age(age1, age2, age3, name1='Lily', name2='Top' , name3='mingming'):
    return f'{name1} is {age1} yrs old, {name2} is {age2} yrs old, and {name3} is {age3} yrs old.'
    
print(names_and_age(4, 5, 6, name1="Lily", name2="top" , name3="mingming"))

