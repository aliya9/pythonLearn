
def msg(a,b):
    if b == 18:
        print("I am "+a+" and I need to take driving test")

    elif b < 18:
        print("I am "+a+" and I can't drive")

    elif b > 18:
        print("I am "+a+" and I can drive")


a=input("Enter name: ")
b=int(input("Enter your age: "))

msg(a,b)

