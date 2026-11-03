class TimeMap:

    def __init__(self):
        self.history = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.history[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        values = self.history[key]

        if not values: return ""

        l, r = 0, len(values) - 1

        while l <= r:
            m = (l + r) // 2
            m_value, m_timestamp = values[m]

            if m_timestamp == timestamp:
                return m_value
            
            if timestamp > m_timestamp:
                l = m + 1
            else:
                r = m - 1
        if r < 0: return ""
        return values[r][0]
            
            
