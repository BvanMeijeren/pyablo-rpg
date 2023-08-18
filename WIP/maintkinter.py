import customtkinter 
from graphics import *
from colorama import Fore, Back, Style

#######
# WIP *
#######
# set theme of menus
customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme('dark-blue')

root = customtkinter.CTk()

class FullScreenApp(object):
    def __init__(self, master, **kwargs):
        self.master=master
        pad=3
        self._geom='200x200+0+0'
        master.geometry("{0}x{1}+0+0".format(
            master.winfo_screenwidth()-pad, master.winfo_screenheight()-pad))
        master.bind('<Escape>',self.toggle_geom)            
    def toggle_geom(self,event):
        geom=self.master.winfo_geometry()
        print(geom,self._geom)
        self.master.geometry(self._geom)
        self._geom=geom

FullScreenApp(root)

# Navigation 
def navigate_to_main_menu():
    main_menu_frame.grid()
    character_creation_frame.grid_remove()
    game_frame.grid_remove()

def navigate_to_character_creation():
    main_menu_frame.grid_remove()
    character_creation_frame.grid()
    game_frame.grid_remove()

def navigate_to_game():
    main_menu_frame.grid_remove()
    character_creation_frame.grid_remove()
    game_frame.grid()




#################
# Main menu frame
#################
main_menu_frame = customtkinter.CTkFrame(master=root)
main_menu_frame.grid()

logo = customtkinter.CTkLabel(master=main_menu_frame, text=images['dragon_logo'])
logo.grid()

welcome_label = customtkinter.CTkLabel(master=main_menu_frame, text='Welcome to Pyablo' )
welcome_label.grid()

# start btn
btn_start = customtkinter.CTkButton(master=main_menu_frame, text='Start your journey', command=navigate_to_character_creation)
btn_start.grid()

def print_slow_ctk(widget, text, delay=50, index=1, start_index=0):
    widget.configure(text=text[start_index: index])
    index += 1
    return widget.after(delay, print_slow_ctk, widget, text, delay, index) if index <= len(text) else None

label = customtkinter.CTkLabel(master=main_menu_frame, text='Inventory')
label.grid(row=3,column=1)
print_slow_ctk(label, ' hello world')

##############################
# Frame for character creation
##############################
character_creation_frame = customtkinter.CTkFrame(master=root)
character_creation_frame.grid(row=0,column=1)

welcome_label = customtkinter.CTkLabel(master=character_creation_frame, text='Character creation' )
welcome_label.grid(row=0,column=1)
#welcome_label.grid(row = 0, column = 0, pady = 2)

from character_creation import *
mainchar = character_creation()

def changeprofession(text):
    mainchar.profession = text

customtkinter.CTkRadioButton(character_creation_frame)
var = customtkinter.StringVar()
class1 = 'Knight'
R1 = customtkinter.CTkRadioButton(character_creation_frame, text=class1, variable=var, value='Knight',
                  command=changeprofession('Knight'))
R1.grid()

R2 = customtkinter.CTkRadioButton(character_creation_frame, text="Mage", variable=var, value=2,
                  command=changeprofession('Mage'))
R2.grid()

R3 = customtkinter.CTkRadioButton(character_creation_frame, text="Rogue", variable=var, value=3,
                  command=changeprofession('Rogue'))
R3.grid()

btn_start = customtkinter.CTkButton(master=character_creation_frame, text='Create character', command=navigate_to_game)
btn_start.grid(row=0,column=1)

################
# Frame for game
################
# Translation layer from customtkinter to rest of Pyablo

def check_expression(event=None):
    #Your code that checks the expression
    varContent = inputentry.get() # get what's written in the inputentry entry widget
    outputtext.configure(text=varContent)

game_frame = customtkinter.CTkFrame(master=root)
game_frame.grid(row=0,column=1)


inventory_label = customtkinter.CTkLabel(master=game_frame, text='Inventory' )
inventory_label.grid(row=0,column=1)



inputentry=customtkinter.CTkEntry(game_frame)
inputentry.bind('<Return>', check_expression)
inputentry.grid(row=0,column=1)

outputtext=customtkinter.CTkLabel(game_frame)
outputtext.grid(row=1,column=1)


# By default, show main menu only
navigate_to_main_menu()

root.mainloop()



