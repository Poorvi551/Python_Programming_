n=int(input("Enter number:"))
square=n**2
if str(square).endswith(str(n)):
    print("Automorphic Number")
else:
    print("Not a Automorphic number")