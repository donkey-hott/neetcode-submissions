from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans = []
        queue = deque()

        for i in range(len(nums)):
            while len(queue) and queue[0] <= i - k:
                queue.popleft()
            
            while len(queue) > 0 and nums[queue[-1]] < nums[i]:
                queue.pop()
            queue.append(i)
            if i >= k - 1:
                ans.append(nums[queue[0]])
        return ans