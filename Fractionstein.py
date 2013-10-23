from Tkinter import *
import Game
import random

"""
Represents the Starting Frame of the Fractionstein GUI.
"""
class StartFrame(Frame):

    """
    Initialize the StartFrame.

    Arguments:
    MainWindow window -- the Window that houses the frame
    Tk parent -- the Tk() object that serves as this frame's parent
    """
    def __init__(self, window, parent):
        # set up the UI and save variables
        Frame.__init__(self, parent)

        self.window = window
        self.parent = parent

        self.parent.title("Dr. Fractionstein's Laboratory")
        self.pack(fill=BOTH, expand=1)

        background_image = PhotoImage(file="img/background_start.gif")
        background_label = Label(self, image=background_image)
        background_label.image = background_image;
        background_label.place(x=0, y=0, relwidth=1, relheight=1)

        # make the Start Game button -- goes to ChooseFrame
        def startGameFunc ():
            self.destroy()
            self.window.chooseFrame()

        startGame = Button(self,text="Start Game", command=startGameFunc)
        startGame.place(x=225, y=550)

        # make the Instructions button -- goes to InstructionsFrame
        def instructionsFunc ():
            self.destroy()
            self.window.instructionsFrame()

        instructions = Button(self, text="Instructions", command=instructionsFunc)
        instructions.place(x=450, y=550)

        # make the Quit button -- exits the window
        quitButton = Button(self, text="Quit", command=self.quit)
        quitButton.place(x=700, y=550)


"""
Represents the Instructions Frame of the Fractionstein GUI.
"""
class InstructionsFrame(Frame):

    """
    Initialize the InstructionsFrame.

    Arguments:
    MainWindow window -- the Window that houses the frame
    Tk parent -- the Tk() object that serves as this frame's parent
    """
    def __init__(self, window, parent):
        # set up the UI and save variables
        Frame.__init__(self, parent)

        self.window = window
        self.parent = parent

        self.parent.title("Dr. Fractionstein's Laboratory")
        self.pack(fill=BOTH, expand=1)

        background_image = PhotoImage(file="img/background_instructions.gif")
        background_label = Label(self, image=background_image)
        background_label.image = background_image;
        background_label.place(x=0, y=0, relwidth=1, relheight=1)

        # make the Back button -- goes to StartFrame
        def backFunc ():
            self.destroy()
            self.window.startFrame()

        backButton = Button(self, text="Back", command=backFunc)
        backButton.place(x=300, y=600)

        # make the Quit button -- exits the window
        quitButton = Button(self, text="Quit", command=self.quit)
        quitButton.place(x=650, y=600)

"""
Represents the Choose Frame of the Fractionstein GUI.

This is where the user is asked to choose which Recipe he or she
would like to play -- i.e. which Monster he or she would like to make.
"""
class ChooseFrame(Frame):

    """
    Initialize the ChooseFrame.

    Arguments:
    MainWindow window -- the Window that houses the frame
    Tk parent -- the Tk() object that serves as this frame's parent
    """
    def __init__(self, window, parent):
        # set up the UI and save variables
        Frame.__init__(self, parent)

        self.window = window
        self.parent = parent

        self.parent.title("Dr. Fractionstein's Laboratory")
        self.pack(fill=BOTH, expand=1)

        background_image = PhotoImage(file="img/background_choose.gif")
        background_label = Label(self, image=background_image)
        background_label.image = background_image;
        background_label.place(x=0, y=0, relwidth=1, relheight=1)

        # variable stores the value of the selected Monster radio button
        var = IntVar()

        # make the Vampire radio button
        vampire_image = PhotoImage(file="img/vampire_text.gif")
        vampire = Radiobutton(self, image=vampire_image,
                              variable=var, value=0)
        vampire.image = vampire_image
        vampire.place(relx=.3, rely=.4, anchor=CENTER)

        # make the Werewolf radio button
        werewolf_image = PhotoImage(file="img/werewolf_text.gif")
        werewolf = Radiobutton(self, image=werewolf_image,
                              variable=var, value=1)
        werewolf.image = werewolf_image
        werewolf.place(relx=.7, rely=.4, anchor=CENTER)

        # make the Zombie radio button
        zombie_image = PhotoImage(file="img/zombie_text.gif")
        zombie = Radiobutton(self, image=zombie_image,
                              variable=var, value=2)
        zombie.image = zombie_image
        zombie.place(relx=.3, rely=.6, anchor=CENTER)

        # make the Dragon radio button
        dragon_image = PhotoImage(file="img/dragon_text.gif")
        dragon = Radiobutton(self, image=dragon_image,
                               variable=var, value=3)
        dragon.image = dragon_image
        dragon.place(relx=.7, rely=.6, anchor=CENTER)

        # make the Enter button -- goes to FractionFrame
        # and starts playing the recipe of whichever Monster
        # radio button was selected
        def enterFunc():
            if var.get() == 0:
                monster = self.window.game.VAMPIRE
            elif var.get() == 1:
                monster = self.window.game.WEREWOLF
            elif var.get() == 2:
                monster = self.window.game.ZOMBIE
            elif var.get() == 3:
                monster = self.window.game.DRAGON

            self.destroy()
            self.window.game.setRecipe(monster)
            self.window.game.playRecipe()

        enterButton = Button(self, text="Enter", command=enterFunc)
        enterButton.place(relx=.3, rely=.8, anchor=CENTER)

        # make the Back button -- returns to StartFrame
        def backFunc():
            self.destroy()
            self.window.startFrame()

        quitButton = Button(self, text="Back", command=backFunc)
        quitButton.place(relx=.7, rely=.8, anchor=CENTER)

