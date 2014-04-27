# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e
         
class Solution:
    # @param intervals, a list of Intervals
    # @param newInterval, a Interval
    # @return a list of Interval
    def insert(self, intervals, newInterval):
        if not intervals:
            return [newInterval]
        n1 = newInterval.start
        n2 = newInterval.end
        insertedIntervals = []
        nn1 = None
        lastEnd=0
        inserted = False
        for intv in intervals:
            if nn1 is None and n1 <= intv.end:
                nn1 = min(n1,intv.start)
            if intv.start > n2 and nn1 is not None:
                if lastEnd <= n2:
                    insertedIntervals.append(Interval(nn1, n2))
                    inserted = True
                insertedIntervals.append(intv)
            elif intv.start > n2 and nn1 is None:
                insertedIntervals.append(intv)
            elif intv.start <= n2 and intv.end > n2:
                insertedIntervals.append(Interval(nn1,intv.end))
                inserted = True
            elif intv.end < n1:
                insertedIntervals.append(intv)
            lastEnd = intv.end
                
        if inserted == False:
            if nn1 is None:
                nn1 = n1
            insertedIntervals.append(Interval(nn1,n2))
        return insertedIntervals
    
    
if __name__ == '__main__':
    intervals = [Interval(1,5)]
    newInterval = Interval(0,1)
    s = Solution()
    res = s.insert(intervals, newInterval)
    for r in res:
        print "["+str(r.start) +","+str(r.end)+"],"
    
