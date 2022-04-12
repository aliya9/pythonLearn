#print numbers from 1to50 but skip printing numbers divisible by 5

for i in range(1,51):
    if i%5==0:
        continue
    print(i)