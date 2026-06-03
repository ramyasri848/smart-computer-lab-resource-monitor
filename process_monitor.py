import psutil
import pandas as pd
from datetime import datetime

def get_processes():
    process_list = []

    for process in psutil.process_iter(
        ['pid', 'name', 'cpu_percent', 'memory_percent', 'status', 'create_time']
    ):
        try:
            process_list.append({
                "PID": process.info['pid'],
                "Name": process.info['name'],
                "CPU (%)": process.info['cpu_percent'],
                "Memory (%)": round(process.info['memory_percent'], 2),
                "Status": process.info['status'],
                "Creation Time": datetime.fromtimestamp(
                    process.info['create_time']
                ).strftime("%Y-%m-%d %H:%M:%S")
            })

        except (
            psutil.NoSuchProcess,
            psutil.AccessDenied,
            psutil.ZombieProcess
        ):
            pass

    return pd.DataFrame(process_list)