import time
from app.services.monitor_service import get_system_metrics

def start_scheduler():
    while True:
        print("Collecting metrics:", get_system_metrics())
        time.sleep(5)