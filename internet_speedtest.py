from tkinter import *
import speedtest
import threading

def speedcheck():
    lab_down.config(text="Checking...")
    lab_up.config(text="Checking...")
    
    t = threading.Thread(target=run_speedtest)
    t.start()

def run_speedtest():
    sp = speedtest.Speedtest()
    sp.get_best_server()
    
    down = str(round(sp.download() / (10**6), 3)) + " Mbps"
    up = str(round(sp.upload() / (10**6), 3)) + " Mbps"
    
    lab_down.config(text=down)
    lab_up.config(text=up)

sp = Tk()
sp.title("Internet Speed Test")
sp.geometry("500x700")
sp.config(bg="blue")

Label(sp, text="Internet Speed Test",
      font=("Times New Roman", 30, "bold"),
      bg="blue", fg="white").place(x=50, y=40, width=380)

Label(sp, text="Download Speed",
      font=("Times New Roman", 30, "bold")).place(x=50, y=130, width=380)

lab_down = Label(sp, text="00",
                 font=("Times New Roman", 30, "bold"))
lab_down.place(x=50, y=190, width=380)

Label(sp, text="Upload Speed",
      font=("Times New Roman", 30, "bold")).place(x=50, y=260, width=380)

lab_up = Label(sp, text="00",
               font=("Times New Roman", 30, "bold"))
lab_up.place(x=50, y=320, width=380)

Button(sp, text="Check Speed",
       font=("Times New Roman", 30, "bold"),
       bg="red",
       command=speedcheck).place(x=50, y=400, width=380)

sp.mainloop()