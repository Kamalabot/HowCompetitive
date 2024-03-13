from typing import List


intlist = List[int]
startTime = [1, 2, 3, 3]
endTime = [3, 4, 5, 6]
profit = [50, 10, 40, 70]

print([x for x in zip(startTime, endTime, profit)])


def memoization(func):  # implementing cache as decorator
    memo = {}  # stores the function params as key
    # and its return as value

    def helper(x):  # takes the parameter of the function
        if x not in memo:
            memo[x] = func(x)
        return memo[x]
    return helper


class Solution:
    def jobScheduling(self, startTime: intlist,
                      endTime: intlist,
                      profit: intlist) -> int:
        def find_next_available_job(index: int, end_time: int) -> int:
            """After given index what is the next job available"""
            left, right = index, len(jobs)
            while left < right:  # this loop has to be completed
                mid = left + (right-left) // 2
                # print(jobs)
                if jobs[mid][0] >= end_time:  # if mid start_time is
                    # greater than current end_time, it has to be skipped
                    right = mid  #  
                else:
                    left = mid + 1

            return left

        @memoization
        def find_optimal_schedule(index: int) -> int:
            if index == len(jobs):
                return 0
            next_available_job = find_next_available_job(index, jobs[index][1])
            max_profit = max(jobs[index][2] + find_optimal_schedule(next_available_job),
                             find_optimal_schedule(index+1))
            return max_profit

        jobs = sorted(zip(startTime, endTime, profit))  # create a array of 
        return find_optimal_schedule(0)


def find_next_available_job(index: int, end_time: int) -> int:
    """After given index what is the next job available"""
    left, right = index, len(jobs)
    while left < right:  # this loop has to be completed
        mid = left + (right-left) // 2
        # print(jobs)
        if jobs[mid][0] >= end_time:  # if mid start_time is
            # greater than current end_time, it has to be skipped
            right = mid  #  
        else:
            left = mid + 1

    return left


lsoln = Solution()

jobs = [x for x in zip(startTime, endTime, profit)]
print(jobs)
print(jobs[0])

print(find_next_available_job(0, jobs[0][1]))

# print(lsoln.jobScheduling(startTime=startTime,
                          # endTime=endTime,
                          # profit=profit))
