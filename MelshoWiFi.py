from Tkinter import *
import tkMessageBox
import tempfile
import wifi

top = Tk()
status_text = StringVar()

def get_status():
    info = wifi.show_wifi()
    stat = info['Status']
    if stat == 'Started\r':
        s = "Status : %s Number of clients : %s  BSSID : %s Radio type : %s Channel : %s"%(info['Status'],info['Number of clients'],info['BSSID'],info['Radio type'],info['Channel'])
        h = 400
        c = 'dark green'
    else:
        h = 320
        s = "Status : %s"%(info['Status'])
        c = 'red'
    status_text.set(s)
    return s, h, c
    

def create():
    k = key.get()
    if k and len(k) < 8 :
        tkMessageBox.showinfo("Password Error", "password must be more than 8 charachters")
    else:
        output,msg = wifi.create_new(ssid.get(),k)
        tkMessageBox.showinfo("hotspot created",msg)
        center_window(300, 400)
        s,h,c = get_status()
        status.configure(fg=c)

def start():
    output, msg = wifi.start_wifi()
    tkMessageBox.showinfo("Hotspot started", msg)
    get_status()
    center_window(300, 400)
    s,h,c = get_status()
    status.configure(fg=c)
    
    

def stop():
    output, msg = wifi.stop_wifi()
    tkMessageBox.showinfo("Hotspot stopped", msg)
    get_status()
    status.configure
    center_window(300, 320)
    s,h,c = get_status()
    status.configure(fg=c)
    



top.iconbitmap(default="icon.ico")
top.title("Melsho Hotspot Creator")
top.resizable(0,0)

h= 180
def center_window(w=300, h=200):
    # get screen width and height
    ws = top.winfo_screenwidth()
    hs = top.winfo_screenheight()
    # calculate position x, y
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    top.geometry('%dx%d+%d+%d' % (w, h, x, y))

# hotspot creation wizard
labelframe = LabelFrame(top, text="Create New WiFi Hotspot")
labelframe.pack(fill="both", expand="yes")

ssid_frame = Frame(labelframe)
ssid_frame.pack()

ssid_label = Label(ssid_frame, text="Hotspot Name      ")
ssid_label.pack(side=LEFT)
ssid = Entry(ssid_frame, bd=5)
ssid.pack(side=RIGHT)

key_frame = Frame(labelframe)
key_frame.pack()

key_label = Label(key_frame, text="Hotspot Password")
key_label.pack(side=LEFT)
key = Entry(key_frame, bd=5)
key.pack(side=RIGHT)

create_frame = Frame(labelframe)
create_frame.pack()

create = Button(create_frame, text="Create WiFi Hotspot", command=create, bd=2)
create.pack()

# wifi control buttons
labelframe_2 = LabelFrame(top, text="Control WiFi Hotspot")
labelframe_2.pack(fill="both", expand="yes")

control_frame = Frame(labelframe_2)
control_frame.pack()

start = Button(control_frame, text="Start WiFi Hotspot",command=start, bd=2)
stop = Button(control_frame, text="Stop WiFi Hotspot",command=stop, bd=2)
start.pack(side=LEFT)
stop.pack(side=RIGHT)

# wifi status and settings

# status

labelframe_3 = LabelFrame(top, text="WiFi Hotspot Status")
labelframe_3.pack(fill="both", expand="yes")
status = Label(labelframe_3, textvariable=status_text)
status.pack()
s,h,c = get_status()
status.configure(fg=c)

def show_sett():
    #settings
    info = wifi.show_wifi()
    labelframe_4 = LabelFrame(top, text="WiFi Hotspot Settings")
    labelframe_4.pack(fill="both", expand="yes")
    mode = Label(labelframe_4,text='Mode : '+info['Mode'])
    ssid_name = Label(labelframe_4,text='SSID name : '+info['SSID name'])
    max_no = Label(labelframe_4,text='Max number of clients : '+info['Max number of clients'])
    auth = Label(labelframe_4,text='Authentication : '+info['Authentication'])

    mode.pack()
    ssid_name.pack()
    max_no.pack()
    auth.pack()





# initialize

show_sett()
center_window(300, h)

#copyright
copyright = Label(top, text="created by Mahmoud Elshobaky")
copyright.pack()

#make shure the app runs as adminstrator
import admin
if admin.isUserAdmin():
    top.mainloop()
else:
    admin.runAsAdmin()
        


