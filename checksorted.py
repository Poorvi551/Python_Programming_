# wap to check whether the list is sorted or not
def check_sorted(l):
    for i in range(len(l)-1):
        if l[i]>l[i+1]:
            print("List is not sorted")
            return
    print("List is sorted")
l=eval(input("Enter list:"))
check_sorted(l)