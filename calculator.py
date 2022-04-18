#create calculator for 3 numbers

def addition(a,b,c):
    return a+b+c

def substraction(a,b,c):
    return a-b-c

def multiply(a,b,c):
    return a*b*c

def division(a,b):
    return a/b

def cube(a):
    return a **3

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
z = int(input("Enter third number: "))

c = addition(x,y,z)
print("Addition= "+str(c))
print("Cube= "+str(cube(c)))

d = substraction(x,y,z)
print("Substraction= "+str(d))
print("Cube= "+str(cube(d)))

e = multiply(x,y,z)
print("Multiplication= "+str(e))
print("Cube= "+str(cube(e)))

f = division(x,y)
print("Division= "+str(f))
print("Cube= "+str(cube(f)))


