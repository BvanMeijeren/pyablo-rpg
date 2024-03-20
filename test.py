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
#  root.mainloop()

import random

# map length determines the number of moves the player have to make before entering the next map
map_length = 4

map_structure = [1] # indicates for every position in the map how many options there are/were

# based on player level, determine how many decision there will be
decisions = random.randint(1,round(map_length*0.2))+1


# set positions of the events
for i in range(map_length):
    #pos = random.randint(2,map_length) # first position cannot be split
    nr = random.randint(2,3)
    map_structure.append( nr )

map_structure.append(1)

print(map_structure)