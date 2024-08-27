from tkinter import messagebox
import speedtest
from tkinter import *

#WINDOW
win = Tk()
win.geometry("300x600")
win.title("Speedtest")
win.config(background="#19096b")


#MAIN
def test_network_speed():
    messagebox.showinfo(title="Note", message="Please wait until the speedtest show the results")

    # Create a Speedtest object
    st = speedtest.Speedtest()

    # Get the best server based on ping
    best_server = st.get_best_server()

    # Extract host and location information
    host = best_server['host']
    server_location = f"{best_server['name']}, {best_server['country']}"

    # Perform the download and upload speed tests
    download_speed = st.download()
    upload_speed = st.upload()

    # Get the ping (latency)
    ping = st.results.ping

    # Convert speeds to Mbps
    download_speed_mbps = download_speed / 1_000_000
    upload_speed_mbps = upload_speed / 1_000_000

    # Update labels with the results
    host_label.config(text=f'Server: {host}')
    location_label.config(text=f'Location: {server_location}')
    ping_label.config(text=f'{ping:.2f} ms')
    download_label.config(text=f'{download_speed_mbps:.2f} Mbps')
    upload_label.config(text=f'{upload_speed_mbps:.2f} Mbps')




#BUTTONS
b1 = Button(win, text="START", command=test_network_speed,background="#fcd22a",width=25,height=4,font=('bold'))
b1.pack()

Label(win, text='Ping:', background="#19096b", foreground="white",width=10,height=2,font=('bold')).place(x=0,y=150)
ping_label = Label(win, text='', background="#19096b", foreground="white")
ping_label.place(x=70,y=160)

Label(win, text='Download:', background="#19096b", foreground="white",width=10,height=2,font=('bold')).place(x=0,y=225)
download_label = Label(win, text='', background="#19096b", foreground="white")
download_label.place(x=90,y=235)

Label(win, text='Upload:', background="#19096b", foreground="white",width=10,height=2,font=('bold')).place(x=0,y=300)
upload_label = Label(win, text='', background="#19096b" , foreground="white")
upload_label.place(x=80,y=310)

host_label = Label(win, text='Server:', background="#19096b", foreground="white",font=('bold'))
host_label.place(x=0,y=400)

location_label = Label(win, text='Location:', background="#19096b", foreground="white",font=('bold'))
location_label.place(x=0 ,y=450)

Made=Label(win,text="Made by Nariman with ❤️", background="#19096b", foreground="white",font=('bold'))
Made.place(x=65,y=575)

win.mainloop()
