import tkinter

def convert_weight():
    kg = float(entry_kg.get())
    pounds = kg * 2.20462
    grams = kg * 1000
    ounces = kg * 35.274
    
    label_pounds.config(text="Pounds: " + str(round(pounds, 2)) + " lbs")
    label_grams.config(text="Grams: " + str(round(grams, 2)) + " g")
    label_ounces.config(text="Ounces: " + str(round(ounces, 2)) + " oz")

win = tkinter.Tk()
win.title("Weight Converter")

label_kg = tkinter.Label(win, text="Enter weight in kilograms:")
label_kg.pack()

entry_kg = tkinter.Entry(win)


button_convert = tkinter.Button(win, text="Convert", command=convert_weight)
button_convert.pack()

label_pounds = tkinter.Label(win, text="Pounds: ")


label_grams = tkinter.Label(win, text="Grams: ")


label_ounces = tkinter.Label(win, text="Ounces: ")


entry_kg.pack()
label_pounds.pack()
label_grams.pack()
label_ounces.pack()
win.mainloop()

