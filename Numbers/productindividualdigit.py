# WAP to find the product of the individual digit
def product(n):
    prod=1
    while n>0:
        ld=n%10
        prod=prod*ld
        n=n//10
    return prod
n=int(input("Enter num:"))
print(product(n))