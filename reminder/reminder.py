import os
import schedule
from datetime import datetime
import sys
# import psutil

path = "/home/hrx/Desktop/reminder/tasks"

os.system(f'notify-send "Welcome to Hawaii"')

# def checkIfProcessRunning(processName):
  
#     for proc in psutil.process_iter():
#         try:
#             if processName.lower() in proc.name().lower():
#                 return True
#         except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
#             pass
#     return False


read_file = open(rf"{path}","r")
tasks = []


for task in read_file.readlines():
    data_task, data_date = task.split("-")
    tasks.append([data_task, data_date[:-1]])
    

print("Tasks: \n",tasks)
read_file.close()


tasknumber = 0        

while True:
    
    now = datetime.now()
    current_time = now.strftime("%H:%M")
    nearest_time = 10000

    for i in range(0,len(tasks)):
        aux_hour,aux_minute = tasks[i][1].split(":")
        aux_time = int(aux_hour)*60 + int(aux_minute)
        
        current_hour,current_minute = current_time.split(":")
        int_current_time = int(current_hour)*60 + int(current_minute)
        
        if  ((aux_time - int_current_time) < nearest_time) and (aux_time > int_current_time + 0.5):
            nearest_time = aux_time- int_current_time
            k = i
            
        if (i == len(tasks) - 1):
            time_for_schedule = tasks[k][1]
            text_for_not = tasks[k][0]
            break
   
    def do_notification():
        os.system(f'notify-send "{text_for_not}"')
    
    
    schedule.every().day.at(f"{time_for_schedule}").do(do_notification)
    
    tasknumber += 1

    while 1:
        schedule.run_pending()
        
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        if current_time == f"{time_for_schedule}:05":
            # print("yes")
            if tasknumber == len(tasks):
                sys.exit("\nAll tasks were notificationed, bye for today <:")
            break
        
        # else:
             # print("no")
