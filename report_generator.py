import pandas as pd
from datetime import datetime
import os


def generate_report():

    try:

        os.makedirs(
            "reports",
            exist_ok=True
        )

        df = pd.read_csv(
            "logs/system_log.csv"
        )

        report = {
            "Report Date": [
                datetime.now().strftime(
                    "%Y-%m-%d"
                )
            ],

            "Average CPU Usage": [
                round(
                    df["CPU Usage"].mean(),
                    2
                )
            ],

            "Average RAM Usage": [
                round(
                    df["RAM Usage"].mean(),
                    2
                )
            ],

            "Average Disk Usage": [
                round(
                    df["Disk Usage"].mean(),
                    2
                )
            ],

            "Highest CPU Usage": [
                round(
                    df["CPU Usage"].max(),
                    2
                )
            ],

            "Highest RAM Usage": [
                round(
                    df["RAM Usage"].max(),
                    2
                )
            ],

            "Highest Disk Usage": [
                round(
                    df["Disk Usage"].max(),
                    2
                )
            ]
        }

        report_df = pd.DataFrame(
            report
        )

        report_df.to_csv(
            "reports/daily_report.csv",
            index=False
        )

        return True

    except:

        return False