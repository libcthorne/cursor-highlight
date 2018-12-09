from tkinter import Tk
root = Tk()
root.wait_visibility(root)
root.wm_attributes('-alpha',0.6)
root.configure(background='#e8ff00')
root.wm_attributes('-type', 'splash')
root.call('wm', 'attributes', '.', '-topmost', '1')

w = 30
h = 30
root.geometry('%dx%d'%(w,h))

def task():
    x = root.winfo_pointerx()-(w/2)
    y = root.winfo_pointery()+10
    root.geometry('+%d+%d'%(x,y))
    root.after(50, task)

root.after(50, task)
root.mainloop()
