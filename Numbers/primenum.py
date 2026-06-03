# WAP to print the number is prime or not
def prime(n):
    count=0
    for i in range(1,n+1):
        if n%i==0:
            count+=1
    if count==2:
        return 'Prime'
    else:
        return 'Not Prime'
n=int(input("Enter a num:"))
print(prime(n))





    # if n%1==0 and n%n==0:
    #     return 'Prime'
    # else:
    #     return 'Not Prime'