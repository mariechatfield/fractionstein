import Recipe
import Ingredient
import fractions

"""
Game class.

This class controls the Recipe and Ingredients that are used in each Game.
"""
class Game:

    # Vampire Monster - 4 Fractions (Easy)
    VAMPIRE = Recipe.Recipe("vampire", (Ingredient.Ingredient("Bat's Blood", 5), 
                                        Ingredient.Ingredient("Wolf Spit", 6),
                                        Ingredient.Ingredient("Foxglove Juice", 7),
                                        Ingredient.Ingredient("Quicksilver", 8)))

    # Werewolf Monster - 6 Fractions (Medium)
    WEREWOLF = Recipe.Recipe("werewolf", (Ingredient.Ingredient("Moon Cheese", 5),
                                          Ingredient.Ingredient("Wolf Spit", 6),
                                          Ingredient.Ingredient("Toad Venom", 7),
                                          Ingredient.Ingredient("Bat's Blood", 8),
                                          Ingredient.Ingredient("Hemlock Root", 9),
                                          Ingredient.Ingredient("Silver Fur", 10)))

    # Zombie Monster - 8 Fractions (Hard)
    ZOMBIE = Recipe.Recipe("zombie", (Ingredient.Ingredient("Toad Venom", 5),
                                      Ingredient.Ingredient("Monkey Sweat", 6),
                                      Ingredient.Ingredient("Quicksilver", 7),
                                      Ingredient.Ingredient("Hemlock Root", 8),
                                      Ingredient.Ingredient("Wolf Spit", 9),
                                      Ingredient.Ingredient("Bat's Blood", 10),
                                      Ingredient.Ingredient("Foxglove Juice", 12),
                                      Ingredient.Ingredient("Fresh Brains", 15)))

    # Dragon Monster - 10 Fractions (Challenge)
    DRAGON = Recipe.Recipe("dragon", (Ingredient.Ingredient("Foxglove Juice", 5),
                                      Ingredient.Ingredient("Quicksilver", 6),
                                      Ingredient.Ingredient("Serpent Milk", 7),
                                      Ingredient.Ingredient("Wolf Spit", 8),

                                      Ingredient.Ingredient("Monkey Sweat", 9),
                                      Ingredient.Ingredient("Lion Tears", 10),
                                      Ingredient.Ingredient("Crocodile Scales", 12),
                                      Ingredient.Ingredient("Bat's Blood", 15),
                                      Ingredient.Ingredient("Gold Dust", 16),
                                      Ingredient.Ingredient("Liquid Fire", 20)))

    """

    Initialize a Game object.

    Arguments:
    MainWindow window -- the Tk window that displays the game
    """
    def __init__(self, window):
        self.window = window

        # stores the fractions selected by the user in the game
        self.selection = []


    """
    Sets the Recipe that is going to be used by the Game.

    Arguments:
    Recipe recipe -- an object that stores Ingredients used to make a Monster
    """
    def setRecipe(self, recipe):
        self.recipe = recipe

        # stores the index of the next Ingredient to use
        self.nextIndex = 0

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
            self.window.fractionFrame(self, ingredient)


    """
    Gets the first Ingredient from the Recipe and plays it.
    """
    def playRecipe(self):
        ingredient = self.getNextIngredient()
        self.playNextIngredient(ingredient)
