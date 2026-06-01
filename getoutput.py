# wap to get the output of file extensions
def get_output(userinput):
    out=[]
    for i in userinput:
        if "." in i:
            pos=i.index(".")
            out.append(i[pos+1:])
    return out
userinput=['python.py','pro1.html','data.db','google.com']
print(get_output(userinput))

