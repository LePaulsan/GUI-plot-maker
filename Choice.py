from tkinter import Button, Entry

class Choice:
    def __init__(self, surface, row, choiceList, name="", connect=""):
        self.name = name
        self.connectTo = connect

        self.button = Button(surface, text="-", command=lambda: self.removeSelf(choiceList))
        self.button.grid(row=row, column=0)

        self.entry = Entry(surface)
        self.entry.grid(row=row, column=1)

    def setName(self, str):
        self.name = str

    def removeSelf(self, tempL):
        tempL.remove(self)