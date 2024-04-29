from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"assets\\frame0")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

window = Tk()

window.geometry("456x819")
logo = PhotoImage(file=relative_to_assets("logo.png"))
window.iconphoto(True, logo)
window.title("Calculator")
window.configure(bg="#181818")

canvas = Canvas(
    window,
    bg="#181818",
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
entry_1 = Entry(
    bd=0,
    bg="#181818",
    fg="#000716",
    font=("INTER", 40, 'bold'),
    foreground="White",
    highlightthickness=0,
    justify='right'
)
entry_1.place(
    x=18.0,
    y=122.0,
    width=420.2969665527344,
    height=73.52210998535156,
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

            # Evaluate the expression using the operands and operators
            result = operands.pop(0)
            for i, op in enumerate(operators):
                operand = operands.pop(0)
                if op == "+":
                    result += operand
                elif op == "-":
                    result -= operand
                elif op == "*":
                    result *= operand
                elif op == "/":
                    result /= operand

            # Display result as integer if it's an integer, otherwise as float
            if isinstance(result, int):
                input_value = str(result)
            else:
                if result.is_integer():
                    input_value = str(int(result))
                else:
                    input_value = str(result)

        entry_1.delete(0, 'end')
        entry_1.insert(0, input_value)
    except Exception as e:
        input_value = "Error"
        entry_1.delete(0, 'end')
        entry_1.insert(0, input_value)
        print(f"Error: {e}")


# Function to handle backspace
def backspace():
    global input_value
    input_value = input_value[:-1]
    entry_1.delete(0, 'end')
    entry_1.insert(0, input_value)

# Function to handle percentage
def percentage():
    global input_value, result
    try:
        if "%" in input_value:
            # Replace operator symbols with their respective Python operators
            expression = input_value.replace("÷", "/").replace("x", "*")

            # Split the expression into operands and operators
            operands = []
            operators = []
            current_operand = ""
            for char in expression:
                if char.isdigit() or char == ".":
                    current_operand += char
                elif char == "%":
                    operands.append(float(current_operand))
                    current_operand = ""
                    operators.append("%")
                else:
                    operands.append(float(current_operand))
                    current_operand = ""
                    operators.append(char)
            operands.append(float(current_operand))

            # Evaluate the expression using the operands and operators
            result = operands.pop(0)
            for i, op in enumerate(operators):
                operand = operands.pop(0)
                if op == "+":
                    result += operand
                elif op == "-":
                    result -= operand
                elif op == "*":
                    result *= operand
                elif op == "/":
                    result /= operand
                elif op == "%":
                    result = (result * operand) / 100

            # Display result as integer if it's an integer, otherwise as float
            if isinstance(result, int):
                input_value = str(result)
            else:
                if result.is_integer():
                    input_value = str(int(result))
                else:
                    input_value = str(result)

        else:
            input_value += "%"
            entry_1.delete(0, 'end')
            entry_1.insert(0, input_value)
            return

        entry_1.delete(0, 'end')
        entry_1.insert(0, input_value)

    except Exception as e:
        input_value = "Error"
        entry_1.delete(0, 'end')
        entry_1.insert(0, input_value)
        print(f"Error: {e}")

# Button images and commands
button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=clear_input,
    relief="flat"
)
button_1.place(
    x=15.0,
    y=269.0,
    width=87.0,
    height=87.0
)


button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: button_click(7),
    relief="flat"
)
button_2.place(
    x=15.0,
    y=377.0,
    width=87.0,
    height=87.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: button_click(4),
    relief="flat"
)
button_3.place(
    x=15.0,
    y=485.0,
    width=87.0,
    height=87.0
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: button_click(1),
    relief="flat"
)
button_4.place(
    x=15.0,
    y=593.0,
    width=87.0,
    height=87.0
)

button_image_5 = PhotoImage(
    file=relative_to_assets("button_5.png"))
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: button_click("00"),
    relief="flat"
)
button_5.place(
    x=15.0,
    y=701.0,
    width=87.0,
    height=87.0
)
button_image_6 = PhotoImage(
    file=relative_to_assets("button_6.png"))
