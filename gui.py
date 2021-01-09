from tkinter import *
import tello
import tkinter.font as tkFont

window = Tk()
window.title("Drone GUI")
window.geometry("800x600")


def connection() :
    import Action
    Action.connectToDrone()
    connectionButton.config(text="Connected", state=DISABLED)
    lightButton.config(bg="lime green")
    label.config(text="Connected!")

def mode() :
    modeButton.config(text="Manual", command=reMode)
    label.config(text="Manual Mode")

def reMode() :
    modeButton.config(text="Auto", command=mode)
    label.config(text="Auto Mode")

# def forward() :
#     # tello.billy.send("forward 50", 4)

# def back() :
#     # tello.billy.send("back 50", 4)

# def left() :
#     # tello.billy.send("left 50", 4)

# def right() :
#     tello.billy.send("right 50", 4)

#Add widget
frm_main = Frame(window, bg="dark grey")
frm_right = Frame(frm_main, bg="dark grey")
frm_left = Frame(frm_main, bg="dark grey")
frm_cam = Frame(frm_left, bg="blue", width=500, height=200)
frm_printOut = Frame(frm_left, bg="black", width=500, height=10)

fontStyle = tkFont.Font(family="Lucida Grande", size=20)
label = Label(frm_printOut, fg="white", bg="black", font=fontStyle)

batteryButton = Button(frm_right, text="78%", state=DISABLED, height=2, width=2)
lightButton = Button(frm_right, text="    ", bg="red", state=DISABLED, height=2, width=2)

connectionButton = Button(frm_right, text="Connect", activebackground="grey", padx=5, pady=5, height=2, width=2, command=connection)
modeButton = Button(frm_right, text="Auto", activebackground="grey", pady=5, height=2, width=2, command=mode)

upButton = Button(frm_right, text="Up", activebackground="grey", padx=5, pady=5, height=3, width=5)
downButton = Button(frm_right, text="Down", activebackground="grey", padx=5, pady=5, height=3, width=5)
leftButton = Button(frm_right, text="Left", activebackground="grey", padx=5, pady=5, height=3, width=5)
rightButton = Button(frm_right, text="Right", activebackground="grey", padx=5, pady=5, height=3, width=5)


#Display widget
frm_main.pack(side=LEFT, fill=BOTH, expand=TRUE)
frm_left.pack(side=LEFT, fill=BOTH, expand=TRUE, anchor=CENTER)
frm_cam.pack(padx=5, pady=5, fill=BOTH, anchor=CENTER, expand=TRUE)
frm_printOut.pack(padx=5, pady=5, fill=BOTH, expand=TRUE)
frm_right.pack(side=LEFT, fill=BOTH, expand=TRUE)

label.grid(row=1, column=1)

batteryButton.grid(row=1, column=2, padx=5, pady=5, columnspan=2, sticky="nsew")
lightButton.grid(row=1, column=4, padx=5, pady=5, columnspan=1, sticky="ns")

connectionButton.grid(row=3, column=1, padx=5, pady=5, columnspan=4, sticky="nsew")
modeButton.grid(row=6, column=1, padx=5, pady=5, columnspan=4, sticky="nsew")

upButton.grid(row=8, column=3, padx=5, pady=5, sticky="nsew")
downButton.grid(row=9, column=3, padx=5, pady=5, sticky="nsew")
leftButton.grid(row=9, column=2, padx=5, pady=5, sticky="nsew")
rightButton.grid(row=9, column=4, padx=5, pady=5, sticky="nsew")

frm_printOut.grid_rowconfigure(0, weight=1)
frm_printOut.grid_columnconfigure(0, weight=1)
frm_printOut.grid_rowconfigure(10, weight=1)
frm_printOut.grid_columnconfigure(10, weight=1)

frm_left.grid_rowconfigure(0, weight=1)
frm_left.grid_columnconfigure(0, weight=1)
frm_left.grid_rowconfigure(10, weight=1)
frm_left.grid_columnconfigure(10, weight=1)

frm_right.grid_rowconfigure(0, weight=1)
frm_right.grid_columnconfigure(0, weight=1)
frm_right.grid_rowconfigure(10, weight=1)
frm_right.grid_columnconfigure(10, weight=1)

window.mainloop()