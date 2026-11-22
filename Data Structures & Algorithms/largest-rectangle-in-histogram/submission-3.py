class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        st = []
        max_area = 0
        n = len(heights)

        for i, h in enumerate(heights):
            start = i

            while st and st[-1][1] > h:
                idx, height = st.pop()
                max_area = max(max_area, height * (i - idx))
                start = idx
            st.append((start, h))
        
        for i, h in st:
            max_area = max(max_area, h * (n - i))
        return max_area