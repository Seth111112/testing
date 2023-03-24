import os
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

# Create the main window
root = tk.Tk()

# get screen size
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# set window size to half of screen width and full screen height
width = int(screen_width / 2)
height = screen_height
root.geometry(f"{width}x{height}+0+0")

# dock window to left side of screen
root.update()
x = 0
y = 0
root.geometry(f"{width}x{height}+{x}+{y}")

# check window position and size
root.update()
root_x = root.winfo_x()
root_y = root.winfo_y()
root_width = root.winfo_width()
root_height = root.winfo_height()

print(f"Screen size: {screen_width}x{screen_height}")
print(f"Window size: {root_width}x{root_height}")
print(f"Window position: ({root_x}, {root_y})")

# Load the image
img = Image.open("Buddy.png")
photo = ImageTk.PhotoImage(img)


# Create a label with the image as the background
bg_label = tk.Label(root, image=photo)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)


# Create temporary file with contents of Default_Config.txt
temp_file = "temp_Config.txt"
with open("Default_Config.txt", "r") as f:
    temp_data = f.read()
with open(temp_file, "w") as f:
    f.write(temp_data)

# Use temporary file to read/edit until the application is closed
with open(temp_file, "r") as f:
    data = f.read()
    text = tk.Text(root)
    text.pack_forget()
    text.insert(tk.END, data)

root.title("ConfigWOW")


# add a label with centered text at the top
#title_label = tk.Label(root, text="", font=("Arial", 18, "bold"))
#title_label.pack(side=tk.TOP, anchor=tk.W,)

# add a label with author name under the title
author_label = tk.Label(root, text="", font=("Arial", 12, "italic"))
author_label.pack(side=tk.TOP, anchor=tk.W,)

# Add a spacer in between the General Information Section and the Acquisition section.
spacer1 = tk.Label(root, text="", font=("Arial", 18, "bold"))
spacer1.pack(side=tk.TOP, anchor=tk.W, padx=15, pady=0)

# add a label for General Information Section
GenInfo_label = tk.Label(root, text="General Switch Information", font=("Arial", 12, "bold"))
GenInfo_label.pack(side=tk.TOP, anchor=tk.W, padx=15, pady=0)

# add an Entry widget to prompt for the hostname
hostname_var = tk.StringVar()
hostname_label = tk.Label(root, text="Hostname:")
hostname_label.pack(side=tk.TOP, anchor=tk.W, padx=15, pady=0)
hostname_entry = tk.Entry(root, textvariable=hostname_var)
hostname_entry.pack(side=tk.TOP, anchor=tk.W, padx=15, pady=0)

# add a dropdown menu to prompt for the timezone
timezone_var = tk.StringVar(value="(GMT-6:00) America/Chicago")
timezone_label = tk.Label(root, text="Timezone:")
timezone_label.pack(side=tk.TOP, anchor=tk.W, padx=15, pady=0)
timezone_menu = tk.OptionMenu(root, timezone_var, "(GMT-5:00) America/New York", "(GMT-6:00) America/Chicago", "(GMT-8:00) America/Los Angeles")
timezone_menu.pack(side=tk.TOP, anchor=tk.W, padx=15, pady=0)

# add a menu button to prompt for the switch size
def update_switchports(*args):
    switchsize = int(switchsize_var.get())
    switchports_var.set(switchsize + 4)
    switchportsuplink_var.set(switchsize + 1)

switchsize_var = tk.StringVar(value="24")
switchsize_label = tk.Label(root, text="Switch Size:")
switchsize_label.pack(side=tk.TOP, anchor=tk.W, padx=15, pady=0)

# Update the callback function when the menu option is changed
switchsize_var.trace("w", update_switchports)

switchsize_menu = tk.OptionMenu(root, switchsize_var, "12", "24", "48")
switchsize_menu.pack(side=tk.TOP, anchor=tk.W, padx=15, pady=0)

# Set the initial values of switchports_var and switchportsuplink_var
switchsize = int(switchsize_var.get())
switchports_var = tk.StringVar(value=str(switchsize + 4))
switchportsuplink_var = tk.StringVar(value=str(switchsize + 1))

# Add a spacer in between the General Information Section and the Acquisition section.
spacer2 = tk.Label(root, text="", font=("Arial", 18, "bold"))
spacer2.pack(side=tk.TOP, anchor=tk.W, padx=15, pady=0)

# add a label for Acquisition Information Section
AcquisitionInfo_label = tk.Label(root, text="Acquisition Information", font=("Arial", 12, "bold"))
AcquisitionInfo_label.pack(side=tk.TOP, anchor=tk.W, padx=15, pady=0)

# Add a section to ask if this is a new Acquisition Switch
def toggle_entry():
    if new_acquisition_switch_var.get() == 1: # 1 corresponds to "Yes" being checked
        acquisitionvlan_entry.config(state="normal")
        acquisitionports_entry.config(state="normal")
    else:
        acquisitionvlan_entry.config(state="disabled")
        acquisitionports_entry.config(state="disabled")

