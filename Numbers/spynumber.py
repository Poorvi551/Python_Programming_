n=int(input("Enter number:"))
sum=0
prod=1
for i in str(n):
    sum+=int(i)
    prod=prod*int(i)
if sum==prod:
    print("Spy number")
else:
    print("Not a spy number")
