# Positional Arguments
def intro(name, city, hobby):
    print(f"My name is {name} I am from {city} and my hobby is {hobby}")

intro("Sai Teja Merugu", "Sangareddy", "Dancing\n")
intro("Dancing", "Sai Teja Merugu", "Sangareddy\n")

def subtract(a, b):
    return a - b

a = subtract(10, 3)
b = subtract(3, 10)

print(str(a - b) + "\n")

# Positional in positional arguments means the arguments are referenced based on its position follows an order

def bio(first_name, last_name, age):
    print(f"First name: {first_name}, Last name: {last_name}, Age: {age}\n")

bio("Sai Teja", "Merugu", 23)

'''
def nums(a, b):
    print(a, b)

nums(1, 2, 3)   # nums() takes 2 positional arguments but 3 were given
'''