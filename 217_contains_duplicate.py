class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        no_duplicates = set(nums)
        return len(nums) != len(no_duplicates)