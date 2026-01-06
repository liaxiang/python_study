class Solution:
    def twoSum(self, nums:list[int], target:int) -> list[int]:
        num_to_index = {}
        for index, num in enumerate(nums):
            compliment = target - num
            if compliment in num_to_index:
                return [num_to_index[compliment], index]
            num_to_index[num] = index
        return []

# For王到此一游
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         for i in range(len(numbs)):
#             for j in range(i+1, len(nums)):
#                 if nums[i] + nums[j] == target:
#                     return [i, j]

nums = [1,9,5,7]
target = 12
T1 = Solution()
result = T1.twoSum(nums, target)
print(result)