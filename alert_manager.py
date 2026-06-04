import psutil

def get_alerts():

    alerts = []

    cpu = psutil.cpu_percent()

    ram = psutil.virtual_memory().percent

    disk = psutil.disk_usage('/').percent

    if cpu > 90:
        alerts.append(
            f"⚠ High CPU Usage: {cpu}%"
        )

    if ram > 85:
        alerts.append(
            f"⚠ Memory Critical: {ram}%"
        )

    if disk > 90:
        alerts.append(
            f"⚠ Disk Nearly Full: {disk}%"
        )

    return alerts