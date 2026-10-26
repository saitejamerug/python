# default args provides flexibility to the user
def greeting(age, name = "User"):
    print("Hello, " + name)
    if age >= 18:
        print("You are eligible to vote\n")
    else:
        print("You are not eligible to vote\n")

greeting(20)

def power(base, exponent = 2):
    return base ** exponent

print(power(2))
print(str(power(2, 3)) + "\n")

def connect(host, port = 3306, protocol = "TCP"):
    print("host :", host)
    print("port :", port)
    print(f"protocol : {protocol}\n")

connect("localhost")
connect("localhost", port = 2256)
connect("ABC", protocol = "HTTP")

# positional parameters followed by default parameters

def discount_price(price, discount = 10):
    discount_amount = (discount / 100) * price
    return discount_amount

print(discount_price(100))

# To provide flexibility for the user and run programs without exceptions