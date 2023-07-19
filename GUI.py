from tkinter import * #ליסא הכל מהפונקציה
window = Tk()
window.title("My first Gui")#כותרת
window.minsize(width=500, height=300) #שינוי גודל חלון

my_label = Label(text="I am A Label", font=("Ariel", 18, "bold"))
my_label.pack() #להציג בתוך החלון הגרפי
my_label.config(text="New Text")#יצית תוית
def button_clicked():
    print("I got clicked")
    new_text = input.get()
    my_label.config(text=new_text)
button = Button(text="Click me", command=button_clicked)#יצירת כפתור
button.pack()#מיקום הכפתור בחלון

input = Entry(width=20)#יצירת שדה קלט
input.pack()#מיקום שדה הקלט בחלון
def scale_used(a):
    print(a)
scale = Scale(from_=0, to=100, command=scale_used)
scale.pack()

def spinbox():
    print(spinbox)
spinbox = Spinbox(from_=0, to=120, width=5, command=scale_used)
spinbox.pack()
window.mainloop() # יציג לנו את החלון על הצג
print(input.get())