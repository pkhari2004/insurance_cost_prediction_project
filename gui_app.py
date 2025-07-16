import pandas as pd
import joblib
import tkinter as tk
from tkinter import messagebox

# Load model
model = joblib.load('insurance_cost_model.pkl')

# Region map
region_map = {'southwest': 1, 'southeast': 2, 'northwest': 3, 'northeast': 4}

# Function to predict insurance cost
def predict_insurance():
    try:
        age = float(e1.get())
        if age <= 0:
            raise ValueError("Age must be positive")
        sex = 1 if sex_var.get() == "Male" else 0
        bmi = float(e3.get())
        children = int(e4.get())
        smoker = 1 if smoker_var.get() == "Yes" else 0
        region = region_map[region_var.get()]
        input_data = pd.DataFrame([[age, sex, bmi, children, smoker, region]],
                                  columns=['age', 'sex', 'bmi', 'children', 'smoker', 'region'])
        prediction = model.predict(input_data)
        result_label.config(text=f"💸 Estimated Cost: ₹{prediction[0]:,.2f}", fg="#00ffe1")

    except Exception as e:
        messagebox.showerror("🚨 Input Error", f"{e}")

# Function to reset fields
def reset_fields():
    e1.delete(0, tk.END)
    e3.delete(0, tk.END)
    e4.delete(0, tk.END)
    sex_var.set("Male")
    smoker_var.set("No")
    region_var.set("southwest")
    result_label.config(text="")

# GUI setup
master = tk.Tk()
master.title("💡 Health Insurance Cost Predictor")
master.geometry("500x550")
master.configure(bg="#121212")

tk.Label(master, text="💡 Insurance Cost Predictor", font=('Helvetica', 18, 'bold'),
         bg="#121212", fg="#39ff14", pady=15).pack(fill=tk.X)

form_frame = tk.Frame(master, bg="#121212")
form_frame.pack(padx=20, pady=10)

label_style = {'font': ('Consolas', 12), 'bg': "#121212", 'fg': '#f5f5f5'}
entry_style = {'bg': "#1f1f1f", 'fg': "#00ffe1", 'insertbackground': "#00ffe1", 'font': ('Consolas', 12)}

# Age
tk.Label(form_frame, text="Age:", **label_style).grid(row=0, column=0, sticky='e', pady=6)
e1 = tk.Entry(form_frame, **entry_style)
e1.grid(row=0, column=1, pady=6)

# Sex
tk.Label(form_frame, text="Sex:", **label_style).grid(row=1, column=0, sticky='e', pady=6)
sex_var = tk.StringVar(value="Male")
tk.OptionMenu(form_frame, sex_var, "Male", "Female").grid(row=1, column=1, sticky='w', pady=6)

# BMI
tk.Label(form_frame, text="BMI:", **label_style).grid(row=2, column=0, sticky='e', pady=6)
e3 = tk.Entry(form_frame, **entry_style)
e3.grid(row=2, column=1, pady=6)

# Children
tk.Label(form_frame, text="Children:", **label_style).grid(row=3, column=0, sticky='e', pady=6)
e4 = tk.Entry(form_frame, **entry_style)
e4.grid(row=3, column=1, pady=6)

# Smoker
tk.Label(form_frame, text="Smoker:", **label_style).grid(row=4, column=0, sticky='e', pady=6)
smoker_var = tk.StringVar(value="No")
tk.OptionMenu(form_frame, smoker_var, "Yes", "No").grid(row=4, column=1, sticky='w', pady=6)

# Region
tk.Label(form_frame, text="Region:", **label_style).grid(row=5, column=0, sticky='e', pady=6)
region_var = tk.StringVar(value="southwest")
tk.OptionMenu(form_frame, region_var, *region_map.keys()).grid(row=5, column=1, sticky='w', pady=6)

# Predict Button
tk.Button(master, text="Predict Cost", font=('Consolas', 12, 'bold'), bg="#ff007c", fg="white",
          command=predict_insurance).pack(pady=10)

# Reset Button
tk.Button(master, text="Reset", font=('Consolas', 12, 'bold'), bg="#ffaa00", fg="black",
          command=reset_fields).pack(pady=5)

# Result Label
result_label = tk.Label(master, text="", font=('Helvetica', 16, 'bold'),
                        bg="#121212", fg="#00ffe1")
result_label.pack(pady=20)

master.mainloop()
