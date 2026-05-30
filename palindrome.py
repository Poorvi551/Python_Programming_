def palindrome(l):
    i=0
    j=len(l)-1
    flag=True
    while i<j:
        if l[i]!=l[j]:
            flag=False
            break
        i=i+1
        j=j-1
    if flag:
        return "Palindrome"
    else:
        return "Not a Palindrome"
l=eval(input("Enter list:"))
print(palindrome(l))