# # binding <Return> event

# import tkinter as tk
# import tkinter.messagebox as msg

# def show(event=None): # handler
#     msg.showinfo('name', 'Your name is ' + inp.get())

# m = tk.Tk()

# prompt = tk.Label(m, text='Name: ')
# prompt.pack(fill='x', side='left')

# inp = tk.Entry(m)
# inp.bind('<Return>', show) # binding the Return event with an handler
# inp.pack(fill='x', side='left')

# ok = tk.Button(m, text='GO', command=show)
# ok.pack(fill='x', side='left')

# m.mainloop()
######################
# from tkinter import *

# def sel():
#    selection = "You selected the option " + str(var.get())
#    label.config(text = selection)

# root = Tk()
# var = StringVar()
# R1 = Radiobutton(root, text="Knight", variable=var, value='Knight',
#                   command=sel)
# R1.pack( anchor = W )

# R2 = Radiobutton(root, text="Mage", variable=var, value='Mage',
#                   command=sel)
# R2.pack( anchor = W )

# R3 = Radiobutton(root, text="Rogue", variable=var, value='Rogue',
#                   command=sel)
# R3.pack( anchor = W)

# label = Label(root)
# label.pack()
# root.mainloop()

x = {1:2}

print( list(x.keys()) )