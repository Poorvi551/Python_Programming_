# WAP to generate 10 fibnoacci number
def fib(n):
    n1=0
    n2=1
    for i in range(1,n+1):
        print(n1,end=' ')
        n3=n1+n2
        n1,n2=n2,n3
n=int(input("Enter val:"))
fib(n)