import psutil
import streamlit as st
import time
import pandas as pd


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
            })
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue
    return process_info


st.title("Process Monitor")

# Display process info
processes = get_process_info()
df = pd.DataFrame(processes)

st.subheader("All Running Processes")
if not df.empty:
    selected_process = st.selectbox(
        "Select a process to view details:", df["Name"].unique()
    )

    if selected_process:
        selected_df = df[df["Name"] == selected_process]
        st.write(selected_df)

# Enter process name to search
process_name_input = st.text_input("Enter process name to search:")
if process_name_input:
    filtered_processes = df[df["Name"].str.contains(process_name_input, case=False)]
    st.subheader(f'Search Results for "{process_name_input}"')
    if not filtered_processes.empty:
        st.write(filtered_processes)
    else:
        st.write("No processes found.")

time.sleep(5)
st.rerun()
