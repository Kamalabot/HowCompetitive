import threading

counter = 0
lock = threading.Lock()


def increase_count():
    # make the counter global and
    # access it here
    global counter
    for _ in range(10000):
        with lock:
            counter += 1


threads = []

for idx in range(5):
    thread = threading.Thread(target=increase_count, name=f"Increase by {idx}")
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print(f"Final counter: {counter}")
