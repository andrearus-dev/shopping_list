import tkinter
from tkinter import *


def createList(shopping):
    for elem in shopping:
        theList.insert(END, elem[0] + "-" + str(elem[1]))


def listIndex(shopping, item):
    index = -1
    for i in range(len(shopping)):
        if shopping[i][0] == item:
            index = i
    return index


def addList(shopping, item, index):
    if index == -1:
        shopping.append([item, 1])


def removeList(shopping, index):
    del(shopping[index])


# Function that adds an item to the list
def add():
    index = listIndex(shopping, item.get())
    addList(shopping, item.get(), index)
    if index >= 0:
        theList.delete(index)
        theList.insert(index, shopping[index][0])

# Function that removes item from the list


def remove():
    index = theList.index(ACTIVE)
    print(index)
    removeList(shopping, index)
    theList.delete(index)

# Function that removes all items from the list


def removeAll():
    theList.delete(0, END)


# Empty Shopping List
shopping = []


# Creating the tkinter window
window = Tk()
window.title("Shopping List")
window.geometry("600x600")


# The layout for the list
theList = Listbox(window, selectmode=MULTIPLE, width=50, height=30, bd=20)
theList.grid(row=0, column=0, columnspan=2, sticky=E)

# Function to createList is called
createList(shopping)

item = StringVar()

# Input item
Label(window, text="Item:").grid(row=1, column=0, sticky=E)
Entry(window, textvariable=item).grid(row=1, column=1, sticky=W)


# Buttons
Button(window, text="Add Item", command=add, padx=30).grid(
    row=3, column=0, columnspan=3)

Button(window, text="Remove Item", command=remove,
       padx=30).grid(row=3, column=3)


window.mainloop()
