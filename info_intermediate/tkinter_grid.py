
import tkinter


def button11_clicked():
    print("Button at grid 1,1 PRESSED!")
    label00.config(text=entry32.get())


def button20_clicked():
    label00.config(text="Button at grid 2,0 PRESSED!")


window = tkinter.Tk()
window.title("GRID EXAMPLE")
window.minsize(width=500, height=300)
window.config(padx=100, pady=200)  # Adds blank space around the edge of the program.

label00 = tkinter.Label(text="Label at grid 0,0.", font=("Arial", 12, "bold"))
label00.grid(column=0, row=0)
label00.config(padx=50, pady=50)

button11 = tkinter.Button(text="Button at grid 1,1", command=button11_clicked)
button11.grid(column=1, row=1)

button20 = tkinter.Button(text="Button at grid 2,0", command=button20_clicked)
button20.grid(column=2, row=0)

entry32 = tkinter.Entry(width=10)
entry32.grid(column=3, row=2)

window.mainloop()
