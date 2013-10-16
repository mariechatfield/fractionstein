import random
import fractions

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

        # choose a random numerator from the range 2 - denom
        temp = range(2, self.denom)
        random.shuffle(temp)
        self.num = random.choice(temp)


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
    Return the numerator of the Ingredient.

    Returns:
    int num -- the numerator of the Ingredient
    """
    def getNumerator (self):
        return self.num

    """
    Return the Fraction representation of the Ingredient's amount.

    Returns:
    Fraction fraction -- the Fraction represented by num / denom
    """
    def getFraction (self):
        return fractions.Fraction(self.num, self.denom)

    """
    Return a list of 4 choices that the user will select from to match
    the Ingredient's Fraction. These choices are guaranteed to have
    at least one combination (of either 2 or 3 fractions) that will add up to
    the Fraction of the Ingredient.

    Returns:
    Fraction[] choices -- a list of four random Fractions to choose from
    """
    def getChoices (self):
        choices = []
        # make sure that the fraction itself cannot be a possible choice
        allOptions = range(1, self.denom)
        allOptions.remove(self.num)

        # first choose a random number between 1 and the numerator
        optionsLessThanNum = range(1, self.num)
        choices.append(random.choice(optionsLessThanNum))
        # do not allow this first option to appear twice
        allOptions.remove(choices[0])
        optionsLessThanNum.remove(choices[0])

        # if there are more numbers between 1 and the numerator,
        # add another as a possible choice
        if optionsLessThanNum:
            choices.append(random.choice(optionsLessThanNum))
            # if the first two choices do not sum up to the numerator,
            # add the difference between numerator and the first choice.
            if (choices[0] + choices[1]) != self.num:
                choices.append(self.num - choices[0])
            # else, add a random option to make sure that three choices
            # have been added by this point
            else:
                choices.append(random.choice(allOptions))
        # if there are no more numbers between 1 and the numerator,
        # add the difference between the numerator and the first choice
        # to make the winning combination, plus a random option to make
        # sure that three choices have been added by this point
        else:
            choices.append(self.num - choices[0])
            choices.append(random.choice(allOptions))

        # if the third choice is still in allOptions, remove it
        # to prevent excessive duplicates; then add one more random option
        if choices[2] in allOptions:
            allOptions.remove(choices[2])
        choices.append(random.choice(allOptions))

        # convert each number in choices to be a Fraction; shuffle and return
        for i in range(len(choices)):
            choices[i] = fractions.Fraction(choices[i], self.denom)
        random.shuffle(choices)
        return choices
