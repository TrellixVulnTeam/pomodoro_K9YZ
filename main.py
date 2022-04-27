import math
from tkinter import *

# ************************ CONSTANTS *********************************
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 0.5
LONG_BREAK_MIN = 3
cycle = 8




# ************************ TIMER RESET ********************************
def reset_count():
    count_down(0)
# ************************TIMER MECHANISM *****************************
def start_count():
    global cycle
    cycle -= 1
    if cycle == 0:
        label.config(text="Long Break", fg=RED)
        count_down(LONG_BREAK_MIN * 60)
    elif cycle % 2 != 0:
        label.config(text="Working", fg=GREEN)
        count_down(WORK_MIN * 60)
    else:
        label.config(text="Short Break", fg=PINK)
        count_down(SHORT_BREAK_MIN  * 60)


# ******************* COUNTDOWN MECHANISM ******************************
def count_down(count):
    count_in_min = math.floor(count / 60)  # this will help get the count to display in minutes
    count_in_sec = count % 60  # this get the remainder after dividing the count which will now be remaining seconds

    # to display the count down in form of 4:00 and not just 3:9
    if count_in_sec <= 9:
        count_in_sec = f"0{count_in_sec}"

    # Update the display as the count down progresses
    canvas.itemconfig(time_text, text=f"{count_in_min}:{count_in_sec}")

    if count > 0:
        window.after(1000, count_down, count - 1)
        # in-built function for tk to do something after a particular milliseconds
        # call count_down function after 1000 milliseconds and pass count-1 into the function as argument

    else:
        start_count()
        check = "✔️"
        session_num = math.floor((8 - cycle)/2)
        if session_num % 2 == 0:
            check *= session_num
            check_mark.config(text=check)

pwd

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
time_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

label = Label(text="Timer", font=(FONT_NAME, 40, "bold"), bg=YELLOW, fg=GREEN)
label.grid(row=0, column=1)

start_btn = Button(text="Start", command=start_count)
start_btn.grid(row=2, column=0)

reset_btn = Button(text="Reset", command=reset_count)
reset_btn.grid(row=2, column=2)

check_mark = Label(fg=GREEN, bg=YELLOW)
check_mark.grid(row=2, column=1)

window.mainloop()
