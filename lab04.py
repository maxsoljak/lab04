print("Hello world")

x = input("How are you today")

if x == "good":
    print("Thats awesome")
elif x == "bad":
    print("Oh no whats wrong")
    y = input("Can I help you somehow?")
    if y == "yes":
        a = input("How can I help you?")
        if a == "i dont know":
            print("Thats okay, sometimes we dont know what is really wrong")
    elif y == "no":
        exit()