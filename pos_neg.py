i = 0
l1 = [-10, -8, 5, 34, 3, 8, -9, -67]
pos = 0
neg = 0

while i < len(l1):

    if l1[i] > 0:
        pos += 1


    else:
        neg += 1

    i += 1


print("Positive numbers: " + str(pos))
print("Negative numbers: " + str(neg))
