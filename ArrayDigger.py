import tkinter as tk
from tkinter import Button, Label, LabelFrame, Entry, filedialog, StringVar, messagebox
import csvhandling

# region function
#Folder browser function
def openPath():
    global folder_path
    folder_path.set(filedialog.askdirectory())
#Starting program function
def startDigging():
    path = str(folder_path_entry.get())
    name = str(file_name_entry.get())
    col = int(targ_x_entry.get())
    row = int(targ_y_entry.get())
    width = int(arr_width_entry.get())
    height = int(arr_height_entry.get())
    
    file_list = csvhandling.getCSVFilesPath(path, name)
    file_count = csvhandling.loopDiggingArray(file_list, row, col, width, height)

    if file_count == 0:
        message_log = "Not found file that contain name = " + name
    elif file_count == 1:
        message_log = "Digging 1 file completed"
    else:
        message_log = "Digging " + str(file_count) + " files completed"
    
    return messagebox.showwarning(title="Finish", message=message_log)
# endregion

#Create tkinter object
window = tk.Tk()
window.title("CSV Array Digger")

#Create frame object
frame = tk.Frame(window)
frame.pack()


# region Frame layout in gui
#Create frame in gui
file_filter_frame = LabelFrame(frame, text="Enter Folder path and common filename that you want to dig")
targ_frame = LabelFrame(frame, text="Enter starting array postion")
arr_frame = LabelFrame(frame, text="Enter array size")
start_frame = Button(frame, text="Starting digging........",command=startDigging)
#Setting layout in gui
file_filter_frame.grid(row=0,column=0,columnspan=4,sticky="ew")
targ_frame.grid(row=1, column=0,sticky='nwes')
arr_frame.grid(row=1,column=1,sticky='nwes')
start_frame.grid(row=1,column=3,sticky='nwes')
# endregion

# region 'Input path and file name filter frame'
#Create element in 'Input path and filename filter'
folder_path_label = Label(file_filter_frame, text="Files path")
file_name_label = Label(file_filter_frame, text="File name filter", width=10)
folder_path_button = Button(file_filter_frame, text="Select folder", command=openPath)
folder_path = StringVar()
folder_path_entry = Entry(file_filter_frame, textvariable=folder_path, width=40)
file_name_entry = Entry(file_filter_frame)
#Setting element layout in 'Input path and file name filter frame'
folder_path_label.grid(row=0, column=1, sticky="sw")
file_name_label.grid(row=0, column=2, sticky="sw")
folder_path_button.grid(row=1,column=0,padx=5,pady=2)
folder_path_entry.grid(row=1, column=1)
file_name_entry.grid(row=1,column=2)
# endregion

# region 'Coordidate of starting cell frame'
#Create element in 'Coordidate of starting cell frame'
targ_x_label = Label(targ_frame, text="Column")
targ_y_label = Label(targ_frame, text="Row")
targ_x_entry = Entry(targ_frame, width=4)
targ_text = Label(targ_frame, text=",")
targ_y_entry = Entry(targ_frame, width=4)
#Setting element layout 'Coordidate of starting cell frame'
targ_x_label.grid(row=0, column=0)
targ_y_label.grid(row=0, column=2)
targ_x_entry.grid(row=1, column=0)
targ_text.grid(row=1,column=1)
targ_y_entry.grid(row=1, column=2)
# endregion

# region 'Array size frame'
#Create element in 'Array size frame'
arr_width_label = Label(arr_frame, text="Width")
arr_height_label = Label(arr_frame, text="Height")
arr_width_entry = Entry(arr_frame, width=4)
x_text = Label(arr_frame, text="x")
arr_height_entry = Entry(arr_frame, width=4)
#Setting element layout in 'Array size frame'
arr_width_label.grid(row=0,column=0)
arr_height_label.grid(row=0,column=2)
arr_width_entry.grid(row=1, column=0)
x_text.grid(row=1,column=1)
arr_height_entry.grid(row=1,column=2)
# endregion

#Start GUI
window.mainloop()


