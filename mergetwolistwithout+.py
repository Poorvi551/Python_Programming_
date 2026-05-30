#wap to merge two list without using + operator
def merge_list(l1,l2):
    out=l1
    for i in l2:
        out.append(i)
    return out
l1=eval(input("Enter list1:"))
l2=eval(input("Enter list2:"))
print(merge_list(l1,l2))