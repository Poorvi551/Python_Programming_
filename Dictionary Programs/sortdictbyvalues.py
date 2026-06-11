# WAP to sort dictionary by values
d=eval(input("Enter the dictionary:"))
items=list(d.items())
for passno in range(1,len(items)):
    for i in range(len(items)-passno):
        if items[i][1]>items[i+1][1]:
            items[i],items[i+1]=items[i+1],items[i]
out={}
for k,v in items:
    out[k]=v
print(out)
