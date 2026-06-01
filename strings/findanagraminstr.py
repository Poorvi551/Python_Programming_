# WAP to check whether the given string is anagram or not
def anagram(s1,s2):
    if sorted(s1)==sorted(s2):
        return 'anagram'
    else:
        return 'not a anagram'
s1=input("Enter string1:").replace(' ','').lower()
s2=input("Enter string2:").replace(' ','').lower()
print(anagram(s1,s2))