import Recipe
import Ingredient
import fractions

"""
Game class.

This class controls the Recipe and Ingredients that are used in each Game.
"""
class Game:

    VAMPIRE = Recipe.Recipe("Vampire", (Ingredient.Ingredient("Bat's Blood", 5) 
                                        Ingredient.Ingredient("Wolf Spit", 6),
                                        Ingredient.Ingredient("Foxglove Juice", 7),
                                        Ingredient.Ingredient("Quicksilver", 8)))

    """
    Initialize a Game object.

    Arguments:
    MainWindow window -- the Tk window that displays the game
    """
    def __init__(self, window):
        self.window = window

        # stores the fractions selected by the user in the game
        self.selection = []

        # stores the index of the next Ingredient to use
        self.nextIndex = 0


    """
    Sets the Recipe that is going to be used by the Game.

    Arguments:
    Recipe recipe -- an object that stores Ingredients used to make a Monster
    """
    def setRecipe(self, recipe):
        self.recipe = recipe

    """
    Returns the Recipe used by the Game.

    Returns:
    Recipe recipe -- the Recipe object used to make a Monster
    """
    def getRecipe(self):
        return self.recipe


    """
    Returns the next Ingredient object in the Recipe; if all Ingredients
    have been iterated through, calls the winFrame of the GUI window.

    Returns:
    Ingredient ingredient -- an Ingredient object
    """
    def getNextIngredient(self):
        if (self.nextIndex >= self.recipe.getSize()):
            self.window.winFrame()
        else:
            ingredient = self.recipe.getIngredients()[self.nextIndex]
            self.nextIndex += 1
            return ingredient


    """
    Plays a given Ingredient by calling the appropriate fractionFrame
    of the GUI window.

    Arguments:
    Ingredient ingredient -- the Ingredient object to be played
    """
    def playNextIngredient(self, ingredient):
        if ingredient:
            choices = ingredient.getChoices()
            self.window.fractionFrame(self, ingredient, choices)


    """
    Gets the first Ingredient from the Recipe and plays it.
    """
    def playRecipe(self):
        ingredient = self.getNextIngredient()
        self.playNextIngredient(ingredient)


    """
    Sets the self.selection attribute to the user-selected list of fractions
    and calls checkAnswer to see if user chose the correct combination.

    Called only by the fractionFrame when Enter button has been pressed.

    Arguments:
    Ingredient ingredient -- the Ingredient object to check selection against
    Fraction[] selection -- a list of Fraction objects that were selected by the user
    """
    def setSelection(self, ingredient, selection):
        self.selection = selection
        self.checkAnswer(ingredient)


    """
    Checks if the sum of the Fractions in self.selection is equal to the
    Fraction in the Ingredient.

    Arguments:
    Ingredient ingredient -- the Ingredient object which was played
    """
    def checkAnswer(self, ingredient):
        selection_sum = fractions.Fraction()
        for x in self.selection:
            selection_sum += x
        if selection_sum == ingredient.getFraction():
            self.window.correctMessage()
        else:
            self.window.incorrectMessage()
