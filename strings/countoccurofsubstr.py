# wap to count the occurrence of substring in the string
def count_occur_substr(s,sub):
    count=0
    for i in range(len(s)-len(sub)+1):
        if s[i:i+len(sub)]==sub:
            count+=1
    return count
s=input("Enter a string:")
sub=input("Enter sub string:")
print(count_occur_substr(s,sub))


# or

def count_occur_substr(s):
    count=0
    sub = input("Enter sub string:")
    for i in range(len(s)-len(sub)+1):
        slice=s[i:i+len(sub)]
        if slice==sub:
            count+=1
    return count
s=input("Enter a string:")
print(count_occur_substr(s))


# or


def count_occur_substr(s):
    count=0
    sub = input("Enter sub string:")
    for i in range(len(s)-len(sub)+1):
        if s[i:i+len(sub)]==sub:
            count+=1
    return count
s=input("Enter a string:")
print(count_occur_substr(s))