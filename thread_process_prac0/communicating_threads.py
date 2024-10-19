import threading
import time
import random

# why buffer? Will find out
buffer = []
buffer_lock = threading.Lock()  # mutex to protect race
# there are two variables competing for lock
buffer_not_empty = threading.Condition(buffer_lock)
buffer_not_full = threading.Condition(buffer_lock)
buffer_size = 5

# Producer thread: produces items and adds to buffer


def producer():
    for _ in range(10):
        item = random.randint(1, 100)
        with buffer_not_full:  # Acquire lock and wait
            # here we know if the buffer is full or not
            while len(buffer) >= buffer_size:
                buffer_not_full.wait()  # wait until space in buffer
            buffer.append(item)
            # notify only after exceeding 4 elments
            if len(buffer) > 4:
                print(f"Producer reached: {len(buffer)} elments")
                buffer_not_empty.notify()
        time.sleep(random.uniform(0.1, 0.3))


def consumer():
    for _ in range(10):
        with buffer_not_empty:
            while not buffer:
                buffer_not_empty.wait()
            item = buffer.pop()
            print(f"Consumer process: {item}")
            if len(buffer) < 2:
                buffer_not_full.notify()
        time.sleep(random.uniform(0.1, 0.2))


produce_thread = threading.Thread(target=producer)
consume_thread = threading.Thread(target=consumer)

produce_thread.start()
consume_thread.start()

produce_thread.join()
produce_thread.join()

print("All tasks completed")
