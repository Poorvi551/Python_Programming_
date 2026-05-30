# wap to find the second largest number in the given list
def sec_largest(l):
    l=list(set(l))
    l.sort()
    return l[-2]
l=eval(input("Enter a list:"))
print(sec_largest(l))