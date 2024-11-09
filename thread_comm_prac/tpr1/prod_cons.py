#!/bin/python

import threading
import time
import queue

buffer = queue.Queue(maxsize=5)


def prd():
    while True:
        item = time.time()
        buffer.put(item)
        print(f"Added {item}")
        time.sleep(1)
        if buffer.full():
            print("Producer halting")
            break


def con():
    while True:
        item = buffer.get()
        print(f"Recd {item}")
        buffer.task_done()
        time.sleep(2)
        if buffer.empty():
            print("Con stop")
            break


producer = threading.Thread(target=prd)
consumer = threading.Thread(target=con)

producer.start()
consumer.start()
