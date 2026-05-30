def move_zeroes(l):
    zero=[]
    out=[]
    for i in l:
        if i!=0:
            out.append(i)
        else:
            zero.append(i)
    return out+zero
l=eval(input("Enter list:"))
print(move_zeroes(l))