import psutil

def get_cpu_info():
    cpu_freq = psutil.cpu_freq()

    return {
        "cpu_usage": psutil.cpu_percent(interval=1),
        "physical_cores": psutil.cpu_count(logical=False),
        "logical_cores": psutil.cpu_count(logical=True),
        "frequency": round(cpu_freq.current / 1000, 2)
    }