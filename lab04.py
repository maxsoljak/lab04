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
            b = input("Would you like to solve a math problem to feel better?")
            if b == "yes":
                equal = input("how much 2+2")
                if equal == 4:
                        print("Thats correct")
            elif b == "no":
                exit()
    elif y == "no":
        exit()