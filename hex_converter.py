import customtkinter as ctk
import tkinter
from customtkinter import filedialog
from tkinter import messagebox
import os


def converter(hexfilepath, goodbasename):
    #creating a list for good lines
    datas = []

    try:
        #convert and append the good lines from the hex files
        with open(hexfilepath, "r") as hexfile:
            for hexline in hexfile:
                currentline = hexline.split(" ")                
                currentline = currentline[1]                
                cuurentline_bytes = bytes.fromhex(currentline)
                currentline = cuurentline_bytes.decode("ascii")

                datas.append(currentline)

        numDatas = len(datas)

        hexfiledir = os.path.dirname(hexfilepath)
        readyfilepath = os.path.join(hexfiledir, goodbasename)

        #debug
        print(f"hexfiledir:{hexfiledir}, readyfilepath:{readyfilepath}")

        with open(readyfilepath, "w") as file:
            for i in range(0,numDatas):
                file.write(datas[i] + "\n")
    except:
        messagebox.showerror("Error", "Couldn't create the new file!")


def submit():
    global hexfilepath_string

    #read the new file's name
    text_entry = entry.get()
    goodbasename_string = text_entry
    window.destroy()

    #get the path for the hexfile
    hexfilepath_string = filedialog.askopenfilename()

    converter(hexfilepath_string, goodbasename_string)
    

def preconverter():
    #get the name of the new file
    global window, entry
    window = ctk.CTkToplevel()
    window.geometry("150x60")
    window.title("Entry Window")

    entry = ctk.CTkEntry(window)
    entry.pack()

    submit_button = ctk.CTkButton(window, text="Submit", command=submit)
    submit_button.pack()


root = ctk.CTk()
root.title("Hex-converter")
root.geometry("250x30")

converter_button = ctk.CTkButton(root, text="Convert", command = preconverter)
converter_button.pack(pady=5)

root.mainloop()