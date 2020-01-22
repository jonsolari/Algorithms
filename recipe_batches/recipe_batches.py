#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
    rec = list(recipe.values())
    ing = list(ingredients.values())
    
    if list(recipe.keys()) != list(ingredients.keys()):
        return 0
    res = {rec[i]: ing[i] for i in range(0, len(rec))}
    diff1 = []
    for key, value in res.items():
        if int(value) // int(key) >= 1:
            diff1.append(int(value // int(key)))
    if len(diff1) == len(recipe.keys()):
        return int(min(diff1))
    else:
        return 0
        
    

if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 10 }
  ingredients = { 'milk': 198, 'butter': 52, 'flour': 10 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))