class Solution:
    def simplifyPath(self, path: str) -> str:
        st = []
        i = 0
        n = len(path)

        while i < n:
            if path[i] == '/':
                i += 1
                segment = ''

                while i < n and path[i] != '/':
                    segment += path[i]
                    i += 1
                if st and segment == '..':
                    st.pop()
                elif segment and segment != '.' and segment != '..':
                    st.append(segment)

        return '/' + '/'.join(st)
