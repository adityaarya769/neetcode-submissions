class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        new_list = list(set(nums))
        return len(new_list) != len(nums)
