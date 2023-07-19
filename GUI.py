from tkinter import * #ליסא הכל מהפונקציה
def button_clicked():
    user_name = username_entry.get()
    age = age_entry.get()
    textinfo = text.get("1.0", "end-1c")
    print(f"User Name : {user_name}\n Age : {age}")
    print(f"text info {textinfo}")


window = Tk()
window.title("User Details")#כותרת
window.minsize(width=500, height=300) #שינוי גודל חלון


my_label = Label(text="Enter user name", font=("Ariel", 18, "bold"))
my_label.pack() #להציג בתוך החלון הגרפי
username_entry = Entry()
username_entry.pack()

age_label = Label(text="Enter user Age", font=("Ariel", 18, "bold"))
age_label.pack() #להציג בתוך החלון הגרפי

age_entry = Entry()
age_entry.pack()

button = Button(text="Submit", command=button_clicked)#יצירת כפתור
button.pack()#מיקום הכפתור בחלון

text = Text(height=5, width=20)
text.focus()
text.pack()

window.mainloop() # יציג לנו את החלון על הצג
button_clicked()