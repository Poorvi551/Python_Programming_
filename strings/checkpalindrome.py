# WAP to check Palindrome using two pointer
# def check_palindrome(s):     this programs reverse the string and checks for palindrome
#     l=list(s)
#     i=0
#     j=len(l)-1
#     while i<j:
#         l[i],l[j]=l[j],l[i]
#         i+=1
#         j-=1
#     return ''.join(l)
# s=input("Enter a string:")
# rev=check_palindrome(s)
# if s==rev:
#     print("String is palindrome")
# else:
#     print("String is not palindrome")

# or

def check_palidrome_str(s):     # this program checks whether the elements are same
    i=0
    j=len(s)-1
    flag=True
    while i<j:
        if s[i]!=s[j]:
            flag=False
            break
        i+=1
        j-=1
    if flag:
        return 'palindrome'
    else:
        return 'not a palindrome'
s=input("Enter string:")
print(check_palidrome_str(s))
