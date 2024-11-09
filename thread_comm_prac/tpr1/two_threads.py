import threading
import time
import random

cond = threading.Condition()

data = []


def consumer():
    with cond:
        print("consumer waiting")
        cond.wait()
        print("Consumer is notified and resumes")
        for d in data:
            print(f"Got {d}")


def prod():
    with cond:
        for id in range(5):
            data.append(id)
            time.sleep(5)
            print(f"Produces has completed {id}")
        print("Producer is notifying")
        cond.notify()


t1 = threading.Thread(target=consumer)
t2 = threading.Thread(target=prod)

t1.start()
t2.start()

t1.join()
t2.join()
