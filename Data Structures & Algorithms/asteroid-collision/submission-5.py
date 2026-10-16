class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        st = []

        for a in asteroids:
            while st and st[-1] > 0 and a < 0:
                diff = st[-1] + a

                if diff == 0:
                    a = 0
                    st.pop()
                elif diff > 0:
                    a = 0
                else:
                    st.pop()
            if a:
                st.append(a)
        return st