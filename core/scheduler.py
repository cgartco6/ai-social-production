import time

def start_scheduler(task, interval=21600):
    while True:
        task()
        time.sleep(interval)
