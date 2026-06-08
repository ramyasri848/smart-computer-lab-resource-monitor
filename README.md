# Smart Computer Lab Resource Monitoring & Analytics System

## Overview

The Smart Computer Lab Resource Monitoring & Analytics System is a Python-based Operating Systems project that monitors and analyzes system resources in real time. The application provides an interactive dashboard for tracking CPU, memory, disk, and process information while generating reports and analytics from collected system data.

## Features

### CPU Monitoring

* Real-time CPU usage monitoring
* Physical and logical core information
* CPU frequency details

### Memory Monitoring

* Total RAM information
* Used RAM information
* Available RAM information
* Swap memory statistics

### Disk Monitoring

* Total storage information
* Used storage information
* Free storage information
* Individual drive details

### Process Monitoring

* Running process information
* Process search functionality
* Top CPU-consuming processes
* Top memory-consuming processes

### System Health Monitoring

* Health score calculation
* System status display
* Resource utilization alerts

### Analytics Dashboard

* Average CPU usage analysis
* Average RAM usage analysis
* Average Disk usage analysis
* Highest CPU usage analysis
* Highest RAM usage analysis
* Highest Disk usage analysis

### Live Graphs

* CPU usage trend visualization
* RAM usage trend visualization
* Disk usage trend visualization

### Report Generation

* CSV report generation
* PDF report generation
* Report download functionality

### Background Monitoring

* Automatic system data logging
* Multithreaded monitoring

## Technologies Used

* Python
* Streamlit
* Psutil
* Pandas
* Plotly
* ReportLab
* Threading

## Project Structure

smart-computer-lab-resource-monitor/

* app.py
* cpu_monitor.py
* memory_monitor.py
* disk_monitor.py
* process_monitor.py
* health_score.py
* alert_manager.py
* logger.py
* analytics.py
* report_generator.py
* background_monitor.py
* requirements.txt
* logs/
* reports/
* assets/

## Installation

1. Clone the repository

git clone https://github.com/ramyasri848/smart-computer-lab-resource-monitor.git

2. Install dependencies

pip install -r requirements.txt

3. Run the application

streamlit run app.py

## Operating System Concepts Used

* Process Management
* Resource Monitoring
* Multithreading
* System Calls
* Memory Management
* CPU Scheduling Observation

## Future Enhancements

* Network Monitoring Module
* Email Alert System
* Multi-System Monitoring
* Database Integration
* Cloud Deployment
* User Authentication

## Author

Ramyasri Kurakula

BTECH CSE

BIT Mesra
