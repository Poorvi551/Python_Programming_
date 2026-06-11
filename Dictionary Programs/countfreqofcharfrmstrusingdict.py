# WAP to count the frequency of character in the string using dictionary
s=input("Enter string:")
out={}
for i in s:
    out[i]=s.count(i)
print(out)
