# WAP to find the HCF/GCD of two numbers
def hcf(n1,n2):
    hcf=1
    for i in range(1,min(n1,n2)+1):
        if n1%i==0 and n2%i==0:
            hcf=i
    return hcf
n1=int(input("Enter num1:"))
n2=int(input("Enter num2:"))
print(hcf(n1,n2))