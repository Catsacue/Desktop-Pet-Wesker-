import pyautogui
import random
import tkinter as tk
import time

global x
global y
x = 960
y = 982
cycle = 0
check = 0
press = False
idle_num =[1,2,3,4,15]
walk_left = [6,7,8,9]
walk_right = [10,11,12,13]
hips_num = [16,17]
sleep_num = [19,20,21]
smack_num = [22]

event_number = random.randrange(1,3,1)

# you're going to have to change the path here if this code is being performed
# on a new device
impath = 'C:\\Users\\Dru\\Documents\\REAL python wesker\\'


#transfer random no. to event
def event(cycle,check,event_number,x):
    if event_number in idle_num:
        check = 0
        print('idle')
        window.after(400,update,cycle,check,event_number,x) #no. 1,2,3,4 = idle
        
    elif event_number == 5:
        check = 1
        print('from idle to sleep')
        window.after(200,update,cycle,check,event_number,x) #no. 5 = idle to sleep
        
    elif event_number in hips_num:
        check  = 6
        print('hips')
        window.after(1000,update,cycle,check,event_number,x)#no. 15,16,17 = hips
        
    elif event_number == 14:
        check = 7
        print('from idle to hips')
        window.after(200,update,cycle,check,event_number,x) #no. 14 = idle to hips
        
    elif event_number == 22:
        check = 8
        print('SMACK!')
        window.after(200,update,cycle,check,event_number,x) #no. 22 = SMACK!!!
        
    elif event_number in walk_left:
        check = 4
        print('walking towards left')
        window.after(100,update,cycle,check,event_number,x)#no. 6,7,8,9 = walk towards left
        
    elif event_number in walk_right:
        check = 5
        print('walking towards right')
        window.after(100,update,cycle,check,event_number,x)#no 10,11,12,13 = walk towards right
        
    elif event_number in sleep_num:
        check  = 2
        print('sleep')
        window.after(1000,update,cycle,check,event_number,x)#no. 19,20,21 = sleep
        
    elif event_number == 18:
        check = 3
        print('from sleep to idle')
        window.after(200,update,cycle,check,event_number,x)#no. 18 = sleep to idle
        
        
#making gif work 
def gif_work(cycle,frames,event_number,first_num,last_num):
    if cycle < len(frames) -1:
        cycle+=1
    else:
        cycle = 0
        event_number = random.randrange(first_num,last_num+1,1)
    return cycle,event_number
    

def update(cycle,check,event_number,x):
 #idle
    if check ==0:
        frame = idle[cycle]
        cycle ,event_number = gif_work(cycle,idle,event_number,1,14)
  
 #idle to sleep
    elif check ==1:
        frame = idle_to_sleep[cycle]
        cycle ,event_number = gif_work(cycle,idle_to_sleep,event_number,19,19)
        
#idle to hips
    elif check ==7:
        frame = idle_to_hips[cycle]
        cycle ,event_number = gif_work(cycle,idle_to_hips,event_number,16,16)
        
#sleep
    elif check == 2:
        frame = sleep[cycle]
        cycle ,event_number = gif_work(cycle,sleep,event_number,18,21)
        
#hips
    elif check == 6:
        frame = hips[cycle]
        cycle ,event_number = gif_work(cycle,hips,event_number,15,17)
        
#smack!
    elif check == 8:
        frame = smack[cycle]
        cycle ,event_number = gif_work(cycle,smack,event_number,1,4)
        
#sleep to idle
    elif check ==3:
        frame = sleep_to_idle[cycle]
        cycle ,event_number = gif_work(cycle,sleep_to_idle,event_number,1,1)
        
#walk toward left
    elif check == 4:
        frame = walk_positive[cycle]
        cycle , event_number = gif_work(cycle,walk_positive,event_number,1,13)
        x -= 5
        
#walk towards right
    elif check == 5:
        frame = walk_negative[cycle]
        cycle , event_number = gif_work(cycle,walk_negative,event_number,1,13)
        x -= -5
        
    window.geometry('40x40+'+str(x)+'+'+str(y))
    label.configure(image=frame)
    window.after(10,event,cycle,check,event_number,x)

