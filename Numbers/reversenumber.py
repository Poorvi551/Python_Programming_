def reverse_number(n):
    rev=0
    while n>0:
        ld=n%10
        rev=rev*10+ld
        n=n//10
    return rev
n=int(input("Enter num:"))
print(reverse_number(n))
