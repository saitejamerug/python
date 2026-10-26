# Keyword Arguments
def trip_details(driver_name, pickup, drop, total_fair):
    print(f"Driver name: {driver_name}")
    print(f"Pickup: {pickup}")
    print(f"Drop: {drop}")
    print(f"Total fair: {total_fair}")

trip_details(drop="Kathmandu",  total_fair=100000, pickup="JNTUH", driver_name="Diraj")

def send_email(to, subject, body):
    print(f"to: {to}")
    print(f"subject: {subject}")
    print(f"body: {body}\n")

send_email(to="CVCORP", subject="For Leave", body="Requesting for a 3 day leave because my health is in bad condition.")
send_email(body="Requesting for a 3 day leave because my health is in bad condition.", to="CVCORP", subject="For Leave")

def create_profile(username, email, age):
    print(f"username: {username}")
    print(f"email: {email}")
    print(f"age: {age}\n")

create_profile(age=23, username="msaiteja", email="msaiteja082@gmail.com")

'''
def food_delivery(restaurant, order_status):
    print(f"restaurant: {restaurant}, order_status: {order_status}")

food_delivery(restaurant="Mehfil", "Delivered")     # SyntaxError: positional argument follows keyword argument
'''
def book_ticket(name, From, To, no_tickets):
    print(f"Passenger name: {name}")
    print(f"From: {From}")
    print(f"To: {To}")
    print(f"No_tickets: {no_tickets}\n")

book_ticket(name="Alice", From="Delhi", To="Mumbai", no_tickets=2)

'''
Keyword arguments enables readability because it gives an understanding of for which parameter the argument is associated
'''
def PG(PG_name, room_no, no_sharing, price):
    print(f"PG_name: {PG_name}")
    print(f"room_no: {room_no}")
    print(f"no_sharing: {no_sharing}")
    print(f"price: {price}")

PG(price = 6000, no_sharing = 1, room_no = 1, PG_name = "Prasanna")