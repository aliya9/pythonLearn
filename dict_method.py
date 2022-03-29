
d1={1:"One",2:"Two",3:"Three",4:"Four",5:"Five"}

#keys

x=d1.keys()
print(x)

#values

y=d1.values()
print(y)

#items

print(d1.items())

#update (2 methods)

d1.update({5:"Five",6:"Six"})
print(d1)

d1[5]="Five"
print(d1)


#get (2 methods)

a=d1.get(5)
print(a)
