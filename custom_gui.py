try:
    import tkinter as tk
except ImportError:
    import Tkinter as tk
# from http://effbot.org/tkinterbook/entry.htm
import string

''' make_entry
    Makes a text-fill box
    RETURNS: the entry
'''
def make_entry(parent, caption, width=None, **options):
    tk.Label(parent, text=caption).pack(side=tk.TOP)
    entry = tk.Entry(parent, **options)
    if width:
        entry.config(width=width)
    entry.pack(side=tk.TOP, padx=10, fill=tk.BOTH)
    return entry

''' make_check
    Makes a check box
    RETURNS: the value of the button.Value = 1 if selected and 0 otherwise
'''
def make_check(parent, texting):
    var = tk.IntVar()
    c = tk.Checkbutton(parent, text=texting, variable=var, command = check_box)
    c.pack()
    return var

''' enter
    Sets the return key to the check_all function
    RETURNS: no return
'''    
def enter(event):
    check_all()

''' not_empty
    Checks whether user left field blank
    RETURNS: true if not empty
'''
def not_empty(string):
    return len (string) > 0

''' within_range
    Checks whether inputted values are within range
    RETURNS: true if suitably entered
'''
def within_range(num):
    filled = filter(not_empty,num)
    if all(((float(param) >= 0 and float(param) <= 1)) for param in filled):
        return True
    else:
        return False

''' check_box
    Determines whether steps and solution should be shown
    RETURNS: true/false depending on desired display
'''
def check_box():
    steps = display_steps.get()
    if steps == 1:
        check_box.disp_steps = True
    else:
        check_box.disp_steps = False
    solution = display_sol.get()
    if solution == 1:
        check_box.disp_sol = True
    else:
        check_box.disp_sol = False

''' check_val
    Checks to make sure numerical values are entered and ints within range
    RETURNS: true if done correctly
'''     
def check_val():
    # set default values
    startx_default = 0.0
    starty_default = 0.0
    jump_default = 0.2
    forward_default = 0.7
    birds_default = 0.8
    rd_default = 0.7
    end_default = 1.0

    # initialize entered to defaults
    startx_entered = startx_default
    starty_entered = starty_default
    jump_entered = jump_default
    forward_entered = forward_default
    birds_entered = birds_default
    rd_entered = rd_default
    end_entered = end_default

    # set "entered" to inputted value if given
    if startx.get() != "":
        startx_entered = float (startx.get())
    if starty.get() != "":
        starty_entered = float (starty.get())
    if jump.get() != "":
        jump_entered = float (jump.get())
    if forward.get() != "":
        forward_entered = float (forward.get())
    if birds.get() != "":
        birds_entered = float (birds.get())
    if returndist.get() != "":
        rd_entered = float (returndist.get())
    if end.get() != "":
        end_entered = float (end.get())
        
    # print('Parameters Entered:',rows.get(),columns.get(), startx.get(), starty.get())
    if within_range([startx.get(), starty.get(), jump.get(),forward.get(),
                         birds.get(),returndist.get(),end.get()]):
        check_val.startx = startx_entered
        check_val.starty = starty_entered
        check_val.jump = jump_entered
        check_val.forward = forward_entered
        check_val.birds = birds_entered
        check_val.rd = rd_entered
        check_val.end = end_entered
        return True               
    else:
        print('Wrong!: Probabilities should be floats between 0 & 1')
        return False

''' check_all
    Makes sure radio values and text-fill values appropriate when user submits
    RETURNS: no return
'''
def check_all():
 if check_val():
     root.destroy()
     print('Maze Parameters Accepted')
     check_box()

# set root and window sizes    
root = tk.Tk()
root.minsize(300,540)
#root.geometry("500x570")
root.title('Enter Maze Parameters')
                 
#frame for window margin
parent = tk.Frame(root, padx=10, pady=10)
parent.pack(fill=tk.BOTH, expand=True)
                 
#entries in window
startx = make_entry(parent, "\n The following should be floats between 0.0 & 1.0\n\n Start Location Row:", 16)
starty = make_entry(parent, "Start Location Column:", 16)
jump = make_entry(parent, "Jump Probability:", 16)
forward = make_entry(parent, "Forward Probability:", 16)
birds = make_entry(parent, "Birds-Eye Probability:", 16)
returndist = make_entry(parent, "Return Distance Ratio:", 16)
end = make_entry(parent, "End Time Ratio:", 16)
mlabel= tk.Label(parent,text='\n').pack()
display_steps = make_check(parent,"Display Maze Creation Steps")
display_sol = make_check(parent, "Display Maze Solution")
    
#button to enter
b = tk.Button(parent, borderwidth=5, text="Enter", width=10, pady=10, command=check_all)
b.pack(side=tk.BOTTOM)
startx.bind('<Return>', enter)
starty.focus_set()
parent.mainloop()
