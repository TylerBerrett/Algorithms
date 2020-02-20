#!/usr/bin/python

# n = amount of times i get to go in that round
# example if n == 2 [rock, rock] and all the other combos

# amount of combos for each element is going to be 3 ^ n

# steps
# make rock, paper, scissors list
# if n = 0 empty array
# if n = 1 one time of rock paper sissors
# if n = 2 rock + rock, rock + paper, rock + sissors.
# loop through list and add rock paper sissors to the item

import sys


def rock_paper_scissors(n):
    if n == 0:
        return [[]]

    choices = [['rock'], ['paper'], ['scissors']]

    def helper(i, arr):
        if i == n:
            return arr
        else:
            new_arr = []
            for item in arr:
                new_arr.append(item + ['rock'])
                new_arr.append(item + ['paper'])
                new_arr.append(item + ['scissors'])
            return helper(i + 1, new_arr)

    return helper(1, choices)


print(rock_paper_scissors(3))

if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_plays = int(sys.argv[1])
        print(rock_paper_scissors(num_plays))
    else:
        print('Usage: rps.py [num_plays]')
