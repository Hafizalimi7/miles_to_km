from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=400, height=200)


def miles_to_km():
    miles = float(miles_input.get()) * 1.609
    m_k_answer.config(text=miles)


miles_label = Label(text="Miles", font=("Ariel", 24, "bold"))
miles_label.grid(column=2, row=0)
miles_label.config(padx=5, pady=5)


miles_input = Entry(width=10)
miles_input.insert(END, string="0")
miles_input.grid(column=1, row=0)


km_label = Label(text="Km", font=("Ariel", 24, "bold"))
km_label.grid(column=2, row=1)
km_label.config(padx=20, pady=5)

equal_label = Label(text="is equal to", font=("Ariel", 24, "bold"))
equal_label.grid(column=0, row=1)
equal_label.config(padx=10, pady=10)


calculate_button = Button(text="Calculate", command=miles_to_km)
calculate_button.grid(column=1, row=2)
calculate_button.config(padx=30, pady=10)

m_k_answer = Label(text="0", font=("Ariel", 24, "bold"))
m_k_answer.grid(column=1, row=1)


window.mainloop()