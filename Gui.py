from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import customtkinter as ctk

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"assets\\frame0")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

window = ctk.CTk()
window.geometry("456x819")
logo = PhotoImage(file=relative_to_assets("logo.png"))
window.iconphoto(True, logo)
window.title("Calculator")
window.configure(bg="#181818")

canvas = Canvas(
    window,
    bg="#FFA700",
    height=819,
    width=456,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)

canvas.place(x=0, y=0)

# Entry widget to display the input and result
entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    228.1484832763672,
    159.76105499267578,
    image=entry_image_1
)
entry_1 = ctk.CTkEntry(
    master=window,
    width=420,
    height=73.5,
    border_width=0,
    corner_radius=8,
    font=("INTER", 40, 'bold'),
    fg_color="#181818",
    text_color="white",
    justify='right'
)
entry_1.place(
    x=18.0,
    y=122.0,
)

# Variables to store the input and result
input_value = ""
result = 0
is_percentage = False
percentage_operand = None

# Function to handle button clicks
def button_click(value):
    global input_value, is_percentage, percentage_operand
    if value == "00":
        input_value += "00"
    elif value == "/":
        input_value += "÷"
        is_percentage = False
        percentage_operand = None
    elif value == "*":
        input_value += "x"
        is_percentage = False
        percentage_operand = None
    elif value == "%":
        if input_value:
            is_percentage = True
            percentage_operand = float(input_value)
            input_value += "%"
        else:
            input_value += value
    else:
        input_value += str(value)
        is_percentage = False
        percentage_operand = None
    entry_1.delete(0, 'end')
    entry_1.insert(0, input_value)

# Function to clear the input
def clear_input():
    global input_value, is_percentage, percentage_operand
    input_value = ""
    is_percentage = False
    percentage_operand = None
    entry_1.delete(0, 'end')

# Function to calculate the result
def calculate_result():
    global input_value, result
    try:
        if "%" in input_value:
            percentage()
        else:
            # Replace operator symbols with their respective Python operators
            expression = input_value.replace("÷", "/").replace("x", "*")

            # Split the expression into operands and operators
            operands = []
            operators = []
            current_operand = ""
            for char in expression:
                if char.isdigit() or char == ".":
                    current_operand += char
                else:
                    operands.append(float(current_operand))
                    current_operand = ""
                    operators.append(char)
            operands.append(float(current_operand))

            # Eval the expression using Python's built-in eval function
            result = eval("".join(str(operand) for operand in operands) + "".join(operators))

            # If the result is an integer, remove the decimal part
            if result.is_integer():
                result = int(result)

            # Display the result
            entry_1.delete(0, 'end')
            entry_1.insert(0, result)
            input_value = str(result)

    except ZeroDivisionError:
        entry_1.delete(0, 'end')
        entry_1.insert(0, "Error: Division by zero")
    except SyntaxError:
        entry_1.delete(0, 'end')
        entry_1.insert(0, "Error: Invalid expression")

def percentage():
    global input_value, is_percentage, percentage_operand
    try:
        operands = input_value.split("%")
        result = float(operands[0]) * (percentage_operand / 100)
        input_value = str(result)
        entry_1.delete(0, 'end')
        entry_1.insert(0, result)
    except ZeroDivisionError:
        entry_1.delete(0, 'end')
        entry_1.insert(0, "Error: Division by zero")
    except SyntaxError:
        entry_1.delete(0, 'end')
        entry_1.insert(0, "Error: Invalid expression")

# Button images
button_images = []
for i in range(10):
    button_images.append(PhotoImage(
        file=relative_to_assets(f"button_{i}.png")))
button_images.append(PhotoImage(
    file=relative_to_assets("button_dot.png")))
button_images.append(PhotoImage(
    file=relative_to_assets("button_divide.png")))
button_images.append(PhotoImage(
    file=relative_to_assets("button_multiply.png")))
button_images.append(PhotoImage(
    file=relative_to_assets("button_subtract.png")))
button_images.append(PhotoImage(
    file=relative_to_assets("button_add.png")))
button_images.append(PhotoImage(
    file=relative_to_assets("button_percentage.png")))
button_images.append(PhotoImage(
    file=relative_to_assets("button_clear.png")))
button_images.append(PhotoImage(
    file=relative_to_assets("button_equals.png")))

