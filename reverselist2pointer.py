# write a program to reverse a list using two pointer approach
def reverse_list(l):
    i=0
    j=len(l)-1
    while i<j:
        l[i],l[j]=l[j],l[i]
        i=i+1
        j=j-1
    return l
l=eval(input("Enter  a list:"))
print(reverse_list(l))