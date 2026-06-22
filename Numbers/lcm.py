#WAP to print lcm of two numbers
def lcm(n1,n2):
    for i in range(1,n1*n2+1):
        if i%n1==0 and i%n2==0:
            return i
n1=int(input("Enter n1:"))
n2=int(input("Enter n2:"))
print(lcm(n1,n2))

#  or
 # faster for large numbers
# def hcf(n1, n2):
#     while n2:
#         n1, n2 = n2, n1 % n2
#     return n1
#
# def lcm(n1, n2):
#     return (n1 * n2) // hcf(n1, n2)