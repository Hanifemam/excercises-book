class Solution:
    def containsDuplicate(self, nums) -> bool:
        nums_set = set()
        for i in nums:
            if i not in nums_set:
                nums_set.add(i)
            else:
                return True
        return False