# Buttons
buttons = []
button_y_positions = [259.76105499267578, 313.76105499267578, 367.76105499267578, 421.76105499267578]
button_x_positions = [
    20.0, 96.0, 172.0, 250.0, 324.0, 122.0, 172.0, 222.0, 272.0, 322.0, 17.0, 97.0, 252.0, 302.0, 16.0, 84.0, 150.0, 210.0, 264.0, 322.0
]
for i in range(20):
    buttons.append(Button(
        window,
        image=button_images[i],
        bg="#181818",
        border_width=0,
        highlightthickness=0,
        activebackground="#181818",
        activeforeground="#181818",
        command=lambda x=i: button_click(x) if i < 19 else clear_input if i == 19 else calculate_result if i == 20 else None,
        cursor="hand2"
    ))
    buttons[i].place(
        x=button_x_positions[i],
        y=button_y_positions[i % 4]
    )

window.mainloop()

def button_click(number):
    global input_value, is_percentage, percentage_operand
    button_char = ""
    if number < 10:
        button_char = str(number)
    elif number == 10:
        button_char = "."
    elif number == 11:
        button_char = "/"
    elif number == 12:
        button_char = "*"
    elif number == 13:
        button_char = "-"
    elif number == 14:
        button_char = "+"
    elif number == 15:
        button_char = "%"
    elif number == 16:
        button_char = "="
    elif number == 17:
        button_char = "c"
    elif number == 18:
        button_char = "AC"
    elif number == 19:
        button_char = "Del"

    if is_percentage:
        button_char = "%"
        is_percentage = False

    if button_char == "AC":
        entry_1.delete(0, 'end')
        input_value = ""
    elif button_char == "c":
        entry_1.delete(len(input_value) - 1, 'end')
        input_value = input_value[:-1]
    elif button_char == "Del":
        entry_1.delete(0, 'end')
        entry_1.insert(0, "Error: Division by zero")
    elif button_char == "%":
        percentage_operand = float(input_value)
        is_percentage = True
    else:
        entry_1.insert(0, button_char)
        input_value = input_value + button_char

def clear_input():
    global input_value, is_percentage, percentage_operand
    entry_1.delete(0, 'end')
    input_value = ""
    is_percentage = False
    percentage_operand = 0

def calculate_result():
    global input_value, is_percentage, percentage_operand
    try:
        result = eval(input_value)

        # If the result is an integer, remove the decimal part
        if result.is_integer():
            result = int(result)

        # Display the result
        entry_1.delete(0, 'end')
        entry_1.insert(0, result)
        input_value = str(result)

    except ZeroDivisionError:
        entry_1.delete(0, 'end')
        entry_1.insert(0, "Error: Division by zero")
    except SyntaxError:
        entry_1.delete(0, 'end')
        entry_1.insert(0, "Error: Invalid expression")

def percentage():
    global input_value, is_percentage, percentage_operand
    try:
        operands = input_value.split("%")
        result = float(operands[0]) * (percentage_operand / 100)
        input_value = str(result)
        entry_1.delete(0, 'end')
        entry_1.insert(0, result)
    except ZeroDivisionError:
        entry_1.delete(0, 'end')
        entry_1.insert(0, "Error: Division by zero")
    except SyntaxError:
        entry_1.delete(0, 'end')
        entry_1.insert(0, "Error: Invalid expression")

def relative_to_assets(path):
    return os.path.join(os.path.dirname(__file__), "assets", path)

# Button images
button_images = []
for i in range(10):
    button_images.append(PhotoImage(
        file=relative_to_assets(f"button_{i}.png")))
button_images.append(PhotoImage(
    file=relative_to_assets("button_dot.png")))
button_images.append(PhotoImage(
    file=relative_to_assets("button_divide.png")))
button_images.append(PhotoImage(
    file=relative_to_assets("button_multiply.png")))
button_images.append(PhotoImage(
    file=relative_to_assets("button_subtract.png")))
button_images.append(PhotoImage(
    file=relative_to_assets("button_add.png")))
button_images.append(PhotoImage(
    file=relative_to_assets("button_percentage.png")))
button_images.append(PhotoImage(
    file=relative_to_assets("button_clear.png")))
button_images.append(PhotoImage(
    file=relative_to_assets("button_equals.png")))

# Buttons
buttons = []
button_y_positions = [259.76105499267578, 313.76105499267578, 367.76105499267578, 421.76105499267578]
button_x_positions = [
    20.0, 96.0, 172.0, 250.0, 324.0, 122.0, 172.0, 222.0, 272.0, 322.0, 17.0, 97.0, 252.0, 302.0, 16.0, 84.0, 150.0, 210.0, 264.0, 322.0
]
for i in range(20):
    buttons.append(Button(
        window,
        image=button_images[i],
        bg="#181818",
        border_width=0,
        highlightthickness=0,
        activebackground="#181818",
        activeforeground="#181818",
        command=lambda x=i: button_click(x) if i < 19 else clear_input if i == 19 else calculate_result if i == 20 else None,
        cursor="hand2"
    ))
    buttons[i].place(
        x=button_x_positions[i],
        y=button_y_positions[i % 4]
    )

window.mainloop()