button_6 = Button(
    image=button_image_6,
    borderwidth=0,
    highlightthickness=0,
    command=percentage,
    relief="flat"
)
button_6.place(
    x=128.0,
    y=269.0,
    width=87.0,
    height=87.0
)

button_image_7 = PhotoImage(
    file=relative_to_assets("button_7.png"))
button_7 = Button(
    image=button_image_7,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: button_click(8),
    relief="flat"
)
button_7.place(
    x=128.0,
    y=377.0,
    width=87.0,
    height=87.0
)

button_image_8 = PhotoImage(
    file=relative_to_assets("button_8.png"))
button_8 = Button(
    image=button_image_8,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: button_click(5),
    relief="flat"
)
button_8.place(
    x=128.0,
    y=485.0,
    width=87.0,
    height=87.0
)

button_image_9 = PhotoImage(
    file=relative_to_assets("button_9.png"))
button_9 = Button(
    image=button_image_9,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: button_click(2),
    relief="flat"
)
button_9.place(
    x=128.0,
    y=593.0,
    width=87.0,
    height=87.0
)

button_image_10 = PhotoImage(
    file=relative_to_assets("button_10.png"))
button_10 = Button(
    image=button_image_10,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: button_click(0),
    relief="flat"
)
button_10.place(
    x=128.0,
    y=701.0,
    width=87.0,
    height=87.0
)

button_image_11 = PhotoImage(
    file=relative_to_assets("button_11.png"))
button_11 = Button(
    image=button_image_11,
    borderwidth=0,
    highlightthickness=0,
    command=backspace,
    relief="flat"
)
button_11.place(
    x=241.0,
    y=269.0,
    width=87.0,
    height=87.0
)

button_image_12 = PhotoImage(
    file=relative_to_assets("button_12.png"))
button_12 = Button(
    image=button_image_12,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: button_click(9),
    relief="flat"
)
button_12.place(
    x=241.0,
    y=377.0,
    width=87.0,
    height=87.0
)

button_image_13 = PhotoImage(
    file=relative_to_assets("button_13.png"))
button_13 = Button(
    image=button_image_13,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: button_click(6),
    relief="flat"
)
button_13.place(
    x=241.0,
    y=485.0,
    width=87.0,
    height=87.0
)

button_image_14 = PhotoImage(
    file=relative_to_assets("button_14.png"))
button_14 = Button(
    image=button_image_14,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: button_click(3),
    relief="flat"
)
button_14.place(
    x=241.0,
    y=593.0,
    width=87.0,
    height=87.0
)

button_image_15 = PhotoImage(
    file=relative_to_assets("button_15.png"))
button_15 = Button(
    image=button_image_15,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: button_click("."),
    relief="flat"
)
button_15.place(
    x=241.0,
    y=701.0,
    width=87.0,
    height=87.0
)

button_image_16 = PhotoImage(
    file=relative_to_assets("button_16.png"))
button_16 = Button(
    image=button_image_16,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: button_click("/"),
    relief="flat"
)
button_16.place(
    x=354.0,
    y=269.0,
    width=87.0,
    height=87.0
)

button_image_17 = PhotoImage(
    file=relative_to_assets("button_17.png"))
button_17 = Button(
    image=button_image_17,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: button_click("*"),
    relief="flat"
)
button_17.place(
    x=354.0,
    y=377.0,
    width=87.0,
    height=87.0
)

button_image_18 = PhotoImage(
    file=relative_to_assets("button_18.png"))
button_18 = Button(
    image=button_image_18,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: button_click("-"),
    relief="flat"
)
button_18.place(
    x=354.0,
    y=485.0,
    width=87.0,
    height=87.0
)

button_image_19 = PhotoImage(
    file=relative_to_assets("button_19.png"))
button_19 = Button(
    image=button_image_19,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: button_click("+"),
    relief="flat"
)
button_19.place(
    x=354.0,
    y=593.0,
    width=87.0,
    height=87.0
)

button_image_20 = PhotoImage(
    file=relative_to_assets("button_20.png"))
button_20 = Button(
    image=button_image_20,
    borderwidth=0,
    highlightthickness=0,
    command=calculate_result,
    relief="flat"
)
button_20.place(
    x=354.0,
    y=701.0,
    width=87.0,
    height=87.0
)

window.resizable(False, False)
window.mainloop()