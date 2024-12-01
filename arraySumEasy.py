"""
sample input 2 4 1 6 3
output 4 8 5 12 9 
You have to sum with maximum number from index 0 to prevIndex in the array to current number 
solution 2+2 = 4 | 4+4 = 8 | 1+4 = 5 | 6+6 = 12 | 3+6 =9 
"""
def arraySum(nums):
  result = []
  for i in range(len(nums)):
    if i ==0:
      result.append(nums[i] *2)
    else:
      bigOne = max(nums[:i+1])
      result.append(nums[i]+bigOne)
  result1 = " ".join([str(x) for x in result])
  return result1
# nums = list(map(int, input().split()))
nums = [2,4,1,6,3]
print(arraySum(nums))