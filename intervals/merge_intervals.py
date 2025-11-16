"""
Problem:
You are given a list of time intervals for meetings, where each interval is represented as a pair (start, end) with integer times.
Some intervals may overlap.

Merge all overlapping intervals and return a list of non-overlapping intervals that cover all the same ranges.
"""
def mergeIntervals(intervals: list[tuple[int,int]]) -> list[tuple[int,int]]:

    # 1. Sort the given list by each interval’s start time.
    #intervals.sort(key=lambda x: x[0]) -this is correct but by default, sort() looks at the first element anyways, so:
    intervals.sort()

    # 2. Create a merged list and add the first interval from the now-sorted list to it.
    merged = [intervals[0]]


    # 3. Loop through the remaining intervals (starting at index 1):
    for i in range(1, len(intervals)):
        curr_start = intervals[i][0]
        curr_end = intervals[i][1]
        prev_start = merged[-1][0]
        prev_end = merged[-1][1]

        if curr_start <= prev_end:
            merged[-1] = (prev_start, max(prev_end, curr_end))
        else:
            merged.append((curr_start,curr_end))

    # 4. Return the merged list.
    return merged