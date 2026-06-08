import threading
import time

from logger import log_system_data


def monitor_system():

    while True:

        log_system_data()

        time.sleep(10)


def start_monitoring():

    monitor_thread = threading.Thread(
        target=monitor_system,
        daemon=True
    )

    monitor_thread.start()