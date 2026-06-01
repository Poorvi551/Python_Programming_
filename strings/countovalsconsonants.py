def count_oval_consonant(s):
    vowel=0
    consonant=0
    for i in s:
        if i in 'AEIOUaeiou':
            vowel+=1
        elif 'A'<=i<='z' or 'a'<=i<='z':
            consonant+=1
    return vowel,consonant
s=input("Enter a string:")
print(count_oval_consonant(s))