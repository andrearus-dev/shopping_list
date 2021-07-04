from tkinter import *

window = Tk()
window.title('Shopping List')
window.geometry("600x600")
window.configure(bg="#2EAD5C")

# List box - where the food items will be displayed

shopping_list = Listbox(window, width=40, height=30)
shopping_list.pack(pady=20)

# Input field
item = StringVar()

input = Label(window, text="Add Item:")
input.pack(pady=5, padx=10,)
entry_field = Entry(window)
entry_field.pack(pady=5,)

my_list = []

for item in my_list:
    shopping_list.insert(END, item)


window.mainloop()
