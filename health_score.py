import psutil

def calculate_health_score():

    cpu = psutil.cpu_percent()

    ram = psutil.virtual_memory().percent

    disk = psutil.disk_usage('/').percent

    score = 100

    score -= cpu * 0.2
    score -= ram * 0.2
    score -= disk * 0.1

    score = max(0, round(score))

    if score >= 80:
        status = "Healthy"

    elif score >= 60:
        status = "Moderate"

    else:
        status = "Critical"

    return {
        "score": score,
        "status": status
    }