class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count1 = 0
        count2 = 0
        candidate1 = None
        candidate2 = None

        for n in nums:
            if n == candidate1:
                count1 += 1
            elif n == candidate2:
                count2 += 1
            elif count1 == 0:
                candidate1 = n
                count1 = 1
            elif count2 == 0:
                candidate2 = n
                count2 = 1
            else:
                count1 -=1
                count2 -=1

        count1 = 0
        count2 = 0
        target = len(nums) // 3
        ans = []
        for n in nums:
            if n == candidate1: count1 += 1
            elif n == candidate2: count2 += 1
            
        if count1 > target: ans.append(candidate1)
        if count2 > target: ans.append(candidate2)
        return ans