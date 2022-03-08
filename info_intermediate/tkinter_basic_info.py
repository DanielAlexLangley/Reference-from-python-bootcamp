
# TKINTER
# EVENT DRIVEN

import tkinter

def button_clicked():
    # my_label.config(text="Button got clicked.")
    print("I got clicked.")
    my_label.config(text=input1.get())  # input1.get()  This returns the input as a string.

window = tkinter.Tk()
window.title("My first GUI program")
window.minsize(width=500, height=300)

# To create a label:
my_label = tkinter.Label(text="I am a label.", font=("Arial", 24, "bold"))
# We can't see the label in the program yet.
# We have to specify how that component will be laid out on the screen before the label will show up. To specify that:
my_label["text"] = "New text"  # Properties can be set when initializing(shown above), or like this line, or .config:
my_label.config(text="Newer text")
my_label.pack()  # This label is automatically centered.
# my_label.pack(side="left")
# Put .pack() as the last line of each widget.

# Button
# See button function above.
button = tkinter.Button(text="Click me", command=button_clicked)
button.pack()

# Entry
# This is basically an input.
input1 = tkinter.Entry(width=10)
input1.pack()

# tkinter has different layout managers that define how to position each widget in your gui program.
# Three to know about:
# Pack, place, grid
# If a label is created, but you don't specify pack, place, or grid, then label won't know up.
my_label_cant_see = tkinter.Label(text="You can't see this label.")
# Pack puts them next to each other, default starting at top, next widgets below in order.
# Problem with pack is that it's difficult to specify a precise position.
# Place is for precise positioning.
my_label_place = tkinter.Label(text="Test place label.", font=("Arial", 12, "bold"))
my_label_place.place(x=0, y=0)
# The problem with place is that it's so specific, we have to determine the precise coordinate to put it there.
# The grid lets you make your entire program be a grid, and you can divide it into as many rows/columns as you want.
my_label_grid = tkinter.Label(text="Test grid label.", font=("Arial", 12, "bold"))
my_label_grid.grid(column=0, row=0)
# The best way to organize widgets in your code then is to
# put them in the order from top to bottom as they will be in your grid.
# You can't mix grid and pack in same program.

window.mainloop()  # This mainloop() will keep the window on the screen,
# or else the window would just disappear after all the code is done.
# This line of code has to be at the very end of your program.
# This is called EVENT DRIVEN and is used in GUI programming.
