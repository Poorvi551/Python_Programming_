def right_rotate(l,n):
    n=n%len(l)
    out=l[-n:]+l[:-n]
    return out
l=eval(input("Enter list:"))
n=int(input("Enter number of rotation:"))
print(right_rotate(l,n))

# Left Rotate
def left_rotate(l,n):
    n=n%len(l)
    out=l[n:]+l[:n]
    return out
l=eval(input("Enter list:"))
n=int(input("Enter number of rotation:"))
print(left_rotate(l,n))