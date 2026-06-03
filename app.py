import streamlit as st

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

st.header(menu)

if menu == "Dashboard":
    st.write("Welcome to the Smart Computer Lab Resource Monitoring & Analytics System")

elif menu == "CPU Monitor":
    st.write("CPU Monitoring Module")

elif menu == "Memory Monitor":
    st.write("Memory Monitoring Module")

elif menu == "Disk Monitor":
    st.write("Disk Monitoring Module")

elif menu == "Process Monitor":
    st.write("Process Monitoring Module")

elif menu == "Network Monitor":
    st.write("Network Monitoring Module")

elif menu == "Analytics":
    st.write("Analytics Dashboard")

elif menu == "Reports":
    st.write("Reports Section")