from plyer import notification
import rotatescreen
from tkinter import*
from tkinter import messagebox
import time

class rotate_screen:
    def __init__(self, root):
        self.root = root
        self.root.title("!!! Virus !!!")
        self.root.geometry("250x200")
        self.root.wm_iconbitmap("images//virus.ico")
        self.root.resizable(False, False)

        # ================ Variable ===========
        self.var_num = IntVar()

        txt_num = Entry(self.root, textvariable=self.var_num, font="consolos 14 bold", bd=3, relief=RIDGE, width=19).place(x=15, y=20)

        start_bt = Button(self.root, text="START", font="calibri 20 bold", width=15, command=self.start, cursor="hand2", bd=0, bg="#008EA4", fg="white").place(x=15, y=60)
        stop_bt = Button(self.root, text="STOP", font="calibri 20 bold", command=root.destroy, width=15, cursor="hand2", bd=0, bg="#DF002A", fg="white").place(x=15, y=120)


    def start(self):
        screen = rotatescreen.get_primary_display()

        for i in range(self.var_num.get()):
            time.sleep(1)
            screen.rotate_to(i*90%360)
            notification.notify( 

                title = "!!! Virus !!! Virus !!! ", 
                message="YOU HAVE STARTED AT YOUR OWN RISK" , 
                app_name = "VIRUS - | BY SUHAS NIDGUNDI |",
                app_icon = "images\\virus.ico",
                ticker = "| BY SUHAS NIDGUNDI |",
                timeout=10

            )

root = Tk()
obj = rotate_screen(root)
root.mainloop()