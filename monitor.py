import psutil
from datetime import datetime
import time
import os

if not os.path.exists("logs"):
    os.makedirs("logs")

LOG_FILE = "logs/system.log"

def monitor_system():
    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory()
    disk = psutil.disk_usage('/')

    log = f"""
==============================
SYSTEM MONITOR
Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

CPU Usage: {cpu}%
Memory Usage: {memory.percent}%
Disk Usage: {disk.percent}%
==============================
"""

    print(log)

    with open(LOG_FILE, "a") as file:
        file.write(log)

while True:
    monitor_system()
    time.sleep(5)