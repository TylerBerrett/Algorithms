#!/usr/bin/python

import argparse


# buying and selling amazon stock

# receives a list of stock prices

# should return the maximum profit that can be made from a singe by and sell

# lowest value

# biggest value

# biggest difference

# [99, 124, 47, 48, 125]
# l = 99
# h = 124
# diff = 25
# l = 47
# h = 125
# if diff > 78 Nothing else diff = 78
# return diff


def find_max_profit(prices):
    lowest = float('inf')
    profit = -lowest

    for i in range(0, len(prices)):
        price = prices[i]
        if profit < price - lowest:
            profit = price - lowest
        if price < lowest:
            lowest = price

    return profit

if __name__ == '__main__':
    # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(description='Find max profit from prices.')
    parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
    args = parser.parse_args()

    print("A profit of ${profit} can be made from the stock prices {prices}.".format(
        profit=find_max_profit(args.integers), prices=args.integers))
