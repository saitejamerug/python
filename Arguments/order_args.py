# Order of args
# mandatory args, default args, arbitrary positional args, arbitrary keyword args
def chat(sender, receiver, app = "Whatsapp", *messages, **reactions):
    print("Sender : ", sender)
    print("Receiver : ", receiver)
    print("You're using app : ", app)
    for message in messages:
        print(message)
    for reaction, emoji in reactions.items():
        print("reaction : ", reaction,",", "Emoji : ", emoji)

chat("Sai", "Dhiraj", "Instagram", "Hi", "How are you?", laughing = ":)", sad = ":(")
