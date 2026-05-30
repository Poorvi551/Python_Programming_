def missing_values(l):
    n=int(input("Enter n value:"))
    sum_val=sum(l)
    res=n*(n+1)//2
    return res-sum_val
l=eval(input("Enter a list:"))
print(missing_values(l))