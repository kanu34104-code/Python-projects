4. #Shutdown app using Python GUI
from tkinter import *
import os

def restart():
    os.system("shutdown /r /t 1")
def restart_time():
    os.system("shutdown /r /t 20")
def logout():
    os.system("shutdown -l")
def shutdown():
    os.system("shutdown /s /t 1")            

st = Tk()
st.title("Shutdown App")
st.geometry("500x400")
st.config(bg="lightblue")

r_button = Button(st, text="Restart", font=("Ariel",20,"bold"), 
                  relief=RAISED,cursor="hand2", command=restart)
r_button.place(x=150,y=60,width=200,height=40)

rt_button = Button(st, text="Restart Time", font=("Ariel",20,"bold"), 
                   relief=RAISED,cursor="hand2", command=restart_time)
rt_button.place(x=150,y=170,width=200,height=40)

lg_button = Button(st, text="Log-Out", font=("Ariel",20,"bold"), 
                   relief=RAISED,cursor="hand2", command=logout)
lg_button.place(x=150,y=270,width=200,height=40)

lg_button = Button(st, text="Shutdown", font=("Ariel",20,"bold"), 
                   relief=RAISED,cursor="hand2", command=shutdown)
lg_button.place(x=150,y=370,width=200,height=40)


#st.bind('<Escape>', lambda e: st.quit())
st.mainloop()


