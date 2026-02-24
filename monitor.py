import psutil
import time
from datetime import datetime
from config import CPU_WARN, RAM_WARN, INTERVAL

def monitor_system():
    print("Starting System Health Monitor...\n")

    while True:
        cpu = psutil.cpu_percent(interval=1)
        ram = psutil.virtual_memory().percent
        disk = psutil.disk_usage('/').percent
        battery = psutil.sensors_battery()
        battery_percent = battery.percent if battery else "Not Available"

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        status_line = (
            f"[{timestamp}] CPU: {cpu}% | "
            f"RAM: {ram}% | "
            f"Disk: {disk}% | "
            f"Battery: {battery_percent}"
        )

        print(status_line)

        # Warnings
        if cpu > CPU_WARN:
            print("⚠ WARNING: High CPU Usage")

        if ram > RAM_WARN:
            print("⚠ WARNING: High RAM Usage")

        # Log to file
        with open("logs/system.log", "a") as f:
            f.write(status_line + "\n")

        time.sleep(INTERVAL)
