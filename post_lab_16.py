# experiment no : 1;
# •	Design Counter App (This app has a button that increments a counter displayed on the screen every time the button is clicked)

from tkinter import *
count = 0

def increase():
    global count
    count += 1
    label.config(text=str(count))

root = Tk()
root.title("Counter")
root.geometry("200x150")

label = Label(root, text="0", font=("Arial", 30))
label.pack(pady=20)

btn = Button(root, text="Click Me", command=increase)
btn.pack()

root.mainloop()


# ------------------------------------------------------------------------------------------------------------

# experiment no : 2;
# Text Input App (This app allows users to type in a text field and display the typed text on the screen when a button is pressed.)

# from tkinter import *

# # Function to show text when button is clicked
# def show_text():
#     user_input = entry.get()            
#     output_label.config(text=user_input) 

# root = Tk()
# root.title("Text Input App")
# root.geometry("300x200")

# entry = Entry(root, font=("Arial", 14))
# entry.pack(pady=10)

# button = Button(root, text="Show Text", command=show_text)
# button.pack(pady=5)

# output_label = Label(root, text="", font=("Arial", 14), fg="blue")
# output_label.pack(pady=10)

# root.mainloop()
