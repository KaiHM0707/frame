import tkinter as tk
scr = tk.Tk()
scr.title("frames")

#creating frames
frame1 = tk.Frame(scr, borderwidth=2, relief="ridge",bg="blue")
frame1.pack(pady=10,padx=10,expand = True,fill=tk.BOTH)
sign = tk.Label(frame1, text="i am framed", fg="black", bg="lightgreen",font=("Times", 20))
sign.pack(padx=20,pady=20,ipadx=20,ipady=20)

frame2 = tk.Frame(frame1,borderwidth=2,relief = "groove",bg="red")
frame2.pack(side=tk.LEFT,pady=15,padx=15,expand=True,fill=tk.BOTH)
sign2 = tk.Label(frame2, text="I am also framed",bg="lightblue")
sign2.pack(padx=15,pady=15,ipadx=20,ipady=20)

frame3 = tk.Frame(frame1,borderwidth=4,relief="sunken",bg="green")
frame3.pack(side=tk.RIGHT,padx=20,pady=20,expand=True,fill=tk.BOTH)
sign3 = tk.Label(frame3, text="I also am framed", bg="pink")
sign3.pack(padx=20,pady=20,ipadx=20,ipady=20)

scr.mainloop()
