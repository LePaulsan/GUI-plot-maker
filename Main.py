from tkinter import *
from Sence import Sence
from Node import Node
from Connector import Connector


# this part just init the window
root = Tk()
root.title("Maker")
cav = Canvas(root, width=1000, height=500)
cav.pack()

# This part making more events
workingSences = []
def makeWindow(globList):
    globList.append(Sence(globList))

createSence = Button(root, text="New sence", command=lambda: makeWindow(workingSences))
createSence.pack(padx=5, pady=5)

nodes = []

# make the nodes
f = open("Plot.txt", "r")

for i, line in enumerate(f):
    nodes.append(Node(cav, 100,  20, line))

f.close()


def checkOutport(event, node):
    for outport in node.outports:
        if outport[0].hover(event):
            return outport[0]

    return None
    
# this function is a fucking mess, it do a fuck ton of things TODO break this functiondown into classes or smaller funciton
def chooseAction(event):
    for node in nodes:
        if node.checkHover(event):
            if checkOutport(event, node) != None:
                checkOutport(event, node).connector.makeMovable(event, nodes)
                return

            else:
                node.makeMovable(event)
                return

def save(nodes):
    f = open("Final plot", "w")
    for node in nodes:
        f.writelines(node.save())
    
    f.close()


createSence = Button(root, text="New Save", command=lambda: save(nodes))
createSence.pack(padx=5, pady=5)

# This set the cilck all its fintion
cav.bind('<Button-1>', chooseAction)

root.mainloop()