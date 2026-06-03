import streamlit as st
from cpu_monitor import get_cpu_info

st.set_page_config(
    page_title="Smart Computer Lab Resource Monitoring & Analytics System",
    layout="wide"
)

st.title("Smart Computer Lab Resource Monitoring & Analytics System")

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

if menu == "Dashboard":
    st.header("Dashboard")
    st.write("Welcome to the Smart Computer Lab Resource Monitoring & Analytics System")

elif menu == "CPU Monitor":
    st.header("CPU Monitor")

    cpu_info = get_cpu_info()

    col1, col2 = st.columns(2)

    with col1:
        st.metric("CPU Usage (%)", f"{cpu_info['cpu_usage']}%")
        st.metric("Physical Cores", cpu_info["physical_cores"])

    with col2:
        st.metric("Logical Cores", cpu_info["logical_cores"])
        st.metric("CPU Frequency (GHz)", cpu_info["frequency"])

elif menu == "Memory Monitor":
    st.header("Memory Monitor")

elif menu == "Disk Monitor":
    st.header("Disk Monitor")

elif menu == "Process Monitor":
    st.header("Process Monitor")

elif menu == "Network Monitor":
    st.header("Network Monitor")

elif menu == "Analytics":
    st.header("Analytics")

elif menu == "Reports":
    st.header("Reports")