import psutil

def get_disk_info():
    total = 0
    used = 0
    free = 0

    for partition in psutil.disk_partitions():
        try:
            usage = psutil.disk_usage(partition.mountpoint)

            total += usage.total
            used += usage.used
            free += usage.free

        except PermissionError:
            continue

    percent = round((used / total) * 100, 2)

    return {
        "total": round(total / (1024 ** 3), 2),
        "used": round(used / (1024 ** 3), 2),
        "free": round(free / (1024 ** 3), 2),
        "percent": percent
    }


def get_drive_info():
    drives = []

    for partition in psutil.disk_partitions():
        try:
            usage = psutil.disk_usage(partition.mountpoint)

            drives.append({
                "drive": partition.device,
                "total": round(usage.total / (1024 ** 3), 2),
                "used": round(usage.used / (1024 ** 3), 2),
                "free": round(usage.free / (1024 ** 3), 2),
                "percent": usage.percent
            })

        except PermissionError:
            continue

    return drives