def sum(l,n):
    out=[]
    for i in range(0,len(l)):
        if l[i]==n:
            out.append([l[i]])
        else:
            for j in range(i+1,len(l)):
                if l[i]+l[j]==n:
                    out.append([l[i],l[j]])
    return out
l=eval(input("Enter list:"))
n=int(input("Enter n val:"))
print(sum(l,n))
