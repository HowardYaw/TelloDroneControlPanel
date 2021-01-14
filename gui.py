from tkinter import *
import tello
import tkinter.font as tkFont
from Action import Action
from video import Video
from threading import Thread
import time

window = Tk()
window.title("Drone Control Panel")
window.geometry("800x600")

actions = Action()
video_handler = Video()

manualMode = BooleanVar()
videoStreaming = BooleanVar()
batteryValue = IntVar()

def connection() :
    drone = actions.connectToDrone()
    connectionButton.config(text="Connected", state=DISABLED)
    lightButton.config(bg="lime green")
    label.config(text="Connected!")
    battery_thread.start()
    video_handler.setTello(drone)

def updateBattery():
    while True:
        batteryValue = actions.getCurrentBattery()
        if (batteryValue != None):
            batteryButton.config(text=str(batteryValue)+"%")
        time.sleep(60)

def autoMode() :
    modeButton.config(text="On Manual", command=manualControlMode)
    label.config(text="Auto Mode")
    manualMode = True
    pre_plan_route_process.start()

def manualControlMode() :
    modeButton.config(text="On Auto", command=autoMode)
    label.config(text="Manual Mode")
    actions.stopPrePlanRoute()
    manualMode = False
    pre_plan_route_process.join()

def onVideoStream() :
    videoStreaming = video_handler.streamOn()
    videoStreamButton.config(text="Video Off", command=offVideoStream)
    # video_frame_thread = Thread(target=updateFrameVideoImage, daemon=True)
    # video_frame_thread.start()

def offVideoStream() :
    video_handler.streamOff()
    videoStreamButton.config(text="Video On", command=onVideoStream)
    videoStreaming = False

def updateFrameVideoImage():
    while videoStreaming:
        frm_cam.config(image=video_handler.get_frame())

def forward() :
    actions.move("forward") if manualMode else print('Not Manual Mode')

def back() :
    actions.move("back") if manualMode else print('Not Manual Mode')

def left() :
    actions.move("left") if manualMode else print('Not Manual Mode')

def right() :
    actions.move("right") if manualMode else print('Not Manual Mode')


#Add widget
frm_main = Frame(window, bg="dark grey")
frm_right = Frame(frm_main, bg="dark grey")
frm_left = Frame(frm_main, bg="dark grey")
frm_cam = Frame(frm_left, bg="blue", width=500, height=200)
frm_printOut = Frame(frm_left, bg="black", width=500, height=10)

fontStyle = tkFont.Font(family="Lucida Grande", size=20)
label = Label(frm_printOut, fg="white", bg="black", font=fontStyle)

batteryButton = Button(frm_right, text="0%", state=DISABLED, height=2, width=2)
lightButton = Button(frm_right, text="    ", bg="red", state=DISABLED, height=2, width=2)

connectionButton = Button(frm_right, text="Connect", activebackground="grey", padx=5, pady=5, height=2, width=2, command=connection)
modeButton = Button(frm_right, text="On Manual", activebackground="grey", pady=5, height=2, width=2, command=manualControlMode)

videoStreamButton = Button(frm_right, text="Video On", activebackground="grey", padx=5, pady=5, height=3, width=6, command=onVideoStream)
takeOffButton = Button(frm_right, text="Take off", activebackground="grey", padx=5, pady=5, height=3, width=6, command=actions.takeOff)
landButton = Button(frm_right, text="Land", activebackground="grey", padx=5, pady=5, height=3, width=6, command=actions.landing)

fowardButton = Button(frm_right, text="Forward", activebackground="grey", padx=5, pady=5, height=3, width=5, command=forward)
backButton = Button(frm_right, text="Backward", activebackground="grey", padx=5, pady=5, height=3, width=5, command=back)
leftButton = Button(frm_right, text="Left", activebackground="grey", padx=5, pady=5, height=3, width=5, command=left)
rightButton = Button(frm_right, text="Right", activebackground="grey", padx=5, pady=5, height=3, width=5, command=right)


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

videoStreamButton.grid(row=8, column=2, padx=5, pady=5, sticky="nsew")
takeOffButton.grid(row=8, column=3, padx=5, pady=5, sticky="nsew")
landButton.grid(row=8, column=4, padx=5, pady=5, sticky="nsew")

fowardButton.grid(row=10, column=3, padx=5, pady=5, sticky="nsew")
backButton.grid(row=11, column=3, padx=5, pady=5, sticky="nsew")
leftButton.grid(row=11, column=2, padx=5, pady=5, sticky="nsew")
rightButton.grid(row=11, column=4, padx=5, pady=5, sticky="nsew")

frm_printOut.grid_rowconfigure(0, weight=1)
frm_printOut.grid_columnconfigure(0, weight=1)
frm_printOut.grid_rowconfigure(12, weight=1)
frm_printOut.grid_columnconfigure(12, weight=1)

frm_left.grid_rowconfigure(0, weight=1)
frm_left.grid_columnconfigure(0, weight=1)
frm_left.grid_rowconfigure(12, weight=1)
frm_left.grid_columnconfigure(12, weight=1)

frm_right.grid_rowconfigure(0, weight=1)
frm_right.grid_columnconfigure(0, weight=1)
frm_right.grid_rowconfigure(12, weight=1)
frm_right.grid_columnconfigure(12, weight=1)

battery_thread = Thread(target=updateBattery, daemon=True)
pre_plan_route_process = Thread(target=actions.startPrePlanRoute, daemon=True)
window.mainloop()