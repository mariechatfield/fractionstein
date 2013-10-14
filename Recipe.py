import Ingredient

"""
Recipe class.

Each Recipe has a tuple of Ingredients that are used to create
a Monster.
"""
class Recipe:
    """
    Initialize a Recipe object.

    Arguments:
    str monster -- the name of the Monster the Recipe is for
    tuple ingredients -- a tuple of Ingredient objects used in the Recipe
    """
    def __init__(self, monster, ingredients):
        if (type(monster) is not str):
            raise Exception ("Expected string for monster argument; got " + str(type(name)))
        if (type(ingredients) is not tuple):
            raise Exception ("Expected tuple for ingredients; got " + str(type(ingredients)))
        for i in ingredients:
            if (not isinstance(i, Ingredient.Ingredient)):
                raise Exception ("Expected tuple of Ingredients for ingredients; got tuple with objects of " + str(type(i)))
        self.monster = monster
        self.ingredients = ingredients
        self.size = len(self.ingredients)
        self.iterPointer = 0


    """
    Return the Monster that the Recipe makes.

    Returns:
    str monster -- the Monster that the Recipe makes
    """
    def getMonster(self):
        return self.monster

    """
    Return the tuple of Ingredients used in the Recipe.

    Returns:
    tuple ingredients -- a tuple of Ingredients that are used in the Recipe
    """
    def getIngredients(self):
        return self.Ingredients


    """
    Return the number of Ingredients used in the Recipe.

    Returns:
    int size -- the lenght of the tuple of Ingredients
    """
    def getIngredients(self):
        return self.size


    """
    Implements an iterator for Recipe.

    Returns:
    iter self -- the iterator object
    """
    def __iter__(self):
        return self

    """
    Provides the next Ingredient in Recipe's iterator.

    Returns:
    Ingredient nextIng -- the next Ingredient in the iterator
    """
    def next(self):
        if self.iterPointer >= self.size:
            raise StopIteration
        nextIng = self.ingredients[self.iterPointer]
        self.iterPointer += 1
        return nextIng
