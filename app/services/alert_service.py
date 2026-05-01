from app.services.monitor_service import get_system_metrics
from app.config import Config
from app.utils.email_sender import send_email_alert

last_alert_sent = False

def check_alert():
    global last_alert_sent

    data = get_system_metrics()
    cpu = data["cpu"]

    if cpu > Config.ALERT_THRESHOLD:
        if not last_alert_sent:
            send_email_alert(f"⚠️ High CPU Usage: {cpu}%")
            last_alert_sent = True
        return {"alert": "⚠️ High CPU! Email Sent"}
    else:
        last_alert_sent = False
        return {"alert": "✅ System Normal"}
