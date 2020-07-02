from tkinter import Canvas
import math
from Connector import Connector

class Port():
    def __init__(self, surface, x, y, r, data):
        # The surface to draw on
        self.surface = surface

        # Data on how to draw the port
        self.x = x
        self.y = y
        self.r = r
        self.data = data

        # Drawing the port to the given location in the geven surface
        self.port = self.surface.create_oval(self.x - self.r, self.y - self.r, self.x + self.r, self.y + self.r)

    # When called, check to see if the mouse locationis on top of the port
    def hover(self, event):
        dist = math.sqrt((self.x - event.x) * (self.x - event.x) + (self.y - event.y) * (self.y - event.y))
        return dist <= self.r


class Outport(Port):
    def __init__(self, surface, x, y, r, data):
        super().__init__(surface, x, y, r, data)
        
        self.connector = Connector(self, self.surface)

    def move(self, x, y):
        self.surface.coords(self.port, x - self.r, y - self.r, x + self.r, y + self.r)
        if self.connector.inport != None:
            self.surface.coords(self.connector.connector, x, y, self.connector.secondX, self.connector.secondY)
        else:
            self.surface.coords(self.connector.connector, x, y, x, y)

    # When called, set its location to the given location
    def update(self, x, y):
        self.x = x
        self.y = y
        self.connector.updateFirst(x, y)

class Inport(Port):
    def __init__(self, surface, x, y, r, data):
        super().__init__(surface, x, y, r, data)
        
        self.connectFrom = []

    def move(self, x, y):
        self.surface.coords(self.port, x - self.r, y - self.r, x + self.r, y + self.r)
        if self.connectFrom:
            for connector in self.connectFrom:
                self.surface.coords(connector.connector, connector.firstX, connector.firstY, x ,y)


    def update(self, x, y):
        self.x = x
        self.y = y
        if self.connectFrom:
            for connector in self.connectFrom:
                connector.updateSecond(x, y)