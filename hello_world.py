import tkinter as tk

print("Hello World") #Prints in terminal

#Structure for a pop-up window
root = tk.Tk()
root.title("Hello World Pop-up Window")
root.geometry("400x200")
root.configure(bg="black")

#Details of the pop-up window
my_label = tk.Label(
    root,
    text="Hello World!",
    font=("Courier", 30, "bold"),
    bg="black",
    fg="#00FF00" #Neon green
)

my_label.pack(pady=65)
root.mainloop() #IMPORTANT!!! Keeps window visible and waits for user to close window