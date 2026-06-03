import streamlit as st
from cpu_monitor import get_cpu_info
from memory_monitor import get_memory_info
from disk_monitor import get_disk_info, get_drive_info
from process_monitor import get_processes, get_process_names

# Page Configuration
st.set_page_config(
    page_title="Smart Computer Lab Resource Monitoring & Analytics System",
    layout="wide"
)

# Title
st.title("Smart Computer Lab Resource Monitoring & Analytics System")

# Sidebar Navigation
st.sidebar.title("Navigation")

menu = st.sidebar.radio(
    "Select Module",
    [
        "Dashboard",
        "CPU Monitor",
        "Memory Monitor",
        "Disk Monitor",
        "Process Monitor",
        "Network Monitor",
        "Analytics",
        "Reports"
    ]
)

# Dashboard
if menu == "Dashboard":
    st.header("Dashboard")
    st.write(
        "Welcome to the Smart Computer Lab Resource Monitoring & Analytics System"
    )

# CPU Monitor
elif menu == "CPU Monitor":
    st.header("CPU Monitor")

    cpu_info = get_cpu_info()

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "CPU Usage (%)",
            f"{cpu_info['cpu_usage']}%"
        )

        st.metric(
            "Physical Cores",
            cpu_info["physical_cores"]
        )

    with col2:
        st.metric(
            "Logical Cores",
            cpu_info["logical_cores"]
        )

        st.metric(
            "CPU Frequency (GHz)",
            cpu_info["frequency"]
        )

# Memory Monitor
elif menu == "Memory Monitor":
    st.header("Memory Monitor")

    memory = get_memory_info()

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "Total RAM (GB)",
            memory["total_ram"]
        )

        st.metric(
            "Used RAM (GB)",
            memory["used_ram"]
        )

        st.metric(
            "RAM Usage (%)",
            f"{memory['ram_usage']}%"
        )

    with col2:
        st.metric(
            "Available RAM (GB)",
            memory["available_ram"]
        )

        st.metric(
            "Swap Total (GB)",
            memory["swap_total"]
        )

        st.metric(
            "Swap Used (GB)",
            memory["swap_used"]
        )

# Disk Monitor
elif menu == "Disk Monitor":
    st.header("Disk Monitor")

    disk = get_disk_info()

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "Total Storage (GB)",
            disk["total"]
        )

        st.metric(
            "Used Storage (GB)",
            disk["used"]
        )

    with col2:
        st.metric(
            "Free Storage (GB)",
            disk["free"]
        )

        st.metric(
            "Disk Usage (%)",
            f"{disk['percent']}%"
        )

    st.subheader("Drive Information")

    drives = get_drive_info()

    for drive in drives:
        st.write(f"### {drive['drive']}")
        st.write(f"Total: {drive['total']} GB")
        st.write(f"Used: {drive['used']} GB")
        st.write(f"Free: {drive['free']} GB")
        st.write(f"Usage: {drive['percent']}%")


# Process Monitor
elif menu == "Process Monitor":
    st.header("Process Monitor")

    process_names = get_process_names()

    selected_process = st.selectbox(
        "Search Process",
        options=[""] + process_names
    )

    processes = get_processes(selected_process)

    st.subheader("Running Processes")

    st.dataframe(
    processes,
    width="stretch"
)

    st.success(
        f"Total Processes Found: {len(processes)}"
    )

# Network Monitor
elif menu == "Network Monitor":
    st.header("Network Monitor")
    st.info("Network Monitoring Module Coming Soon")

# Analytics
elif menu == "Analytics":
    st.header("Analytics")
    st.info("Analytics Dashboard Coming Soon")

# Reports
elif menu == "Reports":
    st.header("Reports")
    st.info("Reports Module Coming Soon")