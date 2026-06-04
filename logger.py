import os
import pandas as pd
from datetime import datetime
import psutil

from health_score import calculate_health_score


def log_system_data():

    os.makedirs("logs", exist_ok=True)

    log_file = "logs/system_log.csv"

    cpu = psutil.cpu_percent()

    ram = psutil.virtual_memory().percent

    disk = psutil.disk_usage('/').percent

    health = calculate_health_score()

    new_data = {
        "Date": [datetime.now().strftime("%Y-%m-%d")],
        "Time": [datetime.now().strftime("%H:%M:%S")],
        "CPU Usage": [cpu],
        "RAM Usage": [ram],
        "Disk Usage": [disk],
        "Health Score": [health["score"]]
    }

    new_df = pd.DataFrame(new_data)

    if os.path.exists(log_file):

        old_df = pd.read_csv(log_file)

        updated_df = pd.concat(
            [old_df, new_df],
            ignore_index=True
        )

        updated_df.to_csv(
            log_file,
            index=False
        )

    else:

        new_df.to_csv(
            log_file,
            index=False
        )