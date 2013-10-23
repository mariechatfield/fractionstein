from Tkinter import *
import Game
import random

class FractionFrame(Frame):

    def __init__(self, window, parent, game, ingredient, choices):
        Frame.__init__(self, parent)

        self.window = window
        self.parent = parent
        self.game = game
        self.ingredient = ingredient
        self.choices = choices

        self.initUI()

    def initUI(self):
        self.parent.title("Dr. Fractionstein's Laboratory")
        self.pack(fill=BOTH, expand=1)

        background_image = PhotoImage(file="img/background_simple.gif")
        background_label = Label(self, image=background_image)
        background_label.image = background_image;
        background_label.place(x=0, y=0, relwidth=1, relheight=1)

        title = Label(self, text="What combination of flasks adds up to " +
                      str(self.ingredient.getFraction()) +
                      " flask of " + self.ingredient.getName() + "?")
        title.place(relx=0.5, y=50, anchor=CENTER)

        self.var = [IntVar(), IntVar(), IntVar(), IntVar()]

        this_flask = random.choice(["flask_", "flask2_"])
        this_color = random.choice(["_orange", "_green", "_red", "_purple"])
        img = []

        for i in self.choices:
            if i < 0.3:
                this_fill = "low"
            elif i > 0.6:
                this_fill = "full"
            else:
                this_fill = "partial"
            img.append(PhotoImage(file = "img/" + this_flask + this_fill + this_color + ".gif"))


        flask0 = Checkbutton(self, image=img[0], text=str(self.choices[0]),
                             compound=RIGHT,
                             variable = self.var[0], command=self.onClick)
        flask0.image = img[0]
        flask0.pack()
        flask0.place(x=50, y=100)

        flask1 = Checkbutton(self, image=img[1], text=str(self.choices[1]),
                             compound=RIGHT,
                             variable = self.var[1], command=self.onClick)
        flask1.image = img[1]
        flask1.place(x=500, y=100)

        flask2 = Checkbutton(self, image=img[2], text=str(self.choices[2]),
                             compound=RIGHT,
                             variable = self.var[2], command=self.onClick)
        flask2.image = img[2]
        flask2.place(x=50, y=350)

        flask3 = Checkbutton(self, image=img[3], text=str(self.choices[3]),
                             compound=RIGHT,
                             variable = self.var[3], command=self.onClick)
        flask3.image = img[3]
        flask3.place(x=500, y=350)

        enterButton = Button(self, text="Enter", command=self.enter)
        enterButton.place(x=150, y=600)

        def backFunc():
            self.destroy()
            self.window.startFrame()

        quitButton = Button(self, text="Back to Main Menu", command=backFunc)
        quitButton.place(x=700, y=600)

    def onClick(self):
        pass

    def enter(self):
        selection = []
        x = 0
        for i in self.var:
            if i.get() == 1:
                selection.append(self.choices[x])
            x+=1
        self.game.setSelection(self.ingredient, selection)

    def destroyFrame(self):
        self.destroy()

    def nextIngredient(self):
        self.destroyFrame()
        self.game.playNextIngredient(self.game.getNextIngredient())


class WinFrame(Frame):

    def __init__(self, window, parent):
        Frame.__init__(self, parent)

        self.window = window
        self.parent = parent
        self.initUI()

    def initUI(self):
        self.parent.title("Dr. Fractionstein's Laboratory")
        self.pack(fill=BOTH, expand=1)

        background_image = PhotoImage(file="img/background_win.gif")
        background_label = Label(self, image=background_image)
        background_label.image = background_image;
        background_label.place(x=0, y=0, relwidth=1, relheight=1)

        monster = self.window.game.getRecipe().getMonster()
        monster_image = PhotoImage(file="img/" + monster + ".gif")
        monster_label = Label(self, image=monster_image)
        monster_label.image = monster_image
        monster_label.place(x=100, y=100)

        def backFunc ():
            self.destroy()
            self.window.startFrame()

        backButton = Button(self, text="Start Over", command=backFunc)
        backButton.place(x=650, y=500)

        quitButton = Button(self, text="Quit", command=self.quit)
        quitButton.place(x=650, y=550)


class StartFrame(Frame):

    def __init__(self, window, parent):
        Frame.__init__(self, parent)

        self.window = window
        self.parent = parent
        self.initUI()

    def initUI(self):
        self.parent.title("Dr. Fractionstein's Laboratory")
        self.pack(fill=BOTH, expand=1)

        background_image = PhotoImage(file="img/background_start.gif")
        background_label = Label(self, image=background_image)
        background_label.image = background_image;
        background_label.place(x=0, y=0, relwidth=1, relheight=1)

        def startGameFunc ():
            self.destroy()
            self.window.chooseFrame()

        startGame = Button(self,text="Start Game", command=startGameFunc)
        startGame.place(x=225, y=550)

        def instructionsFunc ():
            self.destroy()
            self.window.instructionsFrame()

        instructions = Button(self, text="Instructions", command=instructionsFunc)
        instructions.place(x=450, y=550)

        quitButton = Button(self, text="Quit", command=self.quit)
        quitButton.place(x=700, y=550)

