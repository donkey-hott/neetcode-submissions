class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record: List[int] = []
        total = 0

        for op in operations:
            res = 0
            match op:
                case "+":
                    first, second = record[-1], record[-2]
                    res = first + second
                    total += res
                case "D":
                    res = record[-1] * 2
                    total += res
                case "C":
                    item = record.pop()
                    total -= item
                    continue
                case _:
                    res = int(op)
                    total += res
            record.append(res)
        return total
            
