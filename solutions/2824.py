class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        nums.sort()
        j = len(nums)-1
        i = 0
        count = 0
        while(i<j):
            if (nums[i]+nums[j])<target:
                count += (j-i)
                i += 1
            else:
                j -= 1
        return count