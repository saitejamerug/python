def add(*args):
    print(args)
    sum = 0
    for arg in args:
        sum += arg
    print(sum)

add(10, 20, 30)
add(40, 60)

def multiply_all(*args):
    mul = 1
    for arg in args:
        mul *= arg
    return mul

print(multiply_all(20, 30, 40))
print(multiply_all(20, 30))
print(multiply_all(7, 8, 9, 10, 11))
def display_tags(**kwargs):
    for arg in kwargs:
        print(arg, kwargs[arg])

display_tags()