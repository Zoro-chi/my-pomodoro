from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
CHECKMARK = "✔️"
TEXT_FILL = GREEN
REPS = 0
TIMER = None

# ---------------------------- TIMER RESET ------------------------------- #
# .after_cancel() stops the timer countdown
def reset_timer():
    window.after_cancel(TIMER)
    canvas.itemconfig(timer_text, text=f"00:00")
    timer_label.config(text="TIMER")
    check.config(text="")
    global REPS
    REPS = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global REPS

    REPS += 1
    work_sec = WORK_MIN * 60
    long_break = LONG_BREAK_MIN * 60
    short_break = SHORT_BREAK_MIN * 60

    if REPS % 2 == 0:
        count = short_break
        timer_label.config(text="BREAK", fg=PINK)
    elif REPS % 8 == 0:
        count = long_break
        timer_label.config(text="BREAK", fg=RED)
    else:
        count = work_sec
        timer_label.config(text="WORK", fg=GREEN)

    count_down(count)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count):
    global TIMER
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    if count_min < 10:
        count_min = f"0{count_min}"

    # .after() is like a the sleep method in Time module
    if count >= 0:
        canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
        TIMER = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        work_session = math.floor(REPS/2)
        marks = ""
        for _ in range(work_session):
            marks += CHECKMARK
        check.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("POMODORO")
window.config(padx=100, pady=50, bg=YELLOW)

#highlightthickness removes the boundary line between canvas and window
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

timer_label = Label(text="TIMER", fg=TEXT_FILL, font=(FONT_NAME, 30, "bold"), bg=YELLOW)
timer_label.grid(row=0, column=1)

start_button = Button(text="START", fg="white", bg="red", command=start_timer)
start_button.grid(row=2, column=0)

reset_button = Button(text="RESET", fg="white", bg="red", command=reset_timer)
reset_button.grid(row=2, column=2)

check = Label(fg=GREEN, bg=YELLOW)
check.grid(row=3, column=1)

window.mainloop()