new_acquisition_switch_var = tk.IntVar(value=0)
#new_acquisition_switch_label = tk.Label(root, text="New Acquisition Switch:")
#new_acquisition_switch_label.pack(side=tk.TOP, anchor=tk.W, padx=15, pady=0)

new_acquisition_switch_checkbutton = tk.Checkbutton(root, text="- Configure switch for new Acquisition", variable=new_acquisition_switch_var, command=toggle_entry)
new_acquisition_switch_checkbutton.pack(side=tk.TOP, anchor=tk.W, padx=15, pady=0)

# Add a section to ask what the name of new VLAN for the new acquisition will be.
acquisitionvlan_var = tk.StringVar()
acquisitionvlan_label = tk.Label(root, text="VLAN Name:")
acquisitionvlan_label.pack(side=tk.TOP, anchor=tk.W, padx=15, pady=0)
acquisitionvlan_entry = tk.Entry(root, textvariable=acquisitionvlan_var, state="disabled")
acquisitionvlan_entry.pack(side=tk.TOP, anchor=tk.W, padx=15, pady=0)

# Add a section to ask what the ports of the new VLAN for the acquisition will be.
acquisitionports_var = tk.StringVar()
acquisitionports_label = tk.Label(root, text="Untagged Ports:")
acquisitionports_label.pack(side=tk.TOP, anchor=tk.W, padx=15, pady=0)

acquisitionports_entry = tk.Entry(root, textvariable=acquisitionports_var, state="disabled")
acquisitionports_entry.pack(side=tk.TOP, anchor=tk.W, padx=15, pady=0)

# Add a spacer in between the Acquisition information section and the VLAN information Sections.
spacer3 = tk.Label(root, text="", font=("Arial", 18, "bold"))
spacer3.pack(side=tk.TOP, anchor=tk.W, padx=15, pady=0)

# add a label for VLAN Information Section
VLANInfo_label = tk.Label(root, text="VLAN Information", font=("Arial", 12, "bold"))
VLANInfo_label.pack(side=tk.TOP, anchor=tk.W, padx=15, pady=0)

# add an Entry widget to prompt for the Data VlAN IP
DataIP_var = tk.StringVar()
DataIP_label = tk.Label(root, text="Data VLAN IP:")
DataIP_label.pack(side=tk.TOP, anchor=tk.W, padx=15, pady=0)
DataIP_entry = tk.Entry(root, textvariable=DataIP_var)
DataIP_entry.pack(side=tk.TOP, anchor=tk.W, padx=15, pady=0)

# Add a section to ask what the ports of the Data VLAN will be.
DataVLANports_var = tk.StringVar()
DataVLANports_label = tk.Label(root, text="Untagged Data VLAN Ports:")
DataVLANports_label.pack(side=tk.TOP, anchor=tk.W, padx=15, pady=0)
#DataVLANportsInfo_label = tk.Label(root, text="(e.g. 1, 1-2, 1,5, 1-2,5 | 1:1, 1:1-1:2, 1:1,1:5, 1:1-1:2,2:5)")
#DataVLANportsInfo_label.pack(side=tk.TOP, anchor=tk.W, padx=15, pady=0)
DataVLANports_entry = tk.Entry(root, textvariable=DataVLANports_var, state="disabled")
DataVLANports_entry.pack(side=tk.TOP, anchor=tk.W, padx=15, pady=0)

# Add a section to ask if you want to configure Data VLAN Ports
def toggle_entry():
    if DataVLANportsButton_var.get() == 1: # 1 corresponds to "Yes" being checked
       DataVLANports_entry.config(state="normal")
    else:
        DataVLANports_entry.config(state="disabled")
        
DataVLANportsButton_var = tk.IntVar(value=0)
DataVLANportsButton_checkbutton = tk.Checkbutton(root, text="- Configure Untagged Data Ports", variable=DataVLANportsButton_var, command=toggle_entry)
DataVLANportsButton_checkbutton.pack(side=tk.TOP, anchor=tk.W, padx=15, pady=0)

# add an Entry widget to prompt for the Video VlAN IP
VideoIP_var = tk.StringVar()
VideoIP_label = tk.Label(root, text="Video VLAN IP:")
VideoIP_label.pack(side=tk.TOP, anchor=tk.W, padx=15, pady=0)
VideoIP_entry = tk.Entry(root, textvariable=VideoIP_var)
VideoIP_entry.pack(side=tk.TOP, anchor=tk.W, padx=15, pady=0)

