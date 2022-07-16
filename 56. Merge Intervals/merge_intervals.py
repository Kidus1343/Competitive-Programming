class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        answer = []
        for i in range(len(intervals)):
            if not answer:
                answer.append(intervals[i])
            else:
                if answer[-1][1] >= intervals[i][0]:
                    answer[-1][1] = max(answer[-1][1], intervals[i][1])
                else:
                    answer.append(intervals[i])
        return answer
