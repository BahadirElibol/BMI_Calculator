import tkinter as tk
from tkinter import font

# window
window = tk.Tk()
window.title("BMI Calculator")
window.config(padx=30, pady=30, bg="#f0f4f8")
window.minsize(width=600, height=400)

# Custom font
title_font = font.Font(family="Helvetica", size=16, weight="bold")
label_font = font.Font(family="Helvetica", size=12)
entry_font = font.Font(family="Helvetica", size=12)
button_font = font.Font(family="Helvetica", size=12, weight="bold")


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
        except ValueError:
            result_label.config(text="Enter a valid number!")


# Title label
title_label = tk.Label(window, text="BMI Calculator", bg="#f0f4f8", fg="#333", font=title_font)
title_label.pack(pady=(10, 20))

# Weight label
weight_label = tk.Label(window, text="Enter Your Weight (kg)", bg="#f0f4f8", fg="#333", font=label_font)
weight_label.pack(pady=5)

# Weight entry
weight_entry = tk.Entry(window, width=10, font=entry_font, relief="flat", bd=2)
weight_entry.pack(pady=5)

# Height label
height_label = tk.Label(window, text="Enter Your Height (cm)", bg="#f0f4f8", fg="#333", font=label_font)
height_label.pack(pady=5)

# Height entry
height_entry = tk.Entry(window, width=10, font=entry_font, relief="flat", bd=2)
height_entry.pack(pady=5)

# Calculate button
calculate_button = tk.Button(window, text="Calculate", command=calculate_bmi, bg="#4CAF50", fg="white", font=button_font, relief="flat", bd=2, padx=10, pady=5)
calculate_button.pack(pady=20)

# Result label
result_label = tk.Label(window, bg="#e3f2fd", fg="#d32f2f", font=label_font, padx=10, pady=10)
result_label.pack(pady=10)


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
