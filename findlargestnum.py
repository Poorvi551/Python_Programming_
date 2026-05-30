# wap to find the largest value from the given list
def largest_val(l):
    l=list(set(l))
    l.sort()
    return l[-1]
l=eval(input("Enter a list:"))
print(largest_val(l))