# Add a section to ask what the ports of the Video VLAN will be.
VideoVLANports_var = tk.StringVar()
VideoVLANports_label = tk.Label(root, text="Untagged Video VLAN Ports:")
VideoVLANports_label.pack(side=tk.TOP, anchor=tk.W, padx=15, pady=0)
#VideoVLANportsInfo_label = tk.Label(root, text="(e.g. 1, 1-2, 1,5, 1-2,5 | 1:1, 1:1-1:2, 1:1,1:5, 1:1-1:2,2:5)")
#VideoVLANportsInfo_label.pack(side=tk.TOP, anchor=tk.W, padx=15, pady=0)
VideoVLANports_entry = tk.Entry(root, textvariable=VideoVLANports_var, state="disabled")
VideoVLANports_entry.pack(side=tk.TOP, anchor=tk.W, padx=15, pady=0)

# Add a section to ask if you want to configure Video VLAN Ports
def toggle_entry():
    if VideoVLANportsButton_var.get() == 1: # 1 corresponds to "Yes" being checked
        VideoVLANports_entry.config(state="normal")
    else:
        VideoVLANports_entry.config(state="disabled")
        
VideoVLANportsButton_var = tk.IntVar(value=0)
VideoVLANportsButton_checkbutton = tk.Checkbutton(root, text="- Configure Untagged Video Ports", variable=VideoVLANportsButton_var, command=toggle_entry)
VideoVLANportsButton_checkbutton.pack(side=tk.TOP, anchor=tk.W, padx=15, pady=0)

# add an Entry widget to prompt for the Wireless VlAN IP
WirelessIP_var = tk.StringVar()
WirelessIP_label = tk.Label(root, text="Wireless VLAN IP:")
WirelessIP_label.pack(side=tk.TOP, anchor=tk.W, padx=15, pady=0)
WirelessIP_entry = tk.Entry(root, textvariable=WirelessIP_var)
WirelessIP_entry.pack(side=tk.TOP, anchor=tk.W, padx=15, pady=0)

# Add a section to ask what the ports of the Wireless VLAN will be.
WirelessVLANports_var = tk.StringVar()
WirelessVLANports_label = tk.Label(root, text="Untagged Wireless VLAN Ports:")
WirelessVLANports_label.pack(side=tk.TOP, anchor=tk.W, padx=15, pady=0)
#WirelessVLANportsInfo_label = tk.Label(root, text="(e.g. 1, 1-2, 1,5, 1-2,5 | 1:1, 1:1-1:2, 1:1,1:5, 1:1-1:2,2:5)")
#WirelessVLANportsInfo_label.pack(side=tk.TOP, anchor=tk.W, padx=15, pady=0)
WirelessVLANports_entry = tk.Entry(root, textvariable=WirelessVLANports_var, state="disabled")
WirelessVLANports_entry.pack(side=tk.TOP, anchor=tk.W, padx=15, pady=0)

# Add a section to ask if you want to configure Wireless VLAN Ports
def toggle_entry():
    if WirelessVLANportsButton_var.get() == 1: # 1 corresponds to "Yes" being checked
        WirelessVLANports_entry.config(state="normal")
    else:
        WirelessVLANports_entry.config(state="disabled")
        
WirelessVLANportsButton_var = tk.IntVar(value=0)
WirelessVLANportsButton_checkbutton = tk.Checkbutton(root, text="- Configure Untagged Wireless Ports", variable=WirelessVLANportsButton_var, command=toggle_entry)
WirelessVLANportsButton_checkbutton.pack(side=tk.TOP, anchor=tk.W, padx=15, pady=0)

# add a Button widget to save the file
def save_file():
    timezone = timezone_var.get()
    if timezone == "(GMT-5:00) America/New York":
        timezone_replacement = "EST"
    elif timezone == "(GMT-6:00) America/Chicago":
        timezone_replacement = "CST"
    elif timezone == "(GMT-8:00) America/Los Angeles":
        timezone_replacement = "PST"
    
    # Get the text content from the Text widget
    data = text.get("1.0", tk.END)

    # Replace the placeholder texts with actual values
    data = data.replace("<hostname>", hostname_var.get())
    data = data.replace("<timezone>", timezone_var.get())
    data = data.replace("<switchports>", switchports_var.get())
    data = data.replace("<switchportsuplink>", switchportsuplink_var.get())
    data = data.replace("<acquisitionvlan>", acquisitionvlan_var.get())
    data = data.replace("<acquisition_untagged>", acquisitionports_var.get())
    data = data.replace("<dataports_untagged>", DataVLANports_var.get())
    data = data.replace("<videoports_untagged>", VideoVLANports_var.get())
    data = data.replace("<wirelessports_untagged>", WirelessVLANports_var.get())    
    
    filename = filedialog.asksaveasfilename(initialdir="./", title="Save As", initialfile=f"{hostname_var.get()}.txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    with open(filename, "w") as f:
        f.write(data)

save_button = tk.Button(root, text="Save", command=save_file)
save_button.pack(side=tk.BOTTOM, padx=15, pady=25)

root.mainloop()

# wait until the window is closed by the user
root.wait_visibility()
root.destroy()