class InstructionsFrame(Frame):

    def __init__(self, window, parent):
        Frame.__init__(self, parent)

        self.window = window
        self.parent = parent
        self.initUI()

    def initUI(self):
        self.parent.title("Dr. Fractionstein's Laboratory")
        self.pack(fill=BOTH, expand=1)

        background_image = PhotoImage(file="img/background_instructions.gif")
        background_label = Label(self, image=background_image)
        background_label.image = background_image;
        background_label.place(x=0, y=0, relwidth=1, relheight=1)

        def backFunc ():
            self.destroy()
            self.window.startFrame()

        backButton = Button(self, text="Back", command=backFunc)
        backButton.place(x=300, y=600)

        quitButton = Button(self, text="Quit", command=self.quit)
        quitButton.place(x=650, y=600)


class ChooseFrame(Frame):

    def __init__(self, window, parent):
        Frame.__init__(self, parent)

        self.window = window
        self.parent = parent
        self.initUI()

    def initUI(self):
        self.parent.title("Dr. Fractionstein's Laboratory")
        self.pack(fill=BOTH, expand=1)

        background_image = PhotoImage(file="img/background_choose.gif")
        background_label = Label(self, image=background_image)
        background_label.image = background_image;
        background_label.place(x=0, y=0, relwidth=1, relheight=1)

        var = IntVar()

        vampire_image = PhotoImage(file="img/vampire_text.gif")
        vampire = Radiobutton(self, image=vampire_image,
                              variable=var, value=0)
        vampire.image = vampire_image
        vampire.place(relx=.3, rely=.4, anchor=CENTER)

        werewolf_image = PhotoImage(file="img/werewolf_text.gif")
        werewolf = Radiobutton(self, image=werewolf_image,
                              variable=var, value=1)
        werewolf.image = werewolf_image
        werewolf.place(relx=.7, rely=.4, anchor=CENTER)

        zombie_image = PhotoImage(file="img/zombie_text.gif")
        zombie = Radiobutton(self, image=zombie_image,
                              variable=var, value=2)
        zombie.image = zombie_image
        zombie.place(relx=.3, rely=.6, anchor=CENTER)

        dragon_image = PhotoImage(file="img/dragon_text.gif")
        dragon = Radiobutton(self, image=dragon_image,
                               variable=var, value=3)
        dragon.image = dragon_image
        dragon.place(relx=.7, rely=.6, anchor=CENTER)

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

        def backFunc():
            self.destroy()
            self.window.startFrame()

        quitButton = Button(self, text="Back", command=backFunc)
        quitButton.place(relx=.7, rely=.8, anchor=CENTER)

class ExplodeFrame(Frame):

    def __init__(self, window, parent):
        Frame.__init__(self, parent)

        self.window = window
        self.parent = parent
        self.initUI()

    def initUI(self):
        self.parent.title("Dr. Fractionstein's Laboratory")
        self.pack(fill=BOTH, expand=1)

        background_image = PhotoImage(file="img/background_explode.gif")
        background_label = Label(self, image=background_image)
        background_label.image = background_image;
        background_label.place(x=0, y=0, relwidth=1, relheight=1)

    def destroyFrame(self):
        self.destroy()


class MainWindow:
    def main (self):
        self.root = Tk()
        self.root.geometry("1000x700+150+0")
        self.root.resizable(width=FALSE, height=FALSE)
        self.warning = True

    def main_loop (self):
        self.root.mainloop()

    def setGame (self, game):
        self.game = game

    def startFrame (self):
        app = StartFrame(self, self.root)

    def instructionsFrame (self):
        app = InstructionsFrame(self, self.root)

    def chooseFrame (self):
        app = ChooseFrame(self, self.root)

    def fractionFrame (self, game, ingredient, choices):
        self.fracFrame = FractionFrame(self, self.root, game, ingredient, choices)
        app = self.fracFrame

    def winFrame (self):
        app = WinFrame(self, self.root)

    def correctMessage (self):
        self.fracFrame.nextIngredient()

    def incorrectMessage (self):
        self.top = Toplevel(self.root)
        self.top.geometry("400x100+400+200")

        if self.warning:
            self.warning = False
            warning = Message(self.top,
                              text="Are you sure that's correct? Try again",
                              width=350)
            warning.place(relx=0.5, rely=0.25, anchor=CENTER)
            tryAgain = Button(self.top,
                              text="Try Again",
                              command=self.top.destroy)
            tryAgain.place(relx=0.5, rely=0.75, anchor=CENTER)
        else:
            self.fracFrame.destroyFrame()
            self.explodeFrame = ExplodeFrame(self, self.root)
            app = self.explodeFrame
            warning = Message(self.top,
                              text="OH NO! You added the wrong amount and the potion exploded.",
                              width=350)
            warning.place(relx=0.5, rely=0.25, anchor=CENTER)

            def startOverFunction():
                self.top.destroy()
                self.explodeFrame.destroyFrame()
                self.warning = True
                self.startFrame()

            startOver = Button(self.top,
                              text="Start Over",
                              command=startOverFunction)
            startOver.place(relx=0.5, rely=0.75, anchor=CENTER)

        self.root.wait_window(self.top)


"""
Starts the main window.
"""
def startWindow():
    window = MainWindow()
    window.main()
    g = Game.Game(window)
    window.setGame(g)
    window.startFrame()
    window.main_loop()

startWindow()
