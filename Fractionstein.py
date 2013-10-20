from Tkinter import *
import Game
import random

class FractionFrame(Frame):

    def __init__(self, parent, game, ingredient, choices):
        Frame.__init__(self, parent)

        self.parent = parent
        self.game = game
        self.ingredient = ingredient
        self.choices = choices

        self.initUI()

    def initUI(self):
        self.parent.title("Dr. Fractionstein's Laboratory")
        self.pack(fill=BOTH, expand=1)
        title = Label(self, text="Measure Out " +
                      str(self.ingredient.getFraction()) +
                      " Flask of " + self.ingredient.getName())
        title.place(x=400, y=25)

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
        flask0.place(x=50, y=50)

        flask1 = Checkbutton(self, image=img[1], text=str(self.choices[1]),
                             compound=RIGHT,
                             variable = self.var[1], command=self.onClick)
        flask1.image = img[1]
        flask1.place(x=500, y=50)

        flask2 = Checkbutton(self, image=img[2], text=str(self.choices[2]),
                             compound=RIGHT,
                             variable = self.var[2], command=self.onClick)
        flask2.image = img[2]
        flask2.place(x=50, y=300)

        flask3 = Checkbutton(self, image=img[3], text=str(self.choices[3]),
                             compound=RIGHT,
                             variable = self.var[3], command=self.onClick)
        flask3.image = img[3]
        flask3.place(x=500, y=300)

        enterButton = Button(self, text="Enter", command=self.enter)
        enterButton.place(x=150, y=550)

        quitButton = Button(self, text="Quit", command=self.quit)
        quitButton.place(x=700, y=550)

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

    def __init__(self, parent):
        Frame.__init__(self, parent)

        self.parent = parent
        self.initUI()

    def initUI(self):
        self.parent.title("Dr. Fractionstein's Laboratory -- YOU WIN")
        self.pack(fill=BOTH, expand=1)

        # TODO


class MainWindow:
    def main (self):
        self.root = Tk()
        self.root.geometry("1000x800+150+50")
        self.warning = True

    def main_loop (self):
        self.root.mainloop()

    def startFrame (self):
        # TODO
        pass

    def fractionFrame (self, game, ingredient, choices):
        self.fracFrame = FractionFrame(self.root, game, ingredient, choices)
        app = self.fracFrame

    def winFrame (self):
        app = WinFrame(self.root)

    #TODO
    def correctMessage (self):
        self.fracFrame.nextIngredient()

    #TODO
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
            warning = Message(self.top,
                              text="OH NO! You added the wrong amount and the potion exploded.",
                              width=350)
            warning.place(relx=0.5, rely=0.25, anchor=CENTER)

            def startOverFunction():
                self.top.destroy()
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
    # TODO: should call a startFrame to get a Recipe
    # the startFrame can then call g.setRecipe() and g.playRecipe()
    g.setRecipe(g.VAMPIRE)
    g.playRecipe()
    window.main_loop()

startWindow()
