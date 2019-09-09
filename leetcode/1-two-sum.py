"""
Runtime: 800 ms, faster than 31.40% of Python3 online submissions for Two Sum.
Memory Usage: 14.9 MB, less than 11.62% of Python3 online submissions for Two Sum.
https://leetcode.com/problems/two-sum
"""



def twoSum(nums, target):
        # nums is a list of given numbers
        # target is our goal

        for i in range(len(nums)):
            cn = nums[i]
            lf = target - cn
            if lf in nums:
                if nums.index(lf) != i:
                    return [i, nums.index(lf)]


print(twoSum([3, 2, 4], 6))
