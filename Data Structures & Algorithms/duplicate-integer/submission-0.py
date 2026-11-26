class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dict = {}
        for num in nums:
            if num not in dict:
                dict[num] = 1
            else:
                dict[num] += 1
    
        for i in range(len(nums)):
            if dict[nums[i]] > 1:
                return True
        
        return False
        