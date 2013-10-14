import random

"""
Ingredient class.

Each Ingredient object functions as a factory, with a set name
and denominator that is used for every Ingredient. When using
an Ingredient in a Recipe, call the getRandomAmount method
on each Ingredient; that returns the fraction to use.
"""
class Ingredient:
    """
    Initialize an Ingredient object.

    Arguments:
    str name -- the name of the Ingredient
    int denom -- the denominator of the Ingredient's amount
    """
    def __init__(self, name, denom):
        if (type(name) is not str):
            raise Exception ("Expected string for name argument; got " + str(type(name)))
        if (type(denom) is not int):
            raise Exception ("Expected integer for denom argument; got " + str(type(denom)))
        self.name = name
        self.denom = denom


    """
    Return the name of the Ingredient.

    Returns:
    str name -- the name of the Ingredient
    """
    def getName (self):
        return self.name


    """
    Return the denominator of the Ingredient.

    Returns:
    int denom -- the denominator of the Ingredient
    """
    def getDenominator (self):
        return self.denom


    """
    Return a random fraction to use as the Ingredient's amount.

    Returns:
    (int, int) fraction -- a tuple of integers that represent numerator and denominator
    """
    def getRandomAmount (self):
        num = random.choice(range(1, self.denom))
        return (num, self.denom)
