import streamlit as st
import psutil
import time


# Helper function to get process details
def get_process_details(process):
    try:
        # Get memory usage in MB
        memory_info = process.memory_info().rss / (1024 * 1024)
        # Get CPU usage in percentage
        cpu_percent = process.cpu_percent(interval=0.1)
        # Get CPU affinity (which processor core is being used)
        cpu_affinity = (
            process.cpu_affinity() if hasattr(process, "cpu_affinity") else "N/A"
        )
        # Get processor number
        cpu_num = process.cpu_num() if hasattr(process, "cpu_num") else "N/A"
        return memory_info, cpu_percent, cpu_affinity, cpu_num
    except (psutil.NoSuchProcess, psutil.AccessDenied):
        return None


# List processes for Python and Rust
def list_python_rust_processes():
    processes = []
    for process in psutil.process_iter(["pid", "name"]):
        try:
            if (
                "python" in process.info["name"].lower()
                or "rust" in process.info["name"].lower()
            ):
                processes.append(process)
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue
    return processes


st.title("Python & Rust Process Monitor")

# Sidebar to select process
st.sidebar.header("Process Selection")
processes = list_python_rust_processes()
process_names = [f"{proc.info['name']} (PID: {proc.info['pid']})" for proc in processes]

if processes:
    selected_process = st.sidebar.selectbox(
        "Select a Python or Rust process", process_names
    )
    selected_process_index = process_names.index(selected_process)
    process = processes[selected_process_index]

    # Show process information
    with st.spinner("Fetching process details..."):
        memory_info, cpu_percent, cpu_affinity, cpu_num = get_process_details(process)
        if memory_info is not None:
            st.subheader(f"Process Details (PID: {process.pid})")
            st.write(f"**Memory Usage:** {memory_info:.2f} MB")
            st.write(f"**CPU Usage:** {cpu_percent}%")
            st.write(f"**Processor Core (CPU Number):** {cpu_num}")
            st.write(f"**CPU Affinity:** {cpu_affinity}")
        else:
            st.error("Unable to fetch details for the selected process.")
else:
    st.warning("No Python or Rust processes found.")

# Auto-refresh every 5 seconds
time.sleep(5)
st.rerun()
