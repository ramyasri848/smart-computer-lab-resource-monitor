import pandas as pd
from datetime import datetime
import os

from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import (
    getSampleStyleSheet
)


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


def generate_pdf_report():

    try:

        os.makedirs(
            "reports",
            exist_ok=True
        )

        df = pd.read_csv(
            "logs/system_log.csv"
        )

        pdf = SimpleDocTemplate(
            "reports/daily_report.pdf"
        )

        styles = getSampleStyleSheet()

        content = []

        content.append(
            Paragraph(
                "System Monitoring Report",
                styles["Title"]
            )
        )

        content.append(
            Spacer(1, 12)
        )

        content.append(
            Paragraph(
                f"Average CPU Usage: {round(df['CPU Usage'].mean(), 2)}%",
                styles["Normal"]
            )
        )

        content.append(
            Paragraph(
                f"Average RAM Usage: {round(df['RAM Usage'].mean(), 2)}%",
                styles["Normal"]
            )
        )

        content.append(
            Paragraph(
                f"Average Disk Usage: {round(df['Disk Usage'].mean(), 2)}%",
                styles["Normal"]
            )
        )

        content.append(
            Paragraph(
                f"Highest CPU Usage: {round(df['CPU Usage'].max(), 2)}%",
                styles["Normal"]
            )
        )

        content.append(
            Paragraph(
                f"Highest RAM Usage: {round(df['RAM Usage'].max(), 2)}%",
                styles["Normal"]
            )
        )

        content.append(
            Paragraph(
                f"Highest Disk Usage: {round(df['Disk Usage'].max(), 2)}%",
                styles["Normal"]
            )
        )

        pdf.build(content)

        return True

    except:

        return False