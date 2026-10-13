class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        entries = dict()
        for num in nums:
            if num in entries:
                return True
            entries[num] = True
        return False
        