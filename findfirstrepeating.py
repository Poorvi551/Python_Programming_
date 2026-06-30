# wap to find first repeating element

l=eval(input("Enter list:"))
res=[]
for i in l:
    if i in out:
        print(i)
        break
    res.append(i)
# def first_repeating(l):
#     res=[]
#     for i in l:
#         for j in range(i+1,len(l)):
#             if l[i]==l[j]:
#                 res.append(l[i])
#     return res
# l=eval(input("Enter list:"))    #[1,2,3,2,1]
# print(first_repeating(l))



# or

# def first_repeating(l):       Finds repeating values and stores it
#     res=[]
#     i=0
#     j=len(l)-1
#     while l[i]==l[i+1]:
#         res.append(l[i+1])
#         i=+1
#         j-=1
#     return res
# l=eval(input("Enter list:"))
# print(first_repeating(l))
