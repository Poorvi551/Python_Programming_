# wap to find the element which is repeated more numbers of times
def repeated_multiple_times(l):
    for i in l:
        if l.count(i)>l.count(i+1):
            return i
l=eval(input("Enter list:"))
print(repeated_multiple_times(l))
