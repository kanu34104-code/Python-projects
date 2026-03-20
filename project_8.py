6. #Internet Speed Test using Python with GUI
from tkinter import *
import speedtest

def speedcheck():
    spd = speedtest.Speedtest()
    spd.get_servers()
    dl = str(round(spd.download()/(10**6), 3))+ "Mbps"
    ul = str(round(spd.upload()/(10**6), 3))+ "Mbps"
    lab_dl.config(text=dl)
    lab_ul.config(text=ul)

sp = Tk()
sp.title("Internet Speed Test")
sp.geometry("500x7000")
sp.config(bg="lightblue")

lab = Label(sp, text="Internet Speed Test", font=("Ariel", 24, "bold"), bg="lightblue", fg="black")
lab.place(x=60, y=40, width=380, height=50)

lab_dl = Label(sp, text="Download Speed", font=("Ariel", 24, "bold"), bg="lightblue", fg="black")
lab_dl.place(x=60, y=130, width=380, height=50)

lab = Label(sp, text="00", font=("Ariel", 24, "bold"), bg="lightblue", fg="black")
lab.place(x=60, y=200, width=380, height=50)

lab_ul = Label(sp, text="Upload Speed", font=("Ariel", 24, "bold"), bg="lightblue", fg="black")
lab_ul.place(x=60, y=290, width=380, height=50)

lab = Label(sp, text="00", font=("Ariel", 24, "bold"), bg="lightblue", fg="black")
lab.place(x=60, y=360, width=380, height=50)

button = Button(sp, text="Check Speed", font=("Ariel", 24, "bold"), bg="lightgreen", relief=RAISED, command=speedcheck)
button.place(x=60, y=460, width=380, height=50)


sp.mainloop()