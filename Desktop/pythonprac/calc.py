import tkinter as tk


def button_click(number):
    
    current = entery1.get() 
    entery1.delete(0, tk.END)  
    entery1.insert(0, str(current) + str(number))




root = tk.Tk()
root.geometry("300x200")

entery1=tk.Entry(root)
entery2=tk.Entry(root)






b0 = tk.Button(root, text="0", bg="orange", command=lambda: button_click(0))
b1 = tk.Button(root, text="1", bg="orange", command=lambda: button_click(1))
b2 = tk.Button(root, text="2", bg="orange", command=lambda: button_click(2))
b3 = tk.Button(root, text="3", bg="orange", command=lambda: button_click(3))
b4 = tk.Button(root, text="4", bg="orange", command=lambda: button_click(4))
b5 = tk.Button(root, text="5", bg="orange", command=lambda: button_click(5))
b6 = tk.Button(root, text="6", bg="orange", command=lambda: button_click(6))
b7 = tk.Button(root, text="7", bg="orange", command=lambda: button_click(7))
b8 = tk.Button(root, text="8", bg="orange", command=lambda: button_click(8))
b9 = tk.Button(root, text="9", bg="orange", command=lambda: button_click(9))



entery1.grid(row=3,column=1,padx=10,pady=5)
entery2.grid(row=4,column=1,padx=10,pady=5)
b0.grid(row=5,column=0,padx=10,pady=5)

b1.grid(row=5,column=1,padx=10,pady=5)
b2.grid(row=5,column=2,padx=10,pady=5)
b3.grid(row=6,column=0,padx=10,pady=5)
b4.grid(row=6,column=1,padx=10,pady=5)
b5.grid(row=6,column=2,padx=10,pady=5)
b6.grid(row=7,column=0,padx=10,pady=5)
b7.grid(row=7,column=1,padx=10,pady=5)
b8.grid(row=7,column=2,padx=10,pady=5)
b9.grid(row=8,column=1,padx=10,pady=5)

root.mainloop()
