#WAP to find the maximum of values in the dict
d=eval(input("Enter dict:"))
key=list(d.keys())[0]
max_val=d[key]
for k,v in d.items():
    if  v>max_val:
        max_val=v
        key=k
print(key,max_val)