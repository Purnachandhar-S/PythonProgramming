# number of house enough for rats to eat by given units per rat
def calculateHouse(r, n,unit,arr):
  totalFoodNeeded = r*unit
  initialfood = 0
  for house in range(n):
    initialfood = initialfood + arr[house]
    if initialfood >= totalFoodNeeded:
      print(house)
      break

def binaryproblem(string):
  i = 1
  a = int(string[0])
  while i<len(string):
    if string[i]== 'A':
      a&=int(string[i+1])
    elif string[i] == 'B':
      a|= int(string[i+1])
    else:
      a^= int(string[i+1])
    i+=2
  return a

def passwordChecker(string):
  lengthcheck = len(string)>3
  numberCheck 
  CapitalLetterCheck 
  spaceCheck = True
  # for i in string:
  #   if (i == ' ' OR i =="\"):
  #     spaceCheck=False
  return 

def SumPairs(sum1, arr):
  noPairs = 0 
  for i in range(len(arr)):
    for j in range(i+1,len(arr)):
      if(arr[i]+arr[j] == sum1):
        noPairs += 1 
  return noPairs
sum1 = 9 
arr = [5,2,4,3,9,7,1,7] # :5 2 4 3 9 7 1

print(SumPairs(sum1, arr))

print('I appered in github on github')

# print(passwordChecker("aA1_67"))

# – At least 4 characters
# – At least one numeric digit
# – At Least one Capital Letter
# – Must not have space or slash (/)
# – Starting character must not be a number

# string = '0C1A1B1C1C1B0A0'
# print(binaryproblem("1C0C1C1A0B1"))
# print(binaryproblem(string))

# r = 7 # number of rats
# unit = 2 # units it eat per rat
# n = 8 # number of houses
# arr = [2,8,3,5,7,4,1,2]
# # arr = list(map(int,input.split()))
# # calculateHouse(r,n,unit,arr)

