#wap to count the occurrence of an element in the given string
def count_occurrence(s):
    count=0
    element=input("Enter the element:")
    for i in s:
        if i==element:
            count+=1
    return count
s=input("Enter string:")
print(count_occurrence(s))