from tkinter import LabelFrame, Button, Toplevel
from Choice import Choice
from Entrybox import EntryBox
from Textbox import TextBox

class Sence:
    def __init__(self, globList):
        # Create the main window
        self.win = Toplevel()
        self.win.title("New sence")

        # Create the frame for data and choices
        self.dataFrame = LabelFrame(self.win, text="Data")
        self.dataFrame.pack()
        self.choiceFrame = LabelFrame(self.win, text="Choices")
        self.choiceFrame.pack()

        # Name is just an easy way for the maker to refer to
        self.name = EntryBox(self.dataFrame, "Name", 0)
        self.des = EntryBox(self.dataFrame, "Des", 1)

        # Add choices
        Button(self.dataFrame, text="Add choice", command=self.addChoice).grid(row=2, column=0)

        # List of choices
        self.choices = []

        # Submit all info and save them in the Plot.txt
        Button(self.win, text="Summit", command=lambda: self.submit(globList)).pack()
    
    # Create more choices
    def addChoice(self):
        self.choices.append(Choice(self.choiceFrame, len(self.choices), self.choices))

    # This is a very big function that save and destroy the current window
    def submit(self, gList):
        # Make this data into a string
        data = "%s,%s,%d" %(self.name.getData(), self.des.getData(), len(self.choices))

        for choice in self.choices:
            data = data + ",%s,%s" %(choice.entry.get(), choice.connectTo)

        # Save data to the Plot.txt
        f = open("Plot.txt", "a")
        f.write(data + "\n")
        f.close()

        # Remove everything from the working list
        self.win.destroy()
        gList.remove(self)
