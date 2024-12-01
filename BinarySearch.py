def binarySearch(nums,s):
  l = nums[0]
  h = nums[len(nums)-1]
  while l <= h:
    mid = round((l+h) / 2,0)
    if nums[mid] == s:
      return mid 



  
     

nums = [1,2,3,4,5,6,7]
nums.sort()
s = 4
print(binarySearch(nums,s))