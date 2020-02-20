#!/usr/bin/python

import sys


# cookie monster can only eat 0, 1, 2, 3 at a time
# given n how many different ways could he eat them


# Start by dividing by three then use recursion on the remainder?

# What if I check every number and how many times that can be eaten and then add it
# similar to fibonacci sequence?

# THERE IS A PATTERN BUT WHAT THE CUSS IS IT
# if n = 5
# 0 = 1
# 1 = 1
# 2 = 2
# 3 = 4
# 4 = 7
# 5 = 13

# I found the pattern
# 4 == 7 because
# 4 - 1 = 3 and 3 has 4 out comes so it has 4 way so far
# 4 - 2 = 2 and 2 has 2 out comes plus the 4 from the previous step so out come is now 6
# 4 - 3 = 1 and 1 has 1 out comes plus the 6 from the previous step so out come is now 7


# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive 
# recursive solution

# Step one build base case
# or I can just add the values of the previous three
# need to do both

def eating_cookies(n, cache=None):
    base_case = [0 for i in range(0, n + 1)]

    if n == 0:
        return 1
    elif n < 3:
        return n

    base_case[0] = 1
    base_case[1] = 2
    base_case[2] = 4

    for i in range(3, n + 1):
        base_case[i] = base_case[i - 1] + base_case[i - 2] + base_case[i - 3]

    return base_case[n - 1]




if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_cookies = int(sys.argv[1])
        print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies),
                                                                                    n=num_cookies))
    else:
        print('Usage: eating_cookies.py [num_cookies]')
