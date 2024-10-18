import streamlit as st
import pandas as pd
import psutil
from time import sleep


# Function to get process information
def get_process_info():
    process_info = []
    for proc in psutil.process_iter(["pid", "name", "cpu_percent", "memory_info"]):
        try:
            process_info.append({
                "PID": proc.info["pid"],
                "Name": proc.info["name"],
                "CPU (%)": proc.info["cpu_percent"],
                "Memory (MB)": proc.info["memory_info"].rss
                / (1024 * 1024),  # Convert bytes to MB
                "CPU Core": proc.cpu_num(),
                "Threads": proc.num_threads(),  # Add number of threads
            })
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue
    return process_info


# Streamlit app
st.title("Process Monitor")

# Get process information
process_info = get_process_info()

# Convert to DataFrame for display
df = pd.DataFrame(process_info)

# Display process details
st.dataframe(df)

# Allow user to select a process by name
process_name = st.selectbox("Select Process by Name", df["Name"].unique())

# Filter and display details of the selected process
if process_name:
    selected_process = df[df["Name"] == process_name]
    st.write("Details of selected process:")
    st.write(selected_process)

# Option to refresh data
if st.button("Refresh"):
    process_info = get_process_info()
    df = pd.DataFrame(process_info)
    st.dataframe(df)

# sleep(5)
# st.rerun()
