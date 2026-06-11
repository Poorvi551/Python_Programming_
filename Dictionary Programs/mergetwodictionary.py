# WAP to merge two dictionary
d1=eval(input("Enter dictionary1:"))
d2=eval(input("Enter dictionary2:"))
d1.update(d2)
print(d1)

# OR

d1=eval(input("Enter dictionary1:"))
d2=eval(input("Enter dictionary2:"))
out=d1
for i in d2:
    out[i]=d2[i]
print(out)