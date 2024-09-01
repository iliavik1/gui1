import tkinter as tk

root = tk.Tk()

root.geometry("1000x500")
root.title("hi")
label = tk.Label(root, text="hi this is my first program on python", font=('Arial', 18))
label.pack(padx=30, pady=30)
label1 = tk.Label(root, text="this is made for github by iliavik1", font=('Arial', 20))
label1.pack(padx=30, pady=30)
button = tk.Button(root, text="button", font=('Arial', 15))
button.pack(padx=30, pady=30)
button.place(x=400, y=200, height=100, width=200)
label1.place(x=400, y=400, height=100, width=400)

root.mainloop()



print("hi")