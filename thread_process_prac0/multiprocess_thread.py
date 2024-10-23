import threading
import time
from multiprocessing import Process, Queue


def thread_task(thread_id, pid, task_queue):
    # there is the task_queue with takes the result
    time.sleep(1)
    result = f"process {pid} with {thread_id} finished"
    task_queue.put(result)


def process_task(process_id, task_queue):
    # here also the task_queue follows
    threads = []
    for idx in range(4):
        # initiate a thread with functions
        t = threading.Thread(
            target=thread_task,
            args=(f"thread_{idx}", process_id, task_queue),
        )
        # start the thread and append it
        t.start()
        threads.append(t)

    for tdx in threads:
        # join the threads and wait for it
        # to complete
        tdx.join()


# Need to provide an input from the process 1
# that needs to be updated in process two, and then
# output to be printed...

if __name__ == "__main__":
    result_queue = Queue()

    processes = []
    ptemp = 8
    for pdx in range(2):

        # start individual processes
        p = Process(target=process_task, args=(pdx, result_queue))
        # start the processes

        p.start()
        processes.append(p)

    for p in processes:
        # join the process
        p.join()
    print("Here all the threads have completed...")
    while not result_queue.empty():
        # what is the result_queue.get()
        print(result_queue.get())