"""
Represents the Fraction Frame of the Fractionstein GUI.

This is where the user is asked to make a combination of fractions.
It is repeated once for every Ingredient in the Recipe being played.
"""
class FractionFrame(Frame):

    """
    Initialize the FractionFrame for this round.

    Arguments:
    MainWindow window -- the Window that houses the frame
    Tk parent -- the Tk() object that serves as this frame's parent
    Game game -- the Game object being played, which holds the Recipe
                 and all its Ingredients
    Ingredient ingredient -- the individual Ingredient being played
                             in this round
    """
    def __init__(self, window, parent, game, ingredient):
        # set up the UI and save variables
        Frame.__init__(self, parent)

        self.window = window
        self.parent = parent
        self.game = game
        self.ingredient = ingredient
        self.choices = ingredient.getChoices()

        self.parent.title("Dr. Fractionstein's Laboratory")
        self.pack(fill=BOTH, expand=1)

        background_image = PhotoImage(file="img/background_simple.gif")
        background_label = Label(self, image=background_image)
        background_label.image = background_image;
        background_label.place(x=0, y=0, relwidth=1, relheight=1)

        # display completion status of game at top
        status = Label(self, text="STATUS: " +
                       str(self.game.getCurrentIndex()) + " / " +
                       str(self.game.getRecipe().getSize()))
        status.place(x=900, y=10)

        # make the title at the top which gives the prompt fraction
        title = Label(self, text="What combination of flasks adds up to " +
                      str(self.ingredient.getFraction()) +
                      " flask of " + self.ingredient.getName() + "?")
        title.place(relx=0.5, y=50, anchor=CENTER)

        # variable stores the values of the selected Fraction checkbuttons
        self.var = [IntVar(), IntVar(), IntVar(), IntVar()]

        # choose a random flask shape and color to use for all Fractions
        # images in this frame
        this_flask = random.choice(["flask_", "flask2_"])
        this_color = random.choice(["_orange", "_green", "_red", "_purple"])
        img = []

        # select the correct flask fill size based on the Fraction
        # it represents and add the images for each Fraction to a list
        for i in self.choices:
            if i <= 0.25:
                this_fill = "low"
            elif i <= 0.5:
                this_fill = "half"
            elif i <= 0.75:
                this_fill = "partial"
            else:
                this_fill = "full"
            img.append(PhotoImage(file = "img/" + this_flask + this_fill + this_color + ".gif"))

        # make the first flask checkbutton
        flask0 = Checkbutton(self, image=img[0], text=str(self.choices[0]),
                             compound=RIGHT, variable = self.var[0])
        flask0.image = img[0]
        flask0.place(x=50, y=100)

        # make the second flask checkbutton
        flask1 = Checkbutton(self, image=img[1], text=str(self.choices[1]),
                             compound=RIGHT, variable = self.var[1])
        flask1.image = img[1]
        flask1.place(x=500, y=100)

        # make the third flask checkbutton
        flask2 = Checkbutton(self, image=img[2], text=str(self.choices[2]),
                             compound=RIGHT, variable = self.var[2])
        flask2.image = img[2]
        flask2.place(x=50, y=350)

        # make the fourth flask checkbutton
        flask3 = Checkbutton(self, image=img[3], text=str(self.choices[3]),
                             compound=RIGHT, variable = self.var[3])
        flask3.image = img[3]
        flask3.place(x=500, y=350)

        # make the Enter button -- saves the values of the Fractions selected
        # so that they can be checked
        enterButton = Button(self, text="Enter", command=self.enterFunc)
        enterButton.place(x=150, y=600)

        # make the Back button -- returns to StartFrame
        def backFunc():
            self.destroy()
            self.window.startFrame()

        backButton = Button(self, text="Back to Main Menu", command=backFunc)
        backButton.place(x=700, y=600)

    """
    Checks the value of the selected Fractions against the prompt Fraction
    to see if the user has chosen a correct combination.
    """
    def enterFunc(self):
        # the sum of all selected Fractions
        selection = 0
        # the index of the current Fraction
        index = 0

        for i in self.var:
            if i.get() == 1:
                # if the Fraction was selected, add the value of its Fraction
                # to selection
                selection += self.choices[index]
            index+=1

        # check the selection against the correct prompt Fraction and
        # call the correct message
        if selection == self.ingredient.getFraction():
            self.window.correctMessage()
        else:
            self.window.incorrectMessage()

    """
    Destroy the FractionFrame so that another Frame can replace it in
    the MainWindow.

    Used by incorrectMessage, and so must be accessible from the
    MainWindow class.
    """
    def destroyFrame(self):
        self.destroy()

    """
    Destroy the FractionFrame and start the process of creating a new
    FractionFrame for the next ingredient to be used.
    """
    def nextIngredient(self):
        self.destroy()
        self.game.playNextIngredient(self.game.getNextIngredient())


