# wap to count the occurrence of given element in the given list
def count_occurrence(l):
    res=[]
    for i in l:
        if i not in res:
            print(i,":",l.count(i))
            res.append(i)
l=eval(input("Enter list:"))
print(count_occurrence(l))



