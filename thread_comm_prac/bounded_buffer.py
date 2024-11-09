import threading
import queue
import time

buffer = queue.Queue(5)


def producer(id):
    while True:
        item = time.time()
        buffer.put(item)
        print(f"Producer {id} produced {item}")
        time.sleep(1)


def consumer(id):
    while True:
        item = buffer.get()
        print(f"Consumer {id} consumed {item}")
        time.sleep(2)


for i in range(3):
    threading.Thread(target=producer, args=(i,)).start()
    threading.Thread(target=consumer, args=(i,)).start()
