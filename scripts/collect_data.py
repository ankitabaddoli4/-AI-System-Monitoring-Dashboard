import time
from app.services.monitor_service import get_system_metrics

while True:
    print(get_system_metrics())
    time.sleep(5)
