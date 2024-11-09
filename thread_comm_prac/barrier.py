import threading
import time


def task(barrier, id):
    print(f"Thread {id} is waiting at the barrier")
    time.sleep(1)
    barrier.wait()
    print(f"Thread {id} passed the barrier")


barrier = threading.Barrier(3)
threads = [threading.Thread(target=task, args=(barrier, i)) for i in range(3)]
for thread in threads:
    thread.start()
