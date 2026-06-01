# wap to find the first non repeated element in the list
def first_non_repeated(l):
    for i in l:
        if l.count(i)==1:
            return i
l=eval(input("Enter list:"))
print(first_non_repeated(l))