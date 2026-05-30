def missing_multval(l,n):
    for i in range(1, n + 1):
        if i not in l:
            print(i)
l = eval(input("Enter list:"))
n = int(input("Enter a val:"))
missing_multval(l,n)
