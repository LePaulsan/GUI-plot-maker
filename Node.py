from Port import Inport, Outport
import tkinter

class Node:
    def __init__(self, surface, x, y, data, width=150, height=20):
        # Put the data got and put it in a list
        self.datas = data.rstrip("\n").split(",")
        # self.datas[2] = int(self.datas[2]) 

        # drawing data
        self.name = self.datas[0]
        self.x = x
        self.y = y
        self.width = width
        self.height = height + 20 * int(self.datas[2])

        # Drawing on canvas
        self.surface = surface
        self.frame = self.surface.create_rectangle(self.x, self.y, self.x + self.width, self.y + self.height)
        self.text = self.surface.create_text(self.x + 7, self.y - 8, text=self.name, anchor=tkinter.W, width=120)
        self.inport = Inport(self.surface, self.x + 10, self.y + self.height/2, 5, self.name)
        
        # Making the outports
        self.outports = []
        if self.datas[2] != 0:
            for i in range(int(self.datas[2])):
                outport = Outport(self.surface, self.x + self.width - 10, self.y + 30 + i * 20, 5, self.datas[4 + 2 * i])
                des = self.surface.create_text(self.x + self.width - 10 - 10, self.y + 30 + i * 20, text=self.datas[3 + 2 * i], anchor=tkinter.E)
                new = [outport, des]
                self.outports.append(new)

    # when called check if the mouse location is on top of it
    def checkHover(self, event):
        return (self.x <= event.x <= self.x + self.width) and (self.y <= event.y <= self.y + self.height)
    
    # This function make it so that we can pick up the node
    def makeMovable(self, event):
        self.surface.bind('<B1-Motion>', self.move)
        self.surface.bind('<ButtonRelease-1>', self.putDown)

    # When called move all its content to the location of the mouse
    def move(self, event):
        self.surface.coords(self.frame, event.x, event.y, event.x + self.width, event.y + self.height)
        self.surface.coords(self.text, event.x + 7, event.y - 8)
        self.inport.move(event.x + 10, event.y + self.height/2)
        if self.outports:
            for i, outport in enumerate(self.outports):
                outport[0].move(event.x + self.width - 10, event.y + 30 + i * 20)
                self.surface.coords(outport[1],event.x + self.width - 10 - 10, event.y + 30 + i * 20)

    # Put the node down
    def putDown(self, event):
        self.surface.unbind('<B1-Motion>')
        self.surface.unbind('<ButtonRelease-1>')
        self.choosen = False
        self.update(event)

    # When called, set the location of its current things to the location of the mouse
    def update(self, event):
        # Updare the frame
        self.x = event.x
        self.y = event.y

        # As ports are created differentlly, this part is just for hupdating ports
        self.inport.update(event.x + 10, event.y + self.height/2)
        for i, outport in enumerate(self.outports):
            outport[0].update(event.x + self.width - 10, event.y + 30 + i * 20)

    def save(self):
        if self.datas[2] != '0':
            for i, outport in zip(range(int(self.datas[2])),self.outports):
                self.datas[4 + 2 * i] = outport[0].data

            # self.datas.append("\n")

        return ",".join(self.datas)