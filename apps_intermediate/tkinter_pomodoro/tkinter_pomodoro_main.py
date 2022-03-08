
import tkinter
import math

# ---------------------------- CONSTANTS --------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = .05  # 25
SHORT_BREAK_MIN = .1  # 5
LONG_BREAK_MIN = .2  # 20
REPS = 0
TIMER = None
CHECKMARKS = ""

# ---------------------------- TIMER RESET ------------------------------- # 


def reset_button():
    global CHECKMARKS
    window.after_cancel(TIMER)
    canvas.itemconfig(timer_text, text="00:00")
    label_timer_10.config(text="Reset")
    label_checkmarks_13.config(text="")
    global REPS
    REPS = 0

# ---------------------------- TIMER MECHANISM --------------------------- #


def start_timer():
    global REPS
    REPS += 1

    work_seconds = WORK_MIN * 60
    short_break_seconds = SHORT_BREAK_MIN * 60
    long_break_seconds = LONG_BREAK_MIN * 60

    if REPS % 8 == 0:  # If 8th rep, then want long break timer.
        label_timer_10.config(text="Long break", fg=RED)
        count_down(long_break_seconds)
    elif REPS % 2 == 0 and REPS != 7:  # If 2nd, 4th, 6th rep, then want short break timer.
        label_timer_10.config(text="Short break", fg=PINK)
        count_down(short_break_seconds)
    else:  # If 1st, 3rd, 5th, 7th rep, then want 25-minute timer.
        label_timer_10.config(text="Time to work.", fg=GREEN)
        count_down(work_seconds)


# ---------------------------- COUNTDOWN MECHANISM ----------------------- #


def count_down(count):
    count_minutes = math.floor(count / 60)
    count_seconds = (count % 60)
    if count_seconds < 10:
        count_seconds = f"0{count_seconds}"

    canvas.itemconfig(timer_text, text=f"{count_minutes}:{count_seconds}")
    if count > 0:
        global TIMER
        TIMER = window.after(1000, count_down, count - 1)
        # To be able to cancel this after command elsewhere, we have to put this inside a variable.
    else:
        global CHECKMARKS
        start_timer()
        for _ in range(math.floor(REPS/2)):
            CHECKMARKS += "✓"
        label_checkmarks_13.config(text=CHECKMARKS)

# ---------------------------- UI SETUP ---------------------------------- #


window = tkinter.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

label_timer_10 = tkinter.Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 50))
label_timer_10.grid(column=1, row=0)

canvas = tkinter.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = tkinter.PhotoImage(file="tkinter_pomodoro_tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

button_start_02 = tkinter.Button(text="Start", command=start_timer)
button_start_02.grid(column=0, row=2)

button_start_22 = tkinter.Button(text="Reset", command=reset_button)
button_start_22.grid(column=2, row=2)

label_checkmarks_13 = tkinter.Label(bg=YELLOW, fg=GREEN, font=(FONT_NAME, 30))
label_checkmarks_13.grid(column=1, row=3)


window.mainloop()
