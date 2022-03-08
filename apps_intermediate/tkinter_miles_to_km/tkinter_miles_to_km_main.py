
import tkinter


def button_clicked():
    new_number = 1.609 * float(entry10.get())
    label11.config(text=f"{new_number}")  # I used an f string to convert it back to string.


window = tkinter.Tk()
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)

entry10 = tkinter.Entry(width=10)
entry10.grid(column=1, row=0)

label20 = tkinter.Label(text="Miles")
label20.grid(column=2, row=0)

label01 = tkinter.Label(text="is equal to")
label01.grid(column=0, row=1)

label11 = tkinter.Label(text="0")
label11.grid(column=1, row=1)

label21 = tkinter.Label(text="Km")
label21.grid(column=2, row=1)

button12 = tkinter.Button(text="Calculate", command=button_clicked)
button12.grid(column=1, row=2)

window.mainloop()
