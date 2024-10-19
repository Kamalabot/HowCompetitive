import threading
import queue
import time
import random

q = queue.Queue()


# producer generates number and adds them
def producer():
    for idx in range(10):
        item = random.randint(1, 100)
        print("Producer waiting for consumer to finish")
        q.put(item)
        print(f"Producer added: {item}")
        time.sleep(random.uniform(1, 2))


def consumer():
    while True:
        print("consumer waiting...")
        item = q.get()  # this gets the consumer to wait
        if item is None:
            break

        print(f"Consumer procesed: {item}")
        time.sleep(random.uniform(5, 6))
        q.task_done()


producer_thread = threading.Thread(target=producer)
consumer_thread = threading.Thread(target=consumer)

producer_thread.start()
consumer_thread.start()

producer_thread.join()

q.put(None)
