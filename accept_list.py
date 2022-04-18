def even(a):
    l2=[]
    for i in a:
        if i%2 == 0:
            l2.append(i)
    return l2


l1 = []
i=1

n = int(input("How many numbers you want to check: "))

while i <= n:
    num = int(input("Enter number: "))
    l1.append(num)
    i += 1

print(l1)
x = even(l1)
print("Even numbers are: ",x)



