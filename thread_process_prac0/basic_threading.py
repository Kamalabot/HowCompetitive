import threading
import time


def print_numbers():
    for num in range(1, 6):
        print(f"Thread {threading.current_thread().name} prints {num}")
        time.sleep(5)


threads = []

for idx in range(3):
    # three threads start together
    thread = threading.Thread(target=print_numbers, name=f"Thread-{idx + 1}")
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()
