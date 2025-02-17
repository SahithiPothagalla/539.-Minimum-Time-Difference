class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        if len(timePoints) != len(set(timePoints)):  
            return 0
        else:
            result = []
            for t in timePoints:
                hours, minutes = map(int, t.split(":"))
                total = 60 * hours + minutes  
                result.append(total)
            result.sort()  
            mind = 1440 
            for j in range(len(result) - 1):
                mind = min(mind, abs(result[j] - result[j + 1]))
            mind = min(mind, 1440 - abs(result[-1] - result[0]))
            return mind
