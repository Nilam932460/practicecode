import datetime
from tkinter import *
#import tkinter.meassagebox as mb
from tkinter import ttk
from tkcalendar import DateEntry # pip install tkcalendar

# Creating the universial font variables
headlabelfont=("noto Sans CJK TC",15,'bold')
labelfont=('Garamond',14)
entryfont=('Garamond',12)

#Initailizing the GUI window
main=Tk()
main.title('school management System')
main.geometry('1000x600')#widthxheight
main.resizable(0,0)

#Creating the background and foreground color variables
lf_bg = '#FBBF77' # bg color for the left_frame
cf_bg = '#E34234' # bg color for the center_frame

# Placing the components in the main window
Label(main, text="SCHOOL MANAGEMENT SYSTEM",font=headlabelfont,bg='#FF4433').pack(side=TOP, fill=X)


left_frame = Frame(main,bg=lf_bg)
left_frame.place(x=0,y=30,relheight=1,relwidth=0.2)#x,y hor and ver offset in pixce
#relheight,relwidht is a hor and ver float offset bet 0.0 to 1.0


center_frame = Frame(main, bg=cf_bg) #
center_frame.place(relx=0.2, y=30, relheight=1, relwidth=0.2)
#relx and rely means hor and ver offset in fraction bet 0.0 to 1.0

right_frame = Frame(main, bg="Gray35")
right_frame.place(relx=0.4, y=30, relheight=1, relwidth=0.6)

# Placing components in the left frame
Label(left_frame, text="Name", font=labelfont, bg=lf_bg).place(relx=0.375, rely=0.05)
Label(left_frame, text="Contact Number", font=labelfont, bg=lf_bg).place(relx=0.175, rely=0.18)
Label(left_frame, text="Email Address", font=labelfont, bg=lf_bg).place(relx=0.2, rely=0.31)
Label(left_frame, text="Gender", font=labelfont, bg=lf_bg).place(relx=0.375, rely=0.05)
