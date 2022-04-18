#Write a function which accepts list as an argument and returns summation of all arguments

def list(a):
    sum = 0
    for i in a:
        sum = sum + i

    return sum

x = list([1,2,3,4,5,6,7,8])
print(x)

