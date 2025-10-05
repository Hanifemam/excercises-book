class Solution:
    def moveZeroes(self, nums) -> None:
        first_zero = -1
        lst_zero = -1
        ind = 0
        nums_length = len(nums)
        while first_zero < 0 and ind < nums_length:
            if nums[ind] == 0:
                first_zero = ind
                lst_zero = ind
            ind += 1
        for i in nums[ind:nums_length]:
            if i != 0:
                lst_zero += 1
                nums[first_zero] = i
                nums[lst_zero] = 0
                first_zero += 1
            else:
                lst_zero += 1
