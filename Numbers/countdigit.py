# WAP to count the digit in te given number
def count_digit(n):
    count=0
    for i in str(n):
        count+=1
    return count
n=int(input("Enter num:"))
print(count_digit(n))