"""
Represents the Explosion Frame of the Fractionstein GUI.

This simple frame consists of just an "explosion" image which
replaces the FractionFrame whenever the user has given too many
incorrect answers.
"""
class ExplodeFrame(Frame):

    """
    Initialize the ExplodeFrame.

    Arguments:
    MainWindow window -- the Window that houses the frame
    Tk parent -- the Tk() object that serves as this frame's parent
    """
    def __init__(self, window, parent):
        # start the UI and save variables
        Frame.__init__(self, parent)

        self.window = window
        self.parent = parent

        self.parent.title("Dr. Fractionstein's Laboratory")
        self.pack(fill=BOTH, expand=1)

        background_image = PhotoImage(file="img/background_explode.gif")
        background_label = Label(self, image=background_image)
        background_label.image = background_image;
        background_label.place(x=0, y=0, relwidth=1, relheight=1)

    """
    Destroy the ExplodeFrame so that it can be replaced in the MainWindow
    """
    def destroyFrame(self):
        self.destroy()

"""
Represents the Win Frame of the Fractionstein GUI.

This frame displays the image of whatever Monster the user was creating
and options to start a new game or quit.
"""
class WinFrame(Frame):

    """
    Initialize the WinFrame.

    Arguments:
    MainWindow window -- the Window that houses the frame
    Tk parent -- the Tk() object that serves as this frame's parent
    """
    def __init__(self, window, parent):
        # set up the UI and save variables
        Frame.__init__(self, parent)

        self.window = window
        self.parent = parent

        self.parent.title("Dr. Fractionstein's Laboratory")
        self.pack(fill=BOTH, expand=1)

        background_image = PhotoImage(file="img/background_win.gif")
        background_label = Label(self, image=background_image)
        background_label.image = background_image;
        background_label.place(x=0, y=0, relwidth=1, relheight=1)

        # make the Mosnter image
        monster = self.window.game.getRecipe().getMonster()
        monster_image = PhotoImage(file="img/" + monster + ".gif")
        monster_label = Label(self, image=monster_image)
        monster_label.image = monster_image
        monster_label.place(x=100, y=100)

        # make the Back button -- returns to StartFrame
        def backFunc ():
            self.destroy()
            self.window.startFrame()

        backButton = Button(self, text="Start Over", command=backFunc)
        backButton.place(x=650, y=500)

        # make the Quit button -- exits the window
        quitButton = Button(self, text="Quit", command=self.quit)
        quitButton.place(x=650, y=550)


