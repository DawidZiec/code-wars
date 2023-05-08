'''
Pete likes to bake some cakes. He has some recipes and ingredients.
Unfortunately he is not good in maths.
Can you help him to find out, how many cakes he could bake considering his recipes?

Write a function cakes(), which takes the recipe (object) and the available ingredients
(also an object) and returns the maximum number of cakes Pete can bake (integer).
For simplicity there are no units for the amounts
(e.g. 1 lb of flour or 200 g of sugar are simply 1 or 200).
Ingredients that are not present in the objects, can be considered as 0.

Examples:

# must return 2
cakes({flour: 500, sugar: 200, eggs: 1}, {flour: 1200, sugar: 1200, eggs: 5, milk: 200})
# must return 0
cakes({apples: 3, flour: 300, sugar: 150, milk: 100, oil: 100}, {sugar: 500, flour: 2000, milk: 2000})
'''

# examples above are missing quotes in the dicts


def cakes(recipe, available):
    # case 1: check if there are more recipe ingredients than available ingridients
    # if that's the case, 0 cakes can ba made
    if len(recipe) > len(available):
        print("0 first case")
        return 0
    # case 2: check if every recipe ingredient is available
    # if not, 0 cakes can be made
    recipe_list, available_list = [], []
    for key in recipe:
        recipe_list.append(key)
    for key in available:
        available_list.append(key)
    for ingredient in recipe_list:
        if (ingredient in available_list):
            pass
        else:
            print("0 second case")
            return 0
    # case 3: check if there are enough ingredients to make a cake


cakes({"flour": 500, "sugar": 200, "eggs": 1}, {
      "flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200})
