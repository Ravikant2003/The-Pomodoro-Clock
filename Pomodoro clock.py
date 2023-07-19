#-----------------Defining the times------------------
work_min=25
short_break_min=5
long_break_min=20
############################################
"""
How the clock algorithm works
1) Basically, a pomodoro consist of a 25 min session, after which there is a short break of 5 min
2) After the 8th session, that is after 200 min, there is a long break of 20 minutes
3) The main purpose of this clock is to increase your productivity.
"""
############################################
repetition=0 # Tells about the repetions of cycles in Pomodoro cycle
work_sec=25*60
short_break_sec=5*60
long_break_sec=20*60
timer=None # It is used to create tick marks and helps to count time in for of 9,8,7,6,..... countdown style

import math # For calculation purpuse
import tkinter
windows=tkinter.Tk()
windows.title("Pomodoro Clock")
windows.minsize(height=600,width=600)
windows.config(padx=100,pady=100,bg="Yellow")

canvas=tkinter.Canvas(width=200,height=224,bg="yellow",highlightthickness=0) #Canvas helps to create Background
tomato=tkinter.PhotoImage(file="tomato.png") #Helped to create the tomato png
canvas.create_image(100,112,image=tomato)
timertext=canvas.create_text(100,130,text="00:00",fill="White",font=("Franklin Gothic",35,"bold","italic"))
#Timertext shows the 00:00 format time
#-------------------------------------------------------All Functions ----------------------------
def reset_timer(): #Function to reset the timer
    windows.after_cancel(timer)
    canvas.itemconfig(timertext,text="00:00")
    label1.config(text="Timer")
    label2.config(text="")
    global reps
    reps=0
def count_down(count):  # Function to Count time
    count_min=math.floor(count/60)
    count_sec=count%60
    if count_sec<10:
        count_sec=f"0{count_sec}"
    canvas.itemconfig(timertext,text=f"{count_min}:{count_sec}")
    if count>0:
        global timer
        timer=windows.after(1000,count_down,count-1) # used for countdwon in form of 5,4,3,2,1,0 type
    else:
        start_timer()
        if reps%2==0:
            label2.config(text="✔"*int(reps/2))

def start_timer(): # Function to start the time
    global reps
    reps+=1
    if reps%8==0:
        count_down(long_break_sec)
        label1.config(text="Long break",fg="Blue")
    elif reps%2==0:
        count_down(short_break_sec)
        label1.config(text="Short break",fg="Green")
    else:
        count_down(work_sec)
        label1.config(text="Work",fg="Red")

# All Labels used in Pomodoro program
''' 
label1- Shows the "Timer heading"
button1- Creates a button named Start
button2- Creates a button named Stop
label2- Used to make the ✔ sign

'''

label1=tkinter.Label(text="Timer",font=("Castellar",35,"bold","italic"),bg="yellow")
button1=tkinter.Button(text="Start",font=("Times New Roman",12,"bold","italic"),bg="yellow",command=start_timer)
button2=tkinter.Button(text="Stop",font=("Times New Roman",12,"bold","italic"),bg="yellow",command=reset_timer)
label2=tkinter.Label(text="",bg="yellow",highlightthickness=0)

# Used to create the GUI by placement of all the labels
label1.grid(column=5,row=1)
label2.grid(column=5,row=5)
button1.grid(column=1,row=5)
button2.grid(column=9,row=5)
canvas.grid(column=5,row=2)

# Runs the overall Program
windows.mainloop()