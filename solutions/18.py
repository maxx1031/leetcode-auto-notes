class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        # same as three sum
        """
        1 output type: unique list, element is the combination of sum equal to target
        2 duplicate value: exists
            - skip duplication
        3 no vaild result: return []

        fix bug:
        Bug	描述	修复方式
        1	第二层 b 的去重条件错误	改成 if b > a + 1 and nums[b] == nums[b - 1]
        2	提前剪枝逻辑错误地使用了 break	if nums[a] + sum(nums[-3:]) < target: 应该用 continue
        """
        nums.sort()
        if len(nums) < 4:
            return []
        n = len(nums)
        res = []
        for a in range(n-3):
            if a > 0 and  nums[a] == nums[a-1]:
                continue
            if sum(nums[a:a+4]) > target:
                break
            if nums[a] + sum(nums[n-3:]) < target:
                continue
            for b in range(a+1, n-2):
                if b > a+1 and  nums[b] == nums[b-1]:
                    continue
                if nums[a] + sum(nums[b:b+3]) > target:
                    break
                if nums[a] + nums[b] + sum(nums[n-2:]) < target:
                    continue
                c, d = b+1, n-1
                while c < d:
                    # print(a, b, c, d)
                    sum4 = nums[a] + nums[b] + nums[c] + nums[d]
                    if sum4 == target:
                        res.append([nums[a], nums[b], nums[c], nums[d]])
                        c += 1
                        while c < d and nums[c] == nums[c-1]:
                            c += 1
                        d -= 1
                        while c < d and nums[d] == nums[d+1]:
                            d -= 1
                    elif sum4 < target:
                        c += 1
                    else:
                        d -= 1


        return res