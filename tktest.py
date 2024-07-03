import os
import subprocess
from tkinter import *
from tkinter import messagebox as mb

root = Tk()
root.geometry("300x200")

def readingfile(filetype):
    try:
        if filetype==1:
            with open("read.txt") as f:
                readme = f.read();
                #mb.showinfo(title="Title", message = str(readme))
    except FileNotFoundError:
        mb.showerror(title="error", message="No such file or directory:read.txt")

def onclick():
    #mb.showinfo('showinfo', 'message')
    #return os.system('echo FOO') >> 8
    subproc()

def subproc():
    valStr = 'fooooooo'
    #outStr = subprocess.run('echo '+valStr+gettext(), capture_output=True, text=True, shell=True).stdout
    outStr = subprocess.run('nmap '+gettext(), capture_output=True, text=True, shell=True).stdout
    mb.showinfo('info', outStr)

label = Label(root, text='foolabel')
btn = Button(root, text='ClickMe', command=onclick, height=10, width=10)
txt = Text(root)

def gettext():
    return txt.get("1.0", "end")



label.pack()
btn.pack()
txt.pack()

readingfile(1)
root.mainloop()

#def start():
#    mb.showinfo('showinfo', 'message')
#    b.configure(text='stop', command=stop)
#    l['text']= 'working...'
#    global interrupt; interrupt = False
#    root.after(1, step)

#def stop():
#    global interrupt; interrupt = True

