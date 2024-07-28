from tkinter import *
import time
import math

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        label_timer.config(text="Break", fg=RED)
        countdown(long_break_sec)

    elif reps % 2 == 0:
        label_timer.config(text="Break", fg=PINK)
        countdown(short_break_sec)
    else:
        label_timer.config(text="Work", fg=GREEN)
        countdown(work_sec)


def countdown(count):
    global timer
    count_min = math.floor(count / 60)
    count_sec = count % 60

    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(time_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        timer = window.after(1000, countdown, count - 1)

    else:
        start_timer()
        mark = " "
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            mark += "✔️"
        label_tick.config(text=mark)


def reset():
    global reps
    global timer
    window.after_cancel(timer)
    reps = 0
    canvas.itemconfig(time_text, text="00:00")
    label_tick.config(text=" ")
    label_timer.config(text="Timer")

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=210, height=224, bg=YELLOW, highlightthickness=0)
img = PhotoImage(file="tomato.png")
canvas.create_image(105, 112, image=img)
time_text = canvas.create_text(105, 135, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

label_timer = Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 30, "bold"))
label_timer.grid(column=1, row=0)

button_start = Button(text="Start", highlightthickness=0, command=start_timer)
button_start.grid(column=0, row=2)

button_reset = Button(text="Reset", highlightthickness=0, command=reset)
button_reset.grid(column=2, row=2)

label_tick = Label(bg=YELLOW)
label_tick.grid(column=1, row=3)

window.mainloop()
