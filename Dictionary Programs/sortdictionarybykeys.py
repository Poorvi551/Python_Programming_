#WAP to sort dictionary by keys
d=eval(input("Enter dictionary:"))
key=list(d.keys())
for passno in range(1,len(key)):
    for i in range(len(key)-passno):
        if key[i]>key[i+1]:
            key[i],key[i+1]=key[i+1],key[i]
out={}
for i in key:
    out[i]=d[i]
print(out)
