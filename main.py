
from tkinter import *
from tkinter import messagebox
#Define Window
root = Tk()
root.title('Metric/Imperial Converter')
root.resizable(0, 0)
field_font = ('Times New Roman', 12)
bg_color = '#BF9ACA'
button_color = '#41393E'
font_color = '#F8DDE8'
root.config(bg=bg_color)
# Define Conversion
unit_values = {
'centimeters': 0.01,
'meters': 1.0,
'kilometers': 1000.0,
'feet': 0.3048,
'yard': 0.9144,
'miles': 1609.344,
'inches': 0.0254,
'grams': 1.0,
'kilograms': 1000.0,
'pounds': 453.592,
}
# The different types of measurements being used
lengths = ['centimeters', 'meters', 'kilometers', 'feet', 'yard',
'miles', 'inches']
weights = ['kilograms', 'grams', 'pounds']
# List of units used
unit_list = ['select units', 'centimeters', 'meters', 'kilometers',
'inches', 'feet', 'yard', 'miles', 'grams', 'kilograms', 'pounds']
# Define Functions
def convert():
    inp = float(input_field.get())
    start_unit = input_option.get()
    end_unit = output_option.get()

    if start_unit in lengths and end_unit in weights:
        messagebox.showinfo("Error", "Please choose two correlating units")
    elif start_unit in weights and end_unit in lengths:
        messagebox.showinfo("Error", "Please choose two correlating units")
    else:
        output_field.delete(0, END)
        output_field.insert(0, round(inp * unit_values[start_unit]/unit_values[end_unit], 5))

input_option = StringVar()
input_option.set(unit_list[0])
output_option = StringVar()
output_option.set(unit_list[0])
# Layout for buttons
input_field = Entry(root, width=20, font=field_font, borderwidth=3)
input_field.grid(row=0, column=0, padx=10, pady=10)
input_field.insert(0, 'Enter your quantity')
input_list = OptionMenu(root, input_option, *unit_list)
input_list.grid(row=1, column=0, padx=10, pady=10)
to_label = Label(root, text='to', font=field_font, bg=bg_color)
to_label.grid(row=1, column=1, padx=10, pady=10)

output_field = Entry(root, width=20, font=field_font, borderwidth=3)
output_field.grid(row=0, column=2, padx=10, pady=10)
output_list = OptionMenu(root, output_option, *unit_list)
output_list.grid(row=1, column=2, padx=10, pady=10)
convert_btn = Button(root, text='Convert', font=field_font,
bg=button_color, fg=font_color, command=convert)
convert_btn.grid(row=2, column=0, columnspan=3, padx=10, pady=10,
ipadx=50)
root.mainloop()