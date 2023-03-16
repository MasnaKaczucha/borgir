from tkinter import *
from tkinter import ttk
root = Tk()
root.geometry('500x1000')


def click():
    print('name', name_info.get(), 'bun:', buns_info.get(), 'meat:', meat_info.get(), 'doneness:', doneness_info.get())

    for variable in sauce_variables:
        print(variable, sauce_variables[variable].get())

    for variable in veggie_variables:
        print(variable, veggie_variables[variable].get())

    print(veggie_variables['Cucumber'].get())


name_lbl = Label(root, text="Name of the borgir", width=20, font=("bold", 15), anchor="w")
name_lbl.place(x=30, y=30)
name_info = StringVar()

name = Entry(root, textvariable=name_info, width=20)
name.place(x=30, y=70)

meat_lbl = Label(root, text="Meat", width=20, font=("bold", 15), anchor="w")
meat_lbl.place(x=30, y=100)
meat_info = IntVar()

Radiobutton(root, text="Brisket", padx=5, variable=meat_info, value=1).place(x=30, y=130)
Radiobutton(root, text="Dry-Aged Beef", padx=5, variable=meat_info, value=2).place(x=30, y=150)
Radiobutton(root, text="Grass-Fed", padx=5, variable=meat_info, value=3).place(x=30, y=170)

doneness_lbl = Label(root, text="Doneness", width=20, font=("bold", 15), anchor="w")
doneness_lbl.place(x=30, y=200)
doneness_info = IntVar()

Radiobutton(root, text="Rare", padx=5, variable=doneness_info, value=1).place(x=30, y=230)
Radiobutton(root, text="Medium Rare", padx=5, variable=doneness_info, value=2).place(x=30, y=250)
Radiobutton(root, text="Medium", padx=5, variable=doneness_info, value=3).place(x=30, y=270)
Radiobutton(root, text="Medium Well", padx=5, variable=doneness_info, value=4).place(x=30, y=290)
Radiobutton(root, text="Well Done", padx=5, variable=doneness_info, value=5).place(x=30, y=310)

buns_lbl = Label(root, text="Type of Bun", width=20, font=("bold", 15), anchor="w")
buns_lbl.place(x=30, y=340)
buns_info = IntVar()

Radiobutton(root, text="Plain", padx=5, variable=buns_info, value=1).place(x=30, y=370)
Radiobutton(root, text="Sesame Seed", padx=5, variable=buns_info, value=2).place(x=30, y=390)
Radiobutton(root, text="Potato", padx=5, variable=buns_info, value=3).place(x=30, y=410)

frame_veggies = LabelFrame(root, text="Veggies", height=40, font=("bold", 15), padx=5, pady=20)
frame_veggies.place(x=30, y=445)

# veggies_lbl = Label(root, text="Veggies", width=20, font=("bold", 15), anchor="w")
# veggies_lbl.place(x=30, y=440)

# veggies_list = Listbox(root, selectmode="multiple", height=5)
# veggies_list.pack(side=LEFT)
# veggies_list.place(x=30, y=470)

veggies = ["Cucumber", "Iceberg Lettuce", "Tomato", "Jalapeno"]
veggie_variables = {}

for veggie in veggies:

    veggie_info = IntVar()
    checkbutton = Checkbutton(frame_veggies, text=veggie, var=veggie_info)
    checkbutton.pack(anchor="w")

    veggie_variables[veggie] = veggie_info


print(veggie_variables)

#
# for each_item in range(len(veggies)):
#     veggies_list.insert(END, veggies[each_item])


frame_sauces = LabelFrame(root, text="Sauces", height=40, font=("bold", 15), padx=5, pady=20)
frame_sauces.place(x=30, y=630)

sauces = ["BBQ", "Mayo", "Ketchup", "Hot Sauce", "Garlic Sauce"]
sauce_variables = {}

for sauce in sauces:
    sauce_info = IntVar()

    checkbutton = Checkbutton(frame_sauces, text=sauce, var=sauce_info)
    checkbutton.pack(anchor="w")

    sauce_variables[sauce] = sauce_info


Button(root, text="Make me ice cream", width=20, anchor="w", command=click).place(x=30, y=850)

root.mainloop()
