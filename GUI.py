from tkinter import *

def button_clicked():
    username = username_entry.get()
    age = age_entry.get()
    print(f"Username: {username}, Age: {age}")

window = Tk()
window.title("User Input")
window.minsize(width=500, height=300)

# Create username label and input field
username_label = Label(text="Username", font=("Ariel", 18, "bold"))
username_label.pack()
username_entry = Entry(width=20)
username_entry.pack()

# Create age label and input field
age_label = Label(text="Age", font=("Ariel", 18, "bold"))
age_label.pack()
age_entry = Entry(width=20)
age_entry.pack()

# Create submit button
submit_button = Button(text="Submit", command=button_clicked)
submit_button.pack()

window.mainloop()
