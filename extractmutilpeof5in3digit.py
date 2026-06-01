# wap to extract all the five multiples and has 3 digit in the list
def extract_multiple_of_five(l):
    out=[]
    for i in l:
        if i%5==0 and 100<=i<=999:
            out.append(i)
    return out
l=eval(input("Enter list:"))
print(extract_multiple_of_five(l))