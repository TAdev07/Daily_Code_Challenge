class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count = 0
        final = []
        for i in nums:
            if i != val:
                final.append(i)
        nums[:] = final
        return len(nums)