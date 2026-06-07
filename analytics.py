import pandas as pd

def get_analytics():

    try:

        df = pd.read_csv("logs/system_log.csv")

        analytics = {
            "avg_cpu": round(df["CPU Usage"].mean(), 2),
            "avg_ram": round(df["RAM Usage"].mean(), 2),
            "avg_disk": round(df["Disk Usage"].mean(), 2),
            "max_cpu": round(df["CPU Usage"].max(), 2),
            "max_ram": round(df["RAM Usage"].max(), 2),
            "max_disk": round(df["Disk Usage"].max(), 2)
        }

        return analytics

    except:
        return None