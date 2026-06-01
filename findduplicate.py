# wap to find the duplicate element from the list
def find_duplicate(l):
    l1=set()
    out=set()
    for i in l:
        if i in l1:
            out.add(i)    # set has no attribute called append
        else:
            l1.add(i)
    return out
l=eval(input("Enter list:"))
print(find_duplicate(l))
