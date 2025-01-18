import tkinter as tk
from tkinter import ttk
from ipaddress import ip_network

# Function to calculate subnet details
def calculate_subnet():
    """
    Reads the user-provided IP address and CIDR, calculates subnet details, 
    and displays them in the result box.
    """
    try:
        # Get user input
        ip = ip_entry.get()
        cidr = cidr_combobox.get()
        network = f"{ip}{cidr}"
        
        # Calculate network properties
        net = ip_network(network, strict=False)
        
        # Display calculated details
        result_text.set(
            f"CIDR Notation: {net}\n"
            f"IP Range: {net[0]} - {net[-1]}\n"
            f"Total IPs: {net.num_addresses}\n"
            f"Subnet Mask: {net.netmask}\n"
            f"Hex Subnet Mask: {net.netmask.packed.hex().upper()}\n\n"
            f"Powered by © Rodwell Makoto"
        )
    except ValueError:
        # Handle invalid input
        result_text.set("Error: Invalid Input. Please enter a valid IP address and CIDR (e.g., 192.168.0.0 and /24)")

# Function to clear input fields and results
def clear_fields():
    """
    Clears the IP input field, CIDR dropdown, and results.
    """
    ip_entry.delete(0, tk.END)
    cidr_combobox.set("")
    result_text.set("")

# Main window setup
root = tk.Tk()
root.title("Subnet Calculator")
root.geometry("600x450")  # Set fixed window size
root.resizable(False, False)  # Disable resizing

# Apply style for a modern look
style = ttk.Style()
style.configure("TLabel", font=("Arial", 12))
style.configure("TButton", font=("Arial", 10))
style.configure("TEntry", font=("Arial", 12))
style.configure("TLabelFrame", font=("Arial", 12, "bold"))

# Header label
header_label = ttk.Label(root, text="Subnet Calculator", font=("Arial", 16, "bold"))
header_label.pack(pady=10)

# Input section
input_frame = ttk.Frame(root)
input_frame.pack(pady=10, padx=20, fill="x")

# Input fields for base IP
input_label = ttk.Label(input_frame, text="Enter Base IP Address (e.g., 192.168.0.0):")
input_label.pack(anchor="w")
ip_entry = ttk.Entry(input_frame, width=40)
ip_entry.pack(pady=5)

# Dropdown for CIDR prefix
cidr_label = ttk.Label(input_frame, text="Select CIDR Prefix:")
cidr_label.pack(anchor="w")
cidr_combobox = ttk.Combobox(input_frame, values=[f"/{i}" for i in range(32, 0, -1)], width=10)
cidr_combobox.pack(pady=5)

# Button section
button_frame = ttk.Frame(root)
button_frame.pack(pady=10)

# Calculate and clear buttons
calculate_button = ttk.Button(button_frame, text="Calculate", command=calculate_subnet)
calculate_button.grid(row=0, column=0, padx=5)
clear_button = ttk.Button(button_frame, text="Clear", command=clear_fields)
clear_button.grid(row=0, column=1, padx=5)

# Result display section
result_frame = ttk.LabelFrame(root, text="Results", padding=10)
result_frame.pack(pady=10, padx=20, fill="both", expand=True)

# Result text display
result_text = tk.StringVar()
result_label = ttk.Label(result_frame, textvariable=result_text, justify="left", wraplength=550, anchor="nw")
result_label.pack(fill="both", expand=True)

# Run the application
root.mainloop()
