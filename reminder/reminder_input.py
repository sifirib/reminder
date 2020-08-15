import time
import os
import sys
from tkinter import *
import subprocess



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
    
    
    
    OTHER_SCRIPT_NAME = "reminder.py"

    process_outputs = subprocess.getoutput("ps aux | grep " + OTHER_SCRIPT_NAME) # Searching for the process running 2.py
    wanted_process_info = process_outputs.split("\n")[0] # Getting the first line only
    splitted_process_info = wanted_process_info.split(" ") # Splitting the string
    splitted_process_info = [x for x in splitted_process_info if x != ''] # Removing empty items
    pid = splitted_process_info[1] # PID is the secend item in the ps output
    os.system("kill -HUP " + str (pid)) # Killing the other process
    print(str(pid))
    

    exit()

    time.sleep(1000) # Will not be called because exit() was called before   
    
    
    

    
    
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




