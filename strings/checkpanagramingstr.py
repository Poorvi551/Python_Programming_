#WAP to check whether the string is panagram or not
# panagram - string contains all 26 characters  Ex: 'The quick brown fox jumps over the lazy dog'
def panagram(s):
    import string
    str_set=set(s)
    alpha=set(string.ascii_lowercase)
    if alpha.issubset(str_set):
        return 'panagram'
    else:
        return 'not in paragram'
s=input("Enter string:").lower()
print(panagram(s))

