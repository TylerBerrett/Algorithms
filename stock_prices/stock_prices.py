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
    lowest = prices[0]
    highest = prices[len(prices) - 1]
    highest_index = len(prices)

    for i in range(0, len(prices)):
        price = prices[i]
        print(price, i)
        if price < lowest and i <= highest_index:
            lowest = price
        elif price > highest and i > 0:
            highest = price
            highest_index = i

    return highest - lowest


test1 = [1050, 270, 1540, 3800, 2]
test2 = [10, 7, 5, 8, 11, 9]
test3 = [100, 55, 4, 98, 10, 18, 90, 95, 43, 11, 47, 67, 89, 42, 49, 79]
print(find_max_profit(test3))

if __name__ == '__main__':
    # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(description='Find max profit from prices.')
    parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
    args = parser.parse_args()

    print("A profit of ${profit} can be made from the stock prices {prices}.".format(
        profit=find_max_profit(args.integers), prices=args.integers))
