import customtkinter as ctk

# Set appearance and theme
ctk.set_appearance_mode("system")       # "light" or "dark"
ctk.set_default_color_theme("blue")   # "blue", "green", "dark-blue"

app = ctk.CTk()
app.title("My Calculator")
app.geometry("300x460")
app.resizable(False, False)

expression = ""

def add_to_expression(value):
    global expression
    expression += value
    display_var.set(expression)

def clear_expression():
    global expression
    expression = ""
    display_var.set("")

def calculate():
    global expression
    try:
        expression = str(eval(expression))
        display_var.set(expression)
    except:
        display_var.set("Error")
        expression = ""

# Display
display_var = ctk.StringVar()

display = ctk.CTkEntry(app, textvariable=display_var,
                       width=260, height=60,
                       font=("Arial", 24), justify="right")
display.pack(pady=15)

# Buttons frame
frame = ctk.CTkFrame(app)
frame.pack()

buttons = [
    ('7',1,0), ('8',1,1), ('9',1,2), ('/',1,3),
    ('4',2,0), ('5',2,1), ('6',2,2), ('*',2,3),
    ('1',3,0), ('2',3,1), ('3',3,2), ('-',3,3),
    ('0',4,0), ('.',4,1), ('=',4,2), ('+',4,3),
]

# Create buttons
for (text, row, col) in buttons:
    if text == "=":
        command = calculate
        color = "green"
    else:
        command = lambda t=text: add_to_expression(t)
        color = "blue"

    btn = ctk.CTkButton(
    frame, text=text, width=60, height=50,
    corner_radius=8,
    fg_color="gray20",
    hover_color="#0066FF",
    font=("Arial", 18),
    command=command
)

    btn.grid(row=row, column=col, padx=5, pady=5)

# Clear button
clear_btn = ctk.CTkButton(
    app, text="CLEAR", width=260, height=50,
    corner_radius=8, fg_color="#a83232",
    hover_color="#802121", font=("Arial", 18),
    command=clear_expression
)
clear_btn.pack(pady=10)

label = ctk.CTkLabel(
    app,
    text="App By: Grace Chinwe Nwana",
    font=("Arial", 12),
    text_color="#3f4041"   # Dodger blue
)
label.pack(pady=20)



app.mainloop()