import tkinter as tk
from tkinter import filedialog
from script import scan_available_networks,connect_to_wifi,

def open_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        print("Selected file:", file_path)

def button_click():
    print("Button clicked")

# Create the main window
root = tk.Tk()
root.title("Dectionnary Attack Tool")
root.iconbitmap("icon.ico")
root.configure(bg="#34495E")
root.geometry("600x300")
root.resizable(False, False)

# Calculate center position
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width - 600) // 2
y = (screen_height - 300) // 2
root.geometry("+{}+{}".format(x, y))

# Create text area
text_area = tk.Text(root, width=70, height=10,bg="#B0C4DE", fg="#001F3F",font=("Georgia", 9))
text_area.pack(pady=10)

# Create select menu
options = ["Option 1", "Option 2", "Option 3"]
selected_option = tk.StringVar(root)
selected_option.set(options[0])
select_menu = tk.OptionMenu(root, selected_option, *options)
select_menu.config(width=88,bg="#B0C4DE", fg="#001F3F",activebackground='black', activeforeground='green', borderwidth=0) 
select_menu.pack(pady=10)

# Create open file button
open_button = tk.Button(root, text="Select Dictionnary", command=open_file,width=80)
open_button.pack()

# Create a button
action_button = tk.Button(root, text="Start", command=button_click,width=20)
action_button.pack()

# Start the GUI event loop
root.mainloop()