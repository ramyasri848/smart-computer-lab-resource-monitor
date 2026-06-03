import psutil

def get_memory_info():
    memory = psutil.virtual_memory()
    swap = psutil.swap_memory()

    return {
        "total_ram": round(memory.total / (1024 ** 3), 2),
        "used_ram": round(memory.used / (1024 ** 3), 2),
        "available_ram": round(memory.available / (1024 ** 3), 2),
        "ram_usage": memory.percent,
        "swap_total": round(swap.total / (1024 ** 3), 2),
        "swap_used": round(swap.used / (1024 ** 3), 2)
    }