class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []

        for char in tokens:
            match char:
                case "+":
                    st.append(st.pop() + st.pop())
                case "-":
                    subtrahend, minuend = st.pop(), st.pop()
                    st.append(minuend - subtrahend)
                case "*":
                    st.append(st.pop() * st.pop())
                case "/":
                    divisor, dividend = st.pop(), st.pop()
                    st.append(int(dividend / divisor))
                case _:
                    st.append(int(char))
        return st.pop()