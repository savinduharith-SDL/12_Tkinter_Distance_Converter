from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.config(padx=40,pady=20)

begin_text = Label(text="is equal to")
begin_text.grid(column=0, row=1)
begin_text.config(pady=10, padx=10)

value_text = Label()
value_text.grid(column=1, row=1)
value_text.config(padx=10, pady=10)

miles_text = Label(text="Miles")
miles_text.grid(column=2, row=0)
miles_text.config(pady=10, padx=10)

km_text = Label(text="Km")
km_text.grid(column=2, row=1)
km_text.config(padx=10, pady=10)


def calculate():
    value = int(input.get())
    result = value*1.60934
    value_text.config(text=result)


calculate_button = Button(text="Calculate",command=calculate)
calculate_button.grid(column=1, row=2)
calculate_button.config(pady=5, padx=5)

input = Entry(width=20)
input.grid(column=1, row=0)

window.mainloop()

