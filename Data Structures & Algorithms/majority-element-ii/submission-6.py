class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count1 = 0
        n1 = None
        count2 = 0
        n2 = None

        for n in nums:
            if count1 == 0:
                n1 = n
            elif count2 == 0:
                n2 = n

            if n1 == n:
                count1 += 1
            elif n2 == n:
                count2 += 1
            else:
                count1 -= 1
                count2 -= 1
        
        counts = defaultdict(int)
        ans = []

        for n in nums:
            if n == n1 or n == n2:
                counts[n] += 1
            if counts[n] > len(nums) // 3 and n not in ans:
                ans.append(n)
        return ans
            