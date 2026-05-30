def common_val(l1,l2):
    out=[]
    for i in l1:
        if i in l2 and i not in out:
            out.append(i)
    return out
l1=eval(input("Enter list1:"))
l2=eval(input("Enter list2:"))
print(common_val(l1,l2))