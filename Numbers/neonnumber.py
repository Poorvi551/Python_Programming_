n=int(input("Enter a number:"))
sqr=n**2
sum=0
while sqr>0:
    ld=sqr%10
    sum=sum+ld
    sqr=sqr//10
if sum==n:
    print("Neon Number")
else:
    print("Not a Neon Number")