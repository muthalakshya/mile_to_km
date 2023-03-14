from tkinter import *

def covert():
    mile = int(input.get())
    km = int(round(mile * 1.61 , 0))
    label_4.config(text=f"{km}")


window = Tk()
window.minsize(width=250,height=100)
window.title('Mile to KM converter')
window.config(padx=30,pady=30)

# button
button = Button(text="Calculate",command=covert)
button.config(padx=10,pady=10)
button.grid(row=2,column=1)


# label
label_1 = Label(text="is equal to")
label_1.grid(row=1,column=0)

# label
label_2 = Label(text="Miles")
label_2.grid(row=0,column=2)

# label
label_3 = Label(text="Km")
label_3.grid(row=1,column=2)

# label
label_4 = Label(text=0)
label_4.grid(row=1,column=1)

input = Entry(width=10)
input.grid(row=0,column=1)


window.mainloop()