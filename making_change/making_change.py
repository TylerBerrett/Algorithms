#!/usr/bin/python

import sys

# pennies, nickels, dimes, quarters, and half-dollars
# inf supply of coinage
# take in amount of money in cents and list of different coins


# keep previous values
# make list == amount
# populate cache


cents = [1, 5, 10, 25, 50]


def making_change(amount, denominations):
    cache = [0 for i in range(amount + 1)]
    cache[0] = 1

    # use this to populate cache
    for coin in denominations:
        for higher_amount in range(coin, amount + 1):  # coin 1 # amount 10
            cache[higher_amount] += cache[higher_amount - coin]

    return cache[amount]

if __name__ == "__main__":
    # Test our your implementation from the command line
    # with `python making_change.py [amount]` with different amounts
    if len(sys.argv) > 1:
        denominations = [1, 5, 10, 25, 50]
        amount = int(sys.argv[1])
        print("There are {ways} ways to make {amount} cents.".format(ways=making_change(amount, denominations),
                                                                     amount=amount))
    else:
        print("Usage: making_change.py [amount]")
