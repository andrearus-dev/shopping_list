from tkinter import *
from tkinter.font import Font


window = Tk()
window.title('Shopping List')
window.geometry("400x800")
window.configure(bg="#2EAD5C")

bigFont = Font(size=20, weight="bold")


heading1 = Label(window, text=" Food Glorious Food \n Shopping List",
                 bg="#2EAD5C", fg="#fff", font=bigFont).pack(pady=10)


# Adding input text to the list
def add_command():
    text = entry_field.get()
    for item in my_list:
        list_layout.insert(END, text)


# Deleting one item at a time
def delete_command():
    for item in my_list:
        list_layout.delete(ACTIVE)


# Deleting all items with one click of a button
def delete_all_command():
    list_layout.delete(0, END)


# Variable holding empty list
my_list = [""]


# Frame and scroll bar so the user can view the whole list
my_frame = Frame(window, bg="#00570D")
scrollBar = Scrollbar(my_frame, orient=VERTICAL)


# List box - where the items will be displayed
list_layout = Listbox(my_frame, width=40, height=20,
                      yscrollcommand=scrollBar.set)
list_layout.pack(pady=20)


# configure scrollbar
scrollBar.config(command=list_layout.yview)
scrollBar.pack(side=RIGHT, fill=Y)
my_frame.pack(pady=20)

heading2 = Label(window, text="Add items to your list \n Happy Shopping!",
                 bg="#2EAD5C", fg="#fff", font=1).pack(pady=5)


# Entry Field

entry_field = Entry(window)
entry_field.pack(pady=5)


# Buttons - when clicked the function is called
Button(window, text="Add Item", command=add_command).pack(pady=5)

Button(window, text="Delete Item", command=delete_command).pack(pady=5)

Button(window, text="Delete ALL Food Items",
       command=delete_all_command).pack(pady=10)


window.mainloop()
