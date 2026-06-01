# wap to reverse a string using two pointer
def rev_str(s):
    l=list(s)
    i=0
    j=len(l)-1
    while i<j:
        l[i],l[j]=l[j],l[i]
        i+=1
        j-=1
    return ''.join(l)
s=input("Enter a string:")
print(rev_str(s))