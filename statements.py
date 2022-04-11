#Make LIST of numbers which are divisible by 8 and 7 in range 50 to 1000

list = []

for i in range(50,1001):
    if i%8 == 0 and i%7 == 0:
        list.append(i)
print(list)
