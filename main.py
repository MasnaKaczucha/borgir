from tkinter import *
from tkinter import ttk
root = Tk()
root.geometry('500x1000')

name_lbl = Label(root, text="Name of the borgir", width=20, font=("bold", 15), anchor="w")
name_lbl.place(x=30, y=30)

name = Entry(root, width=20)
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

veggies_lbl = Label(root, text="Veggies", width=20, font=("bold", 15), anchor="w")
veggies_lbl.place(x=30, y=440)

veggies_list = Listbox(root, selectmode="multiple", height=5)
veggies_list.pack(side=LEFT)
veggies_list.place(x=30, y=470)
veggies = ["Cucumber", "Iceberg Lettuce", "Tomato", "Jalapeno"]

for each_item in range(len(veggies)):
    veggies_list.insert(END, veggies[each_item])

sauces_lbl = Label(root, text="Sauces", width=20, font=("bold", 15), anchor="w")
sauces_lbl.place(x=30, y=550)

sauces_list = Listbox(root, selectmode="multiple", height=5)
sauces_list.pack(side=LEFT)
sauces_list.place(x=30, y=580)
sauces = ["BBQ", "Mayo", "Ketchup", "Hot Sauce", "Garlic Sauce"]

for each_item in range(len(sauces)):
    sauces_list.insert(END, sauces[each_item])

Button(root, text="Make me ice cream", width=20, anchor="w").place(x=30, y=700)

root.mainloop()