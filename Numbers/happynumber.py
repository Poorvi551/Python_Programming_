n=int(input("Enter a number:"))
val=set()
while n>1:
    if n in val:
        print("not a happy number")
        break
    val.add(n)
    sum = 0
    for i in str(n):
        num = int(i)
        sum = sum + (n ** 2)
    n = sum
else:
    print("Happy Number")

