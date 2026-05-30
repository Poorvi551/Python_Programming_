# Write a program to sum the integer present in a list
def sum_interger(l):
    sum=0
    for i in l:
        if type(i)==int:
            sum=sum+i
    return sum
l=eval(input("Enter a list:"))
print(sum_interger(l))