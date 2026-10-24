class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        max_left, max_right = height[l], height[r]
        ans = 0

        while l < r:
            if max_left < max_right:
                ans += max_left - height[l]
                l += 1
                max_left = max(max_left, height[l])
            else:
                ans += max_right - height[r]
                r -= 1
                max_right = max(max_right, height[r])
        return ans