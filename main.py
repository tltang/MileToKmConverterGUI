
import tkinter
window = tkinter.Tk()
window.title("Mile to Km Converter")
window.minsize(width=300, height=150)
window.config(padx=40, pady=20)

def button_clicked():
    # my_label.config(text="i am clicked")
    mile = float(my_input.get())
    mile *= 1.60934
    my_label4.config(text=round(mile,2))


my_label = tkinter.Label(text="is equal to", font=("Arial", 12, "bold"))
my_label.grid(column=1,row=2)

my_input = tkinter.Entry(width=10)
# my_input.pack()
my_input.grid(column=2,row=1)
my_input.focus()

my_label2 = tkinter.Label(text="Miles", font=("Arial", 12, "bold"))
my_label2.grid(column=3,row=1)

my_label3 = tkinter.Label(text="Km", font=("Arial", 12, "bold"))
my_label3.grid(column=3,row=2)

my_label4 = tkinter.Label(text="0", font=("Arial", 12, "bold"))
my_label4.grid(column=2,row=2)

my_button = tkinter.Button(text="Calculate", command=button_clicked)
my_button.grid(column=2,row=3)


window.mainloop()
