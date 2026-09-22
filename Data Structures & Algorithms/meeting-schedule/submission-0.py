"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        sorted_intervals = sorted(intervals, key=lambda x: x.end)
        # sorted_intervals = intervals
        n = len(sorted_intervals)
        for i in range(n - 1):
            if sorted_intervals[i].end > sorted_intervals[i + 1].start:
                return False
        return True