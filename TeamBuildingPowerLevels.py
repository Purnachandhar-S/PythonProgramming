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

 """
# def max_power_level(power_levels):
#     # Sort the power levels to make it easier to find min/max and manipulate
#     power_levels.sort()
    
#     # Handle the case of a zero in the list
#     if 0 in power_levels:
#         # Exclude zeros, since multiplying by zero would result in 0
#         power_levels = [p for p in power_levels if p != 0]
    
#     # If no values left after excluding zeros, return 0
#     if len(power_levels) == 0:
#         return 0
    
#     # Calculate product of all power levels
#     product = 1
#     for p in power_levels:
#         product *= p
    
#     # If product is positive, return it directly
#     if product > 0:
#         return product

#     # If product is negative, check if excluding the smallest (most negative) number helps
#     if product < 0:
#         # Remove the smallest negative number (first element of the sorted list)
#         smallest = power_levels[0]
#         # in the -9 -5 -1 I have to remove -1 to get maximum multiplication value 

#         # Compute product excluding the smallest element
#         product_exclude_smallest = product // smallest
#         return product_exclude_smallest

# # Test input 1: 
# print(max_power_level([3, -1, -5, 2, 5, -9]))  # Expected output: 1350 

# # Test input 2:
# print(max_power_level([-10, -2, 0]))  # Expected output: 20 

def max_power_level(nums):
  mul = 1 
  for i in nums:
    mul *=i 
  if mul == 0:
    if all(p==0 for p in nums):
      return 0 # incase all zeros in array 
    nonZeroArray = [x for x in nums if x != 0]
    product = 1 
    for i in nonZeroArray:
      product *= i
    if product > 0:
      nonZeroArray = [str(x) for x in nonZeroArray]
      result = ' '.join(nonZeroArray)
      return result
    else:
      return 0
  elif mul < 0:
    largest_negative = max([p for p in nums if p < 0],default=None)
    product = 1
    for i in nums:
      if i != largest_negative:
        product *= i
    return product
  else:
    product=1
    for i in nums:
      product *= i 
    return product


array1 = [3, -1, -5, 2, 5, -9]
array2 = [-10,-2,0]
array3 = [0,0,0,0,0]
array4 = [3]
print(max_power_level(array4)) # actually i have to return the array as a single string 


# case 1 : 0 in nums so remove 0 
# case 1.1 : if mul is positive -> return that array 
# case 1.2 : if mul is negative -> return 0
# case 2 : if the mul is negative 
#           step 1 removing the biggest negative number - thanks to chatgpt (I can get smallest positive number is same way)
#                    largest_negative = max([p for p in power_levels if p < 0], default=None)
# case 3 : if the mul is positive -> return that array 
# chatgpt 
# case : if the array have 1 element
#         if element is positive return +ve and -ve return 0

# Case when there are no non-zero numbers (e.g., all zeros)
  #  if all(p == 0 for p in power_levels):
  #       return 0
