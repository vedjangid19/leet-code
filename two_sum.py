from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        temp_dict = {}

        for index, value in enumerate(nums):
            temp_value = target - value

            if temp_value in temp_dict:
                return [temp_dict[temp_value], index]
            
            temp_dict[value] = index


    def twoSum2(self, nums: List[int], target: int) -> List[int]:
        # Iterate over the list with index and value
        for ind, i in enumerate(nums):
            # Iterate over the rest of the list starting from the next index
            for ind2, j in enumerate(nums[ind + 1:], ind + 1):
                # Check if the sum of the two numbers matches the target
                if i + j == target:
                    return [ind, ind2]



sol_obj = Solution()
nums = [3, 2, 4]
target = 6
print(sol_obj.twoSum2(nums=nums, target=target))
print(sol_obj.twoSum(nums=nums, target=target))