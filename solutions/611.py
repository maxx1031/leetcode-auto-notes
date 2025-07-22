class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        """
        triangle: 
        
        a + b > c 
        a + c > b
        b + c > a
        a > 0, b > 0, c > 0


        C(n, 3) and then check if the triplet is valid
        1. sort array
        2. i, j, k: how to move pointers
        - if [i,j,k] meet the conditions
        - key ideas:如果数组排好序后：a <= b <= c，只需判断：
        ✅ a + b > c，其余两个条件会自然满足。
        - 
        """
        nums.sort()
        n = len(nums)
        count = 0

        for k in range(n - 1, 1, -1):  # 固定第三边
            i = 0
            j = k - 1
            while i < j:
                if nums[i] + nums[j] > nums[k]:  # 满足三角形条件
                    count += (j - i)  # [i, j-1] 全部都能和 j, k 构成三角形
                    j -= 1
                else:
                    i += 1
        return count