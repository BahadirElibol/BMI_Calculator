import tkinter

#window
window = tkinter.Tk()
window.title("BMI Calculator")
window.config(padx=30, pady=30, bg="light blue")
window.minsize(width=400, height=300)

def calculate_bmi():
    height = height_entry.get()
    weight = weight_entry.get()
    if weight == "" or height == "":
        result_label.config(text="Enter both weight and height!")
    else:
        try:
            bmi = float(weight) / ((float(height) / 100) ** 2)
            result_string = write_result(bmi)
            result_label.config(text=result_string)
        except:
            result_label.config(text="Enter a valid number!")

#label1
weight_label = tkinter.Label(text="Enter Your Weight (kg)")
weight_label.pack()

#entry1
weight_entry = tkinter.Entry(width=10)
weight_entry.pack()

#label2
height_label = tkinter.Label(text="Enter Your Height (cm)")
height_label.pack()

#entry2
height_entry = tkinter.Entry(width=10)
height_entry.pack()

#button
calculate_button = tkinter.Button(text="Calculate", command=calculate_bmi)
calculate_button.pack()

#label3
result_label = tkinter.Label(bg="light blue", fg="red")
result_label.pack()

def write_result(bmi):
    result_string = f"Your BMI is {round(bmi, 2)}. You are "
    if bmi < 18.5:
        result_string += "UNDER WEIGHT"
    elif 18.5 <= bmi < 25:
        result_string += "NORMAL"
    elif 25 <= bmi < 30:
        result_string += "OVER WEIGHT"
    else:
        result_string += "OBESE"
    return result_string

window.mainloop()