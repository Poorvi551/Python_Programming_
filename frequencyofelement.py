def freq_element(l):
    out=[]
    for i in l:
        if i not in out:
            print(i,":",l.count(i))
            out.append(i)
l=eval(input("Enter list:"))
print(freq_element(l))