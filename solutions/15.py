"""
#1 how to avoid duplications:
- outer for-loop: nums[i] == nums[i-1]
- inner for-loop: nums[j] == nums[j-1]
#2 early stop:
- if nums[i] + nums[i+1] + nums[i+1] > 0: break
- if nums[i] + nums[i-2] + nums[i-2] < 0: continue
"""
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
	nums.sort()
	ans = []
	n = len(nums)
	for i in range(n-2):
	    x = nums[i]
	    if i > 0 and x == nums[i-1]:
		continue
            if x +  nums[i+1] + nums[i+1] > 0:
		break
            if x +  nums[i-2] + nums[i-1] < 0:
                continue
  	    j = i + 1
	    k = n - 1
 	    while j < k:
		s = x + nums[j] + nums[k]
		if s > 0:
		    k -= 1
		elif s < 0:
		   j += 1
		else:
		    ans.append([x, nums[j], nums[k])
		    j += 1
		    while j < k and nums[j] == nums[j-1]:
			j += 1
		    k -= 1
		    while j < k and nums[k] == nums[k+1]:
			k -= 1
	return ans

