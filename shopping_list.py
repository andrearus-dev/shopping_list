import tkinter
from tkinter import *

shopping_list = []


def createList(shopping):
    for elem in shopping_list:
        shopping_list.insert(END, elem[0] + "-" + str(elem[1]))


root = Tk()
root.title("Shopping List")


addButton = Button(window, text="Add Item", padx=50, pady=5)
addButton.pack()

root.mainloop()
