class TimeMap:

    def __init__(self):
        self.hash_map = dict()

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.hash_map:
            self.hash_map[key].append((timestamp, value))
        else:
            self.hash_map[key] = [(timestamp, value)]

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        values = self.hash_map.get(key, "")
        left, right = 0, len(values) - 1
        while left <= right:
            mid = (left + right) // 2
            if values[mid][0] <= timestamp:
                left += 1
                res = values[mid][1]
            else:
                right -= 1
 
        return res
