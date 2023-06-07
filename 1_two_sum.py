class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = dict()
        for i, n in enumerate(nums):
            target_less_num = target - n
            if n in hash_map:
                return [i, hash_map[target - target_less_num]]
            hash_map[target_less_num] = i