"""
Represents the window which displays the Fractionstein GUI.
"""
class MainWindow:

    """
    Initialize the MainWindow.
    """
    def __init__ (self):
        # set up the GUI window
        self.root = Tk()
        self.root.geometry("1000x700+150+0")
        self.root.resizable(width=FALSE, height=FALSE)

        # number of warnings for incorrect answers that have been issued
        self.warningsIssued = 0

        # number of warnings allowed before an explosion
        self.warningsAllowed = 2

    """
    Start the main loop of the Tk object.
    """
    def main_loop (self):
        self.root.mainloop()

    """
    Set the Game object to play.
    """
    def setGame (self, game):
        self.game = game

    """
    Make the window display the StartFrame.
    """
    def startFrame (self):
        app = StartFrame(self, self.root)

    """
    Make the window display the InstructionsFrame.
    """
    def instructionsFrame (self):
        app = InstructionsFrame(self, self.root)

    """
    Make the window display the ChooseFrame.
    """
    def chooseFrame (self):
        app = ChooseFrame(self, self.root)

    """
    Make the window display the FractionFrame.
    """
    def fractionFrame (self, game, ingredient):
        # save the FractionFrame object so that it can be used
        # in the incorrectMessage method
        self.fracFrame = FractionFrame(self, self.root, game, ingredient)
        app = self.fracFrame

    """
    Make the window display the WinFrame.
    """
    def winFrame (self):
        app = WinFrame(self, self.root)

    """
    Respond to a correct answer in the game by playing the next Ingredient.
    """
    def correctMessage (self):
        self.fracFrame.nextIngredient()

    """
    Respond to an incorrect answer in the game.

    If there are still warnings left, issue a warning and allow the user
    to try the FractionFrame again.

    If the number of allowed warnings have already been issued, replace
    the FractionFrame with the ExplodeFrame and force the user to start over.
    """
    def incorrectMessage (self):
        # set up the UI for a message window
        self.top = Toplevel(self.root)
        self.top.geometry("400x100+400+200")

        # if there are still warnings left, display a warning message
        if self.warningsIssued < self.warningsAllowed:
            # increment the number of warning issued
            self.warningsIssued += 1

            # make the warning message and display
            warning = Message(self.top,
                              text="Are you sure that's correct? Try again",
                              width=350)
            warning.place(relx=0.5, rely=0.25, anchor=CENTER)

            # make the TryAgain button -- removes the warning message
            # and allows the user to access the FractionFrame again
            tryAgain = Button(self.top,
                              text="Try Again",
                              command=self.top.destroy)
            tryAgain.place(relx=0.5, rely=0.75, anchor=CENTER)

        # if the number of allowed warnings have been issued, display the
        # ExplodeFrame and force the user to start over
        else:
            # replace the FractionFrame with the ExplodeFrame
            self.fracFrame.destroyFrame()
            self.explodeFrame = ExplodeFrame(self, self.root)
            app = self.explodeFrame

            # make the explosion message and display
            warning = Message(self.top,
                              text="OH NO! You added the wrong amount and the potion exploded.",
                              width=350)
            warning.place(relx=0.5, rely=0.25, anchor=CENTER)

            # make the startOver button -- returns to StartFrame
            def startOverFunction():
                self.top.destroy()
                self.explodeFrame.destroyFrame()
                self.warningsIssued = 0
                self.startFrame()

            startOver = Button(self.top,
                              text="Start Over",
                              command=startOverFunction)
            startOver.place(relx=0.5, rely=0.75, anchor=CENTER)

        # make the MainWindow wait until the message window has been resolved
        self.root.wait_window(self.top)


"""
Starts the main window.
"""
def startWindow():
    window = MainWindow()
    g = Game.Game(window)
    window.setGame(g)
    window.startFrame()
    window.main_loop()

startWindow()
