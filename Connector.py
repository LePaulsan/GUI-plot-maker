from tkinter import Canvas

class Connector:
    def __init__(self, outport, surface):
        self.surface = surface

        self.outport = outport
        self.inport = None

        self.firstX = self.outport.x
        self.firstY = self.outport.y
        self.secondX = self.outport.x
        self.secondY = self.outport.y

        self.connector = self.surface.create_line(self.firstX, self.firstY, self.secondX, self.secondY)

        self.currentHover = None

    # Make the event movable
    def makeMovable(self, event, nodes):
        self.surface.bind('<B1-Motion>', lambda event: self.move(event, nodes))
        self.surface.bind('<ButtonRelease-1>', lambda event: self.end(event, nodes))

    def findInport(self, event, nodes):
        for node in nodes:
            if node.inport.hover(event):
                return node.inport
        return None

    def move(self, event, nodes):
        self.surface.coords(self.connector, self.firstX, self.firstY, event.x, event.y)
        self.currentHover = self.findInport(event, nodes)
        if self.inport != None:
            for thing in self.inport.connectFrom[:]:
                if thing == self:
                    self.inport.connectFrom.remove(thing)

    def end(self, event, nodes):
        self.surface.unbind('<B1-Motion>')
        self.surface.unbind('<ButtonRelease>')
        if self.currentHover != None:
            self.inport = self.currentHover
            self.inport.connectFrom.append(self)

            self.outport.data = self.inport.data

            self.secondX = self.inport.x
            self.secondY = self.inport.y

            self.surface.coords(self.connector, self.firstX, self.firstY, self.secondX, self.secondY)
        else:
            self.surface.coords(self.connector, self.firstX, self.firstY, self.secondX, self.secondY)

    def updateFirst(self, x, y):
        self.firstX = x
        self.firstY = y

    def updateSecond(self, x, y):
        self.secondX = x
        self.secondY = y
