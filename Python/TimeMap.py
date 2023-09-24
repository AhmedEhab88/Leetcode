class TimeMap:
    def __init__(self):
        self.timeMap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.timeMap:
            self.timeMap[key] = list(list())
            self.timeMap[key] = [value, timestamp]
        else:
            self.timeMap[key].extend([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        values_list = self.timeMap[key]
        time_stamps = [values_list[x] for x in range(1, len(values_list), 2)]

        l, r = 0, len(time_stamps) - 1
        minSoFar = -1
        if timestamp < time_stamps[0]:
            return ""
        elif timestamp > time_stamps[-1]:
            return values_list[values_list.index(time_stamps[-1]) - 1]
        else:
            while l <= r:
                mid = (l + r) // 2
                if time_stamps[mid] == timestamp:
                    return values_list[values_list.index(timestamp) - 1]
                elif time_stamps[mid] > timestamp:
                    r = mid - 1
                else:
                    minSoFar = time_stamps[mid]
                    l = mid + 1

        return values_list[values_list.index(minSoFar) - 1]
