# Keywords and values stored in keys and values
def order_details(**kwargs):
    for key, value in kwargs.items():
        print(key,":", value)
order_details(is_bill_paid = False, order_id = 1011, bill = 234, name = "Dhiraj", status = "PickedUp", food = "Chicken Shawarma")

def display_tags(**kwargs):
    for key, value in kwargs.items():
        print(key,":", value)

display_tags(name = "Sai", age = "23")