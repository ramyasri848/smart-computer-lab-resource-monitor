import random

def get_lab_statistics():

    total_pcs = 40

    online_pcs = random.randint(32, 40)

    average_cpu = round(
        random.uniform(20, 75),
        2
    )

    average_ram = round(
        random.uniform(30, 80),
        2
    )

    highest_load_machine = (
        f"PC-{random.randint(1,40)}"
    )

    return {
        "total_pcs": total_pcs,
        "online_pcs": online_pcs,
        "average_cpu": average_cpu,
        "average_ram": average_ram,
        "highest_load_machine": highest_load_machine
    }