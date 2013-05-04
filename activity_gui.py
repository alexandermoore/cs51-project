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
    # master = tk.Tk()
    variable = tk.StringVar(parent)
    variable.set("Choose Activity")
    w = apply(tk.OptionMenu, (parent,variable) + tuple(OPTIONS))
    w.pack()
    
def enter(event):
    check_val() 

    
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
            root.destroy()
            print('Maze Parameters Accepted')
            return
    else:
        print('Wrong!: Rows and columns should be positive ints')

# set root and window sizes    
root = tk.Tk()
root.minsize(200,200)
#root.geometry("500x550")
root.title('BAAC Maze Generation')
                 
#frame for window margin
parent = tk.Frame(root, padx=10, pady=10)
parent.pack(fill=tk.BOTH, expand=True)
                 
#entries in window
opt = make_option(parent,["Genetic Algorithm with Pythagorean Solver",
           "Genetic Algorithm with Smart Solver",
           "Genetic Algoithm with Inverse Solver",
           "Create Custom Maze"],16)
rows = make_entry(parent, "\nNumber of Rows:", 16)
columns = make_entry(parent, "Number of Columns:", 16)

    
#button to enter
b = tk.Button(parent, borderwidth=5, text="Enter", width=10, pady=10, command=check_val)
b.pack(side=tk.BOTTOM)
rows.bind('<Return>', enter)
columns.focus_set()
parent.mainloop()