window = tk.Tk()
window.title("Wesker")
window.iconbitmap('C:\\Users\\Dru\\Documents\\REAL python wesker\\icon.ico')

#calls wesker action gif
idle = [tk.PhotoImage(file=impath+'wesker_stand_r.gif',format = 'gif -index %i' %(i)) for i in range(3)]#idle gif

idle_to_sleep = [tk.PhotoImage(file=impath+'wesker_tosleep_r.gif',format = 'gif -index %i' %(i)) for i in range(13)]#idle to sleep gif

sleep = [tk.PhotoImage(file=impath+'wesker_sleep_r.gif',format = 'gif -index %i' %(i)) for i in range(3)]#sleep gif

sleep_to_idle = [tk.PhotoImage(file=impath+'wesker_fromsleep_r.gif',format = 'gif -index %i' %(i)) for i in range(13)]#sleep to idle gif

walk_positive = [tk.PhotoImage(file=impath+'wesker_walk_l.gif',format = 'gif -index %i' %(i)) for i in range(4)]#walk to left gif

walk_negative = [tk.PhotoImage(file=impath+'wesker_walk_r.gif',format = 'gif -index %i' %(i)) for i in range(4)]#walk to right gif

idle_to_hips = [tk.PhotoImage(file=impath+'wesker_tohips_l.gif',format = 'gif -index %i' %(i)) for i in range(11)]# hands on hips gif

hips = [tk.PhotoImage(file=impath+'wesker_hips_l.gif',format = 'gif -index %i' %(i)) for i in range(3)]# hips gif

smack = [tk.PhotoImage(file=impath+'wesker_smack.gif',format = 'gif -index %i' %(i)) for i in range(2)]# smack gif


adjust = tk.Toplevel(window)
adjust.transient(window)
adjust.title( "Y Adjust" )
adjust.attributes('-topmost', True)
window.update_idletasks()


entry = tk.Entry(adjust)
entry.pack()

global new_y

def get_text():
    has_letter = False
    text = entry.get()
    for char in text:
        if char.isalpha():
            has_letter = True
            break
    if has_letter == True:
        print("Invalid.")
    elif has_letter == False:
        if len(text) > 4:
            new_y = 1040
        elif int(text) > 1080:
            new_y = 1040
        else:
            new_y = int(text)
        print("Input: " + str(new_y))
        
        global y
        y = new_y

# Create a button to trigger the function
button = tk.Button(adjust, text="Move Wesker", command=get_text)
button.pack()

def closer( event ):
    window.destroy()
    
def closer2( event ):
    adjust.destroy()
    

adjust_window = None

def move(event):
    global adjust_window
    global entry
    if adjust_window is None or not adjust_window.winfo_exists():  # If the window is open
        # Create the adjust window
        adjust_window = tk.Toplevel(window)
        adjust_window.transient(window)
        adjust_window.title("Y Adjust")
        adjust_window.attributes('-topmost', True)
        
        entry = tk.Entry(adjust_window)
        entry.pack()
        
        button = tk.Button(adjust_window, text="Move Wesker", command=get_text)
        button.pack()
    else:
        # If the adjust window already exists, bring it to the front
        adjust_window.lift()  # Brings the window to the front
        adjust_window.focus_force()  # Forces focus on the window

# after clicking/selecting wesker and pressing button, close/open windows
window.bind( "<Escape>", closer )
window.bind("WM_DELETE_WINDOW", closer)
adjust.bind("WM_DELETE_WINDOW", closer2)
window.bind("f",move)

#window configuration
window.config(highlightbackground='green')
label = tk.Label(window,bd=0,bg='green')

window.overrideredirect(True)
# make window appear over all other windows
window.attributes('-topmost', True)
window.wm_attributes('-transparentcolor','green')
label.pack()

#loop 
window.after(10,update,cycle,check,event_number,x)
window.mainloop()