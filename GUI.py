try:
    import tkinter as tk
except ImportError:
    import Tkinter as tk
# from http://effbot.org/tkinterbook/entry.htm
import string

def make_entry(parent, caption, width=None, **options):
    tk.Label(parent, text=caption).pack(side=tk.TOP)
    entry = tk.Entry(parent, **options)
    if width:
        entry.config(width=width)
    entry.pack(side=tk.TOP, padx=10, fill=tk.BOTH)
    return entry
def enter(event):
    check_val() 

def not_empty(string):
    return len (string) > 0

def within_range(num):
    filled = filter(not_empty,num)
    if all(((float(param) >= 0 and float(param) <= 1)) for param in filled):
        return True
    else:
        return False
    
def check_val():
    # set default values
    rows_default = 20
    cols_default = 20
    startx_default = 0.0
    starty_default = 0.0
    jump_default = 0.3
    forward_default = 0.7
    birds_default = 0.8
    rd_default = 0.7
    end_default = 1.0

    # initialize entered to defaults
    rows_entered = rows_default
    cols_entered = cols_default
    startx_entered = startx_default
    starty_entered = starty_default
    jump_entered = jump_default
    forward_entered = forward_default
    birds_entered = birds_default
    rd_entered = rd_default
    end_entered = end_default

    # set entered to value if given
    if rows.get() != "":
        rows_entered = int (rows.get())
    if columns.get() != "":
        cols_entered = int (columns.get())
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
    if int (rows_entered) > 0 and int (cols_entered) >0:
        if within_range([startx.get(), starty.get(), jump.get(),forward.get(),
                         birds.get(),returndist.get(),end.get()]):
            check_val.rows = rows_entered
            check_val.cols = cols_entered
            check_val.startx = startx_entered
            check_val.starty = starty_entered
            check_val.jump = jump_entered
            check_val.forward = forward_entered
            check_val.birds = birds_entered
            check_val.rd = rd_entered
            check_val.end = end_entered
            root.destroy()
            print('Maze Parameters Accepted')
            return
        else:
            print('Wrong!: Probabilities should be floats between 0 & 1')                 
    else:
        print('Wrong!: Rows and columns should be positive ints')
    
root = tk.Tk()
root.minsize(300,550)
root.geometry("500x550")
root.title('Enter Maze Parameters')
                 
#frame for window margin
parent = tk.Frame(root, padx=10, pady=10)
parent.pack(fill=tk.BOTH, expand=True)
                 
#entries in window
rows = make_entry(parent, "Number of Rows:", 16)
columns = make_entry(parent, "Number of Columns:", 16)
startx = make_entry(parent, "\n The following should be floats between 0.0 & 1.0\n\n Start Location Row:", 16)
starty = make_entry(parent, "Start Location Column:", 16)
jump = make_entry(parent, "Jump Probability:", 16)
forward = make_entry(parent, "Forward Probability:", 16)
birds = make_entry(parent, "Birds-Eye Probability:", 16)
returndist = make_entry(parent, "Return Distance RAtio:", 16)
end = make_entry(parent, "End Time Ratio:", 16) 
    
#button to enter
b = tk.Button(parent, borderwidth=4, text="Enter", width=10, pady=8, command=check_val)
b.pack(side=tk.BOTTOM)
rows.bind('<Return>', enter)
columns.focus_set()
parent.mainloop()
