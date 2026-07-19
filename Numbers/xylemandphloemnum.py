n=int(input("Enter a number:"))
n_str=str(n)
first_last=int(n_str[0])+int(n_str[-1])
sum=0
for i in n_str[1:len(n_str)-1]:
    sum=sum+int(i)
if first_last==sum:
    print("Xylem number")
else:
    print("Phloem number")