import time
import os
import sys
from tkinter import *


path = "/home/hrx/Desktop/reminder/tasks"
path2 = "/home/hrx/Desktop/reminder/reminder.py"

write_file = open(rf"{path}", "a+")

def addTask():
    print(new_task_input.get(), time_of_task_input.get())
    write_file.write(f"{new_task_input.get()}-{time_of_task_input.get()}\n")
    write_file.close()
    root.destroy()

    popup = Tk()
    
    last_text = Label(popup, text = "Task is added\nWill let you know :)")
    last_text.grid()
    popup = mainloop()
    
    
    os.system(f"pkill -f {path2}")
    os.system(f"python {path2}")
    
    # sys.exit("Task is added, will let you know.")


root = Tk()

new_task = Label(root, text = "New Task: ")
new_task_input = Entry(root)

time_of_task = Label(root, text = "Scheduled Time: ")
time_of_task_input = Entry(root)

addButton = Button(root, text = "Add task", command = addTask )


new_task.grid()
new_task_input.grid()

time_of_task.grid()
time_of_task_input.grid()

addButton.grid()

root = mainloop()




