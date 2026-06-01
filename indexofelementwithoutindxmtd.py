#wap to print index values of the given element without using index values. - assignment q2
def find_index_without_idxmetd(l):
    for i in enumerate(l):                      # used to print the index values of an element
        print(i)
l=eval(input("Enter list:"))
find_index_without_idxmetd(l)