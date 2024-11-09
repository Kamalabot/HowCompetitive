import threading
import time
import queue

buffer = queue.Queue(maxsize=5)


def producer():
    while True:
        item = time.time()
        buffer.put(item)
        print(f"Produced {item}")
        time.sleep(1)
        if buffer.full():
            print("Producer stopping")
            break


def consumer():
    while True:
        item = buffer.get()
        print(f"Consumed {item}")
        buffer.task_done()
        time.sleep(5)
        if buffer.empty():
            print("consumer stopping")
            break


# Create threads
producer_thread = threading.Thread(target=producer)
consumer_thread = threading.Thread(target=consumer)

# Start threads
producer_thread.start()
consumer_thread.start()
