class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        st = []
        ans = 0
        n = len(heights)

        for i in range(n):
            start_idx = i
            while st and st[-1][1] > heights[i]:
                start, val = st.pop()

                ans = max(ans, val * (i - start))
                start_idx = start
            st.append((start_idx, heights[i]))
        
        for idx, height in st:
            ans = max(ans, height * (n - idx))
        
        return ans
