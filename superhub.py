import os
import time
import threading
from datetime import datetime
import win32api
import win32con

class SuperHub:
    def __init__(self):
        self.tasks = []

    def add_task(self, name, schedule_time, command):
        task = {
            'name': name,
            'schedule_time': schedule_time,
            'command': command,
            'last_run': None
        }
        self.tasks.append(task)
        print(f"Task '{name}' added to schedule.")

    def run_task(self, task):
        current_time = datetime.now().strftime("%H:%M")
        if current_time == task['schedule_time'] and task['last_run'] != current_time:
            print(f"Running task: {task['name']}")
            os.system(task['command'])
            task['last_run'] = current_time
            print(f"Task '{task['name']}' completed.")

    def start_scheduler(self):
        print("Starting SuperHub Scheduler...")
        while True:
            for task in self.tasks:
                self.run_task(task)
            time.sleep(60)

def set_system_time(hour, minute):
    day = datetime.now().day
    month = datetime.now().month
    year = datetime.now().year
    second = 0
    weekday = 0
    millisec = 0
    win32api.SetSystemTime(year, month, weekday, day, hour, minute, second, millisec)
    print(f"System time set to {hour}:{minute}.")

if __name__ == "__main__":
    superhub = SuperHub()
    superhub.add_task("Example Task", "14:30", "echo Hello, this is a scheduled task!")
    
    # Run the scheduler in a separate thread
    scheduler_thread = threading.Thread(target=superhub.start_scheduler)
    scheduler_thread.daemon = True
    scheduler_thread.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("Scheduler stopped.")