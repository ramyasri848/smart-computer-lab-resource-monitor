import psutil
import pandas as pd
from datetime import datetime

def get_processes(search_term=""):
    process_list = []

    for process in psutil.process_iter(
        ['pid', 'name', 'cpu_percent', 'memory_percent', 'status', 'create_time']
    ):
        try:
            process_name = process.info['name'] or ""

            if (
                search_term == ""
                or search_term.lower() in process_name.lower()
            ):
                process_list.append({
                    "PID": process.info['pid'],
                    "Name": process_name,
                    "CPU (%)": process.info['cpu_percent'],
                    "Memory (%)": round(
                        process.info['memory_percent'],
                        2
                    ),
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


def get_process_names():
    names = set()

    for process in psutil.process_iter(['name']):
        try:
            if process.info['name']:
                names.add(process.info['name'])

        except (
            psutil.NoSuchProcess,
            psutil.AccessDenied,
            psutil.ZombieProcess
        ):
            pass

    return sorted(list(names))


def get_top_cpu_processes():
    process_list = []

    for process in psutil.process_iter(
        ['name', 'cpu_percent']
    ):
        try:
            process_list.append({
                "Process": process.info['name'],
                "CPU (%)": process.info['cpu_percent']
            })

        except (
            psutil.NoSuchProcess,
            psutil.AccessDenied,
            psutil.ZombieProcess
        ):
            pass

    df = pd.DataFrame(process_list)

    return df.sort_values(
        by="CPU (%)",
        ascending=False
    ).head(10)


def get_top_memory_processes():
    process_list = []

    for process in psutil.process_iter(
        ['name', 'memory_percent']
    ):
        try:
            process_list.append({
                "Process": process.info['name'],
                "Memory (%)": round(
                    process.info['memory_percent'],
                    2
                )
            })

        except (
            psutil.NoSuchProcess,
            psutil.AccessDenied,
            psutil.ZombieProcess
        ):
            pass

    df = pd.DataFrame(process_list)

    return df.sort_values(
        by="Memory (%)",
        ascending=False
    ).head(10)