class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        st = []

        for a in asteroids:
            if a < 0 and st:
                while st and st[-1] > 0 and abs(st[-1]) < abs(a):
                    st.pop()
                if not st:
                    st.append(a)
                elif st[-1] > 0 and abs(st[-1]) == abs(a):
                    st.pop()
                elif st[-1] < 0:
                    st.append(a)
                elif st[-1] > a:
                    continue
                else:
                    st.append(a)
            else:
                st.append(a)
        return st