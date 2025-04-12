# scheduler.py
from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime
import pytz
from dateutil import parser

class Scheduler:
    def __init__(self):
        self.scheduler = BackgroundScheduler()
        self.scheduler.start()
        self.tasks = []
        
    def schedule_task(self, time, task, callback=None):
        try:
            # Parse the time
            task_time = parser.parse(time)
            
            # Schedule the task
            job = self.scheduler.add_job(
                self._execute_task,
                'date',
                run_date=task_time,
                args=[task, callback]
            )
            
            # Store task info
            task_id = job.id
            self.tasks.append({
                "id": task_id,
                "time": task_time,
                "task": task
            })
            
            return {
                "success": True, 
                "message": f"Task scheduled for {task_time.strftime('%H:%M:%S on %Y-%m-%d')}",
                "task_id": task_id
            }
            
        except Exception as e:
            return {"success": False, "message": str(e)}
    
    def _execute_task(self, task, callback=None):
        # Execute the task (in MVP, just print and notify)
        print(f"Executing task: {task}")
        
        # If callback provided, call it
        if callback:
            callback(task)