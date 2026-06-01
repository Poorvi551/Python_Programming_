# wap to print first non-repeating character from string
def non_repeat(s):
    for i in range(len(s)):
        count=0
        for j in range(len(s)):
            if s[i]==s[j]:
                count+=1
        if count==1:
            return s[i]
s=input("Enter string:")
print(non_repeat(s))

