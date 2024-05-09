# HOW IS GRADESCOPE SAYING THIS PROGRAM DOESN'T OUTPUT ANYTHING
# WHEN IT CLEARLY DOES. THIS PROGRAM WORKS ON MY MACHINE, BUT
# GRADESCOPE SAYS IT DOESN'T OUTPUT ANYTHING FOR ANY TESTS.
# I HAVE NO IDEA.

import numpy as np
import sys

def findI(jobs):
    retval = -1
    for i in range(len(jobs)-1, -1, -1):
        if jobs[i][1] <= jobs[j][0]:
            retval = i
            break
    return retval

def weightIntDP(jobs):
    m = np.zeros(len(jobs))

    for j in range(len(jobs)):
        # find index i < j, such that jobs[i][1] < jobs[j][0]
        i = findI(jobs)
        if i == -1:
            adding = 0
        else:
            adding = m[i]

        # either add jobs[j]'s weight to m[i] or just use m[j-1]
        m[j] = max(m[j-1], adding + jobs[j][2])

    return m[len(jobs)-1]


if __name__ == "__main__":
    instances = int(sys.stdin.readline())
    max_weights = []
    for i in range(instances):
        num_jobs = int(sys.stdin.readline())
        jobs = []
        for j in range(num_jobs):
            jobs.append(list(map(int, sys.stdin.readline().split(" "))))
        jobs.sort(key=lambda x: x[1])
        max_weights.append(weightIntDP(jobs))

    for weight in max_weights:
        print(int(weight))