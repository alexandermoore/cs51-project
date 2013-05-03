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

def within_range(num):
    if all((float(param) >= 0 and float(param) <= 1) for param in num):
        return True
    else:
        return False
    
def check_val():
    # set default value
    rows_entered = 20
    cols_entered = 20
    if rows.get() != "":
        rows_entered = int (rows.get())
    if columns.get() != "":
        cols_entered = int (columns.get())
        
    # print('Parameters Entered:',rows.get(),columns.get(), startx.get(), starty.get())
    if int (rows_entered) > 0 and int (cols_entered) >0:
        if within_range([startx.get(), starty.get(), jump.get(),forward.get(),
                         birds.get(),returndist.get(),end.get()]):
            check_val.rows = rows_entered
            check_val.cols = cols_entered
            check_val.startx = float (startx.get())
            check_val.starty = float (starty.get())
            check_val.jump = float (jump.get())
            check_val.forward = float (forward.get())
            check_val.birds = float (birds.get())
            check_val.rd = float (returndist.get())
            check_val.end = float (end.get())
            root.destroy()
            print('Maze Parameters Accepted')
            return
        else:
            raise SystemExit('Probabilities should be floats between 0 & 1')                 
    else:
        raise SystemExit('Rows and columns should be positive ints')
    
root = tk.Tk()
root.minsize(300,530)
root.geometry("500x530")
root.title('Enter Maze Parameters')
                 
#frame for window margin
parent = tk.Frame(root, padx=10, pady=10)
parent.pack(fill=tk.BOTH, expand=True)
                 
#entrys in window
rows = make_entry(parent, "Rows:", 16)
columns = make_entry(parent, "Columns:", 16)
startx = make_entry(parent, "\n Start Location Row:", 16)
starty = make_entry(parent, "Start Location Column:", 16)
jump = make_entry(parent, "Jump Probability:", 16)
forward = make_entry(parent, "Forward Probability:", 16)
birds = make_entry(parent, "Birds-Eye Probability:", 16)
returndist = make_entry(parent, "Return Distance:", 16)
end = make_entry(parent, "End Time:", 16) 
    
#button to enter
b = tk.Button(parent, borderwidth=4, text="Enter", width=10, pady=8, command=check_val)
b.pack(side=tk.BOTTOM)
rows.bind('<Return>', enter)
columns.focus_set()
parent.mainloop()
