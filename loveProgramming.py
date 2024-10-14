from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:  # Edge case for empty list
            return 0
        
        # Initialize two pointers, `i` tracks the position of unique elements
        i = 0
        
        # Start from the second element and move through the list
        for j in range(1, len(nums)):
            print('i is {} and j is {}'.format(i,j))
            if nums[j] != nums[i]:
                # Increment `i` and update the next unique position
                i += 1
                nums[i] = nums[j]  # Update the array in-place
                print('*',end=" ")
            print(nums)
        
        # The number of unique elements is i + 1 (as i is zero-indexed)
        return i + 1

# Test the function with the given example
nums = [ 0, 1, 1, 1, 1, 2, 2, 3, 3, 4]
sol = Solution()
new_length = sol.removeDuplicates(nums)

# Output results
print(f"New length: {new_length}")
print(f"Modified nums: {nums[:new_length]} + {[None]*(len(nums)-new_length)}")

# from typing import List

# class Solution:
#     def removeDuplicates(self, nums: List[int]) -> int:
#         print(nums)  # This will print the array passed to the method
#         return len(nums)  # Dummy return for now
#     def combinedElements(self, nums: List[int]) -> int:
#         print(nums)

# # Parse the string into a list of integers
# nums = list(map(int, '1 1 1 1 1'.split()))

# # Create an instance of the Solution class
# sol = Solution()

# # Call the removeDuplicates method and pass the list
# sol.removeDuplicates(nums)
# # sol.combinedElements(nums)