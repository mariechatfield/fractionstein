from Tkinter import *
import Game

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


        flask0 = Checkbutton(self, text=str(self.choices[0]),
                             variable = self.var[0], command=self.onClick)
        flask0.place(x=50, y=50)

        flask1 = Checkbutton(self, text=str(self.choices[1]),
                             variable = self.var[1], command=self.onClick)
        flask1.place(x=500, y=50)

        flask2 = Checkbutton(self, text=str(self.choices[2]),
                             variable = self.var[2], command=self.onClick)
        flask2.place(x=50, y=300)

        flask3 = Checkbutton(self, text=str(self.choices[3]),
                             variable = self.var[3], command=self.onClick)
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
        self.destroy()
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
        self.root.geometry("1000x800+150+100")

    def main_loop (self):
        self.root.mainloop()

    def fractionFrame (self, game, ingredient, choices):
        app = FractionFrame(self.root, game, ingredient, choices)

    def winFrame (self):
        app = WinFrame(self.root)

    #TODO
    def correctMessage (self):
        pass

    #TODO
    def incorrectMessage (self):
        pass

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
