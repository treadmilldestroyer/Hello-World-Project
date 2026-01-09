import tkinter as tk

print("Hello World")

root = tk.Tk()
root.title("Retro Hello World")
root.geometry("400x400")
root.configure(bg="black")

my_label = tk.Label(
    root,
    text="Hello World!",
    font=("Courier", 30),
    bg="black",
    fg="#00FF00"
)

my_label.pack(pady=100)
root.mainloop()