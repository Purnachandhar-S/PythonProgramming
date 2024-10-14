n=5

 
# # for i in range(n+2):
# #   for j in range(i):
# #     print(j, end=" ")
# #   print()



# '''
# 5
# 4 5 
# 3 4 5 
# 2 3 4 5
# 1 2 3 4 5
# '''
# for i in range(n):
#   for j in range(n-i,n+1):
#     print(j, end=" ")
#     # print("{} {}".format(n-i,n+1))
#   print()

# for i in range(1,n+2):
#   space = (n-i)*"  "
#   result = ""
#   for j in range(1,i):
#     result += str(j)+ " "
#   print(space+ result)

# for i in range(1,6):
#   for s in range(5,i,-1):
#     print(" ",end="")
#   for j in range(1,i+1):
#     print(j,end="")
#   print()
  

#           5 
#         4 5
#       3 4 5
#     2 3 4 5
#   1 2 3 4 5

# for i in range(n):
#   for s in range(n, i,-1 ):
#     print(" ",end=" ")
#   for j in range(n-i,n+1):
#     print(j,end=" ")
#   print()


# for i in range(n):
#   # for s in range(i):
#   #   print(" ",end=" ")
#   # for j in range(n-i,0,-1):
#   #   print(j,end=" ")
#   for k in range(i+1):
#     print(k,end=" ")
#   print()

"""
Pyramid shape
        1
      2 1 2
    3 2 1 2 3
  4 3 2 1 2 3 4
5 4 3 2 1 2 3 4 5

"""
# for i in range(n+1):
#   # first part 
#   for s in range(n, i,-1 ):
#     print(" ",end=" ")

#   for k in range(i,0,-1):
#     print(k,end=" ")
#   # third part 
#   for j in range(2,i+1):
#     print(j, end=" ")
#   print()

for i in range(n+1):
    for s in range(n,i,-1):
      print(" ",end=" ")
    for k in range(n-i,n+1):
      print(k, end= " ")
    print()


