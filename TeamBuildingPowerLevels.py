"""
if given power levels = 3 -1 -5 2 5 -9
- if you choose all the characters for your team, the team's power level will be -1350  (multiplying all)
- However, you can increase your team's power level by stractegically excluding the character with -1 power level.
- This gives your team a power level of 1350 (multiplying 3 -5 2 5 -9)
- this is the maximum possible power that your team can achieve from the given characters.
- The power levels of these characters in ascending order are -9,-5,2,3,5 (OUTPUT)
Sample input2 
-10 -2 0 (output = 20)

how to join a array
how to remove one element from array


"""

array = [ 3, -5, 2, 5, -9,0] 
array2 = [-10,-2,0]

mul = 1 
for i in array:
  mul = mul*i
print(mul)

if mul ==0 :
  arr2 = [x for x in array if x != 0] 
  # you use array.remove() or pop(numver)
  result = 1
  for i in arr2:
    result *= i 
  if result> 0:
    answer = " ".join(arr2)
    print(answer)
  # in the case of zero excluding zero can get highest power 
  result = array.filter(each != 0)
  print(result)
elif mul>0:
  # in the case of printing directly 
  print(1)
elif mul<0:
  # in the case of Negative number excluding one smallest number 
  print(-1)