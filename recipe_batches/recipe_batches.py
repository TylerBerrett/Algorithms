#!/usr/bin/python

import math


# Takes in a recipe and in the form of a dictionary
# Takes in ingredients and in the form of a dictionary
# keys will be the ingredient names
# output must be how many times you can make the recipe complete

# get matching names
# check how many times it can do that one ingredient add to array
# return smallest element in array

def recipe_batches(recipe, ingredients):
    batches = float('inf')
    for item in recipe:
        try:
            recipe_amount = recipe[item]
            ingredients_amount = ingredients[item]
            compare = ingredients_amount // recipe_amount
            if compare < batches:
                batches = compare

        except KeyError:
            return 0

    return batches


if __name__ == '__main__':
    # Change the entries of these dictionaries to test
    # your implementation with different inputs
    recipe = {'milk': 100, 'butter': 50, 'flour': 5}
    ingredients = {'milk': 132, 'butter': 48, 'flour': 51}
    print("{batches} batches can be made from the available ingredients: {ingredients}.".format(
        batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
