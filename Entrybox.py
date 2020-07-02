from tkinter import Label, Entry

class EntryBox:
    def __init__(self, surface, text, row):
        self.label = Label(surface, text=text)
        self.label.grid(row=row, column=0)
        
        self.entry = Entry(surface)
        self.entry.grid(row=row, column=1)

    def getData(self):
        return self.entry.get() 

