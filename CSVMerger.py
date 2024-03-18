import tkinter as tk
from tkinter import Button, Label, LabelFrame, Entry, filedialog, StringVar, messagebox, BooleanVar, Checkbutton
import csvhandling

# region function
#Folder browser function
def openPath():
    global folder_path
    folder_path.set(filedialog.askdirectory())

#Starting program function
def startMerging():
    path = str(folder_path_entry.get())
    name = str(file_name_entry.get())
    header = bool(merge_header.get())
    
    file_list = csvhandling.getCSVFilesPath(path, name)
    file_count = csvhandling.mergeCSV(file_list, path, header)

    if file_count == 0:
        message_log = "Not found file that contain name = " + name
    elif file_count == 1:
        message_log = "Found 1 file that contain name =" + name
    else:
        message_log = "Merging " + str(file_count) + " files completed"
    
    return messagebox.showwarning(title="Finish", message=message_log)
    
# endregion
    
#Create tkinter object
window = tk.Tk()
window.title("CSV Merger")

#Create frame object
frame = tk.Frame(window)
frame.pack()

# region Frame layout in gui
#Create frame in gui
file_filter_frame = LabelFrame(frame, text="Enter Folder path and common filename that you want to merge")
start_frame = Button(frame, text="Starting merging........",command=startMerging)

#Setting layout in gui
file_filter_frame.grid(row=0,column=0,sticky="ew")
start_frame.grid(row=1,column=0,columnspan=4,sticky='nwes')
# endregion

# region 'Input path and file name filter frame'
#Create element in 'Input path and filename filter'
folder_path_label = Label(file_filter_frame, text="Files path")
file_name_label = Label(file_filter_frame, text="File name filter", width=10)
folder_path_button = Button(file_filter_frame, text="Select folder", command=openPath)
folder_path = StringVar()
folder_path_entry = Entry(file_filter_frame, textvariable=folder_path, width=40)
file_name_entry = Entry(file_filter_frame)
merge_header = BooleanVar()
merge_header.set(False)
merge_header_button = Checkbutton(file_filter_frame, text = "Use first file header", variable = merge_header)
#Setting element layout in 'Input path and file name filter frame'
folder_path_label.grid(row=0, column=1, sticky="sw")
file_name_label.grid(row=0, column=2, sticky="sw")
folder_path_button.grid(row=1,column=0,padx=5,pady=2)
folder_path_entry.grid(row=1, column=1)
file_name_entry.grid(row=1,column=2)
merge_header_button.grid(row=1,column=3)
# endregion

#Start GUI
window.mainloop()