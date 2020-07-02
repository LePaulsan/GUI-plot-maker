from tkinter import Label, Text

class TextBox:
    def __init__(self, surface, text, row):
        self.label = Label(surface, text=text)
        self.label.grid(row=row, column=0)
        
        self.text = Text(surface)
        self.text.grid(row=row, column=1)
    
    def getData(self):
        return self.text.get("1.0","end-1c")