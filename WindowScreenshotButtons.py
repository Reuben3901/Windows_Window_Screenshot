from PIL import ImageGrab
from tkinter import *
import win32gui, time

root = Tk()
root.title("Window Screenshots")
root.geometry("280x38")
counter = 1

toplist, winlist = [], []


def enum_cb(hwnd, results):
    winlist.append((hwnd, win32gui.GetWindowText(hwnd)))
    
def grabImg(text):
    global counter,toplist,winlist
    win32gui.EnumWindows(enum_cb, toplist)
    windows = [(hwnd, title) for hwnd, title in winlist if text in title.lower()]

    for window in windows:
        hwnd = window[0]

        win32gui.SetForegroundWindow(hwnd)
        time.sleep(.5)
        bbox = win32gui.GetWindowRect(hwnd)
        x1,y1,x2,y2 = bbox
        bbox = (x1+7),y1,(x2-7),(y2-7)
        img = ImageGrab.grab(bbox)
        img.save(text+"_"+str(hwnd)+"_"+str(img.width)+"_"+str(img.height)+"_"+str(counter)+".png", "PNG")
        counter += 1
        time.sleep(1)
        
    toplist, winlist = [], []


topFrame = Frame(root)
topFrame.pack()
#middleFrame = Frame(root)
#middleFrame.pack()
#bottomFrame= Frame(root)
#bottomFrame.pack()

button1 = Button(topFrame, text='spreadsheet', fg='green', command = lambda: grabImg(text='libreoffice'))
button2 = Button(topFrame, text='pdf', fg='red', command = lambda: grabImg(text='adobe acrobat'))
button3 = Button(topFrame, text='Notepad', fg='blue', command = lambda: grabImg(text='notepad'))
button4 = Button(topFrame, text='Chrome', fg='orange', command = lambda: grabImg(text='chrome'))
#button3 = Button(middleFrame, text='Notepad', fg='blue', command = NotepadImg)

button1.pack(side=LEFT, padx=5, pady=5)
button2.pack(side=LEFT, padx=5, pady=5)
button3.pack(side=LEFT, padx=5, pady=5)
button4.pack(side=LEFT, padx=5, pady=5)
root.mainloop()
