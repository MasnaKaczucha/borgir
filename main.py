from tkinter import *
import tkinter
from PIL import ImageTk, Image

# create window
root = Tk()
root.geometry('500x1000')


# tell what condiments to add, executes after user sends form
def components():

    condiments = []

    # type of bun
    bun_in = buns_info.get()
    if bun_in == 1:
        condiments.append('plain')
    elif bun_in == 2:
        condiments.append('sesame')
    elif bun_in == 3:
        condiments.append('potato')

    # level of doneness
    doneness_in = doneness_info.get()
    if doneness_in == 1:
        condiments.append('rare')
    elif doneness_in == 2:
        condiments.append('medium-rare')
    elif doneness_in == 3:
        condiments.append('medium')
    elif doneness_in == 4:
        condiments.append('medium-well')
    elif doneness_in == 5:
        condiments.append('well-done')

    # vegetables
    for veggie_fn in veggie_variables:
        if veggie_variables[veggie_fn].get() == 1:
            condiments.append(veggie_fn)

    # sauces
    for sauce_fn in sauce_variables:
        if sauce_variables[sauce_fn].get() == 1:
            condiments.append(sauce_fn)

    condiments.append('bottom')

    print_imgs(condiments)
    print(condiments)


# make new window with the completed burger
def print_imgs(list_fn):

    # open new window
    window = tkinter.Toplevel(root)
    window.geometry('1000x1000')

    for item in list_fn:

        # send photos to the new window
        borgir = Image.open("condiments/" + item + ".jpg")
        borgir = borgir.resize((100, 100))
        image = ImageTk.PhotoImage(borgir)
        label_img = tkinter.Label(window, image=image)
        label_img.PhotoImage = image
        label_img.pack()
    window.mainloop()


# Label for the name input
name_lbl = Label(root, text="Name of the borgir", width=20, font=("bold", 15), anchor="w")
name_lbl.place(x=30, y=30)
name_info = StringVar()

# Form to enter the name of the burger
name = Entry(root, textvariable=name_info, width=20)
name.place(x=30, y=70)

# Label for the type of meat
meat_lbl = Label(root, text="Meat", width=20, font=("bold", 15), anchor="w")
meat_lbl.place(x=30, y=100)
meat_info = IntVar()

# Types of meat, user can only choose one
Radiobutton(root, text="Brisket", padx=5, variable=meat_info, value=1).place(x=30, y=130)
Radiobutton(root, text="Dry-Aged Beef", padx=5, variable=meat_info, value=2).place(x=30, y=150)
Radiobutton(root, text="Grass-Fed", padx=5, variable=meat_info, value=3).place(x=30, y=170)

# Label for the level of doneness
doneness_lbl = Label(root, text="Doneness", width=20, font=("bold", 15), anchor="w")
doneness_lbl.place(x=30, y=200)
doneness_info = IntVar()

# Levels of doneness
Radiobutton(root, text="Rare", padx=5, variable=doneness_info, value=1).place(x=30, y=230)
Radiobutton(root, text="Medium Rare", padx=5, variable=doneness_info, value=2).place(x=30, y=250)
Radiobutton(root, text="Medium", padx=5, variable=doneness_info, value=3).place(x=30, y=270)
Radiobutton(root, text="Medium Well", padx=5, variable=doneness_info, value=4).place(x=30, y=290)
Radiobutton(root, text="Well Done", padx=5, variable=doneness_info, value=5).place(x=30, y=310)

# Label for buns
buns_lbl = Label(root, text="Type of Bun", width=20, font=("bold", 15), anchor="w")
buns_lbl.place(x=30, y=340)
buns_info = IntVar()

# Types of buns, choose one
Radiobutton(root, text="Plain", padx=5, variable=buns_info, value=1).place(x=30, y=370)
Radiobutton(root, text="Sesame Seed", padx=5, variable=buns_info, value=2).place(x=30, y=390)
Radiobutton(root, text="Potato", padx=5, variable=buns_info, value=3).place(x=30, y=410)

# Frame for the checklist of vegetables
frame_veggies = LabelFrame(root, text="Veggies", height=40, font=("bold", 15), padx=5, pady=20)
frame_veggies.place(x=30, y=445)

# Define your veggies
veggies = ["Cucumber", "Lettuce", "Tomato", "Jalapeno"]
veggie_variables = {}

# Type out your veggies
for veggie in veggies:

    veggie_info = IntVar()
    checkbutton = Checkbutton(frame_veggies, text=veggie, var=veggie_info)
    checkbutton.pack(anchor="w")

    # Transfer inputs into outs
    veggie_variables[veggie] = veggie_info

# Frame for sauces
frame_sauces = LabelFrame(root, text="Sauces", height=40, font=("bold", 15), padx=5, pady=20)
frame_sauces.place(x=30, y=630)

# Your sauces
sauces = ["BBQ", "Mayo", "Ketchup"]
sauce_variables = {}

# Print out sauces
for sauce in sauces:
    sauce_info = IntVar()

    # Make check buttons
    checkbutton = Checkbutton(frame_sauces, text=sauce, var=sauce_info)
    checkbutton.pack(anchor="w")

    # In to out
    sauce_variables[sauce] = sauce_info

# Submit button
Button(root, text="Submit", width=20, anchor="w", command=components).place(x=30, y=850)

root.mainloop()
