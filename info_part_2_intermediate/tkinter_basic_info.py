
import tkinter

window = tkinter.Tk()
window.title("My first GUI program")
window.minsize(width=500, height=300)

# To create a label:
my_label = tkinter.Label(text="I am a label.", font=("Arial", 24, "bold"))
# We can't see the label in the program yet.
# We have to specify how that component will be laid out on the screen before the label will show up. To specify that:
my_label.pack()  # This label is automatically centered.
# my_label.pack(side="left")
my_label["text"] = "New text"  # Properties can be set when initializing(shown above), or like this line, or .config:
my_label.config(text="Newer text")

# Entry
# This is basically an input.
input1 = tkinter.Entry(width=10)
input1.pack()

# To create a button:
def button_clicked():
    # my_label.config(text="Button got clicked.")
    my_label.config(text=input1.get())  # input1.get()  This returns the input as a string.
    print("I got clicked.")
button = tkinter.Button(text="Click me", command=button_clicked)
button.pack()

window.mainloop()  # This mainloop() will keep the window on the screen,
# or else the window would just disappear after all the code is done.
# This line of code has to be at the very end of your program.
