# WAP to remove duplicate values in the dictionary
d=eval(input("Enter dict:"))
out={}
res=set()
for k,v in d.items():
    if v not in res:
        out[k]=v
        res.add(v)
print(out)
