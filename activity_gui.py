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

def make_option(parent,OPTIONS, *values):
    variable = tk.StringVar(parent)
    variable.set("Choose Activity")
    w = apply(tk.OptionMenu, (parent,variable) + tuple(OPTIONS))
    w.pack()

def make_radio(parent, text1, text2):
    v = tk.IntVar()
    R1 = tk.Radiobutton(parent, text=text1, variable=v, value=1, command = check_radio).pack(anchor=tk.W)
    R2 = tk.Radiobutton(parent, text=text2, variable=v, value=2, command = check_radio).pack(anchor=tk.W)
    return v

def enter(event):
    check_all()

def check_radio():
    radio = act.get()
    if (radio == 1 or radio == 2):
        return True
    else:
        print('Please pick an activity!')
        return False
        
    
def check_val():
    # set default values
    rows_default = 20
    cols_default = 20

    # initialize entered to defaults
    rows_entered = rows_default
    cols_entered = cols_default

    # set "entered" to inputted value if given
    if rows.get() != "":
        rows_entered = int (rows.get())
    if columns.get() != "":
        cols_entered = int (columns.get())
        
    # print('Parameters Entered:',rows.get(),columns.get(), startx.get(), starty.get())
    if int (rows_entered) > 0 and int (cols_entered) >0:
            check_val.rows = rows_entered
            check_val.cols = cols_entered
            return True
    else:
        print('Wrong!: Rows and columns should be positive ints')
        return False

# main function to check
def check_all():
    if check_val() and check_radio():
        root.destroy()
        print('Parameters Accepted')
    
# set root and window sizes    
root = tk.Tk()
root.minsize(300,200)
#root.geometry("500x550")
root.title('BAAC Maze Generation')
                 
#frame for window margin
parent = tk.Frame(root, padx=10, pady=10)
parent.pack(fill=tk.BOTH, expand=True)
                 
#entries in window
mlabel= tk.Label(parent,text='Choose Activity:').pack()
act = make_radio(parent, "Genetic Algorithm", "Custom Maze")
rows = make_entry(parent, "\nNumber of Rows:", 16)
columns = make_entry(parent, "Number of Columns:", 16)

    
#button to enter
b = tk.Button(parent, borderwidth=5, text="Enter", width=10, pady=10, command=check_all)
b.pack(side=tk.BOTTOM)
rows.bind('<Return>', enter)
columns.focus_set()
parent.mainloop()

