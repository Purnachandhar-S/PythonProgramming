def removeDuplicates(nums):
  i=0
  for j in range(1,len(nums)):
    if nums[j] != nums[i]:
      i+=1
      # nums[j] = nums[i+1]
    print(i)
  print(nums)
  return
array = [0,1,1,1,1,2,2,2,3,4,4]
removeDuplicates(array)

# class solution:
#   def removeDuplicates(self,nums):
#     print(nums)
#     return 

# sol = solution()
# sol.removeDuplicates(1)
