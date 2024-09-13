import threading
import multiprocessing
import time


# CPU bound task
def sum_of_squares(limit):
    result = 0
    for i in range(limit):
        result += i * i
    return result


# need a wrapper to call the fn in thread
def run_thread_task(limit):
    sum_of_squares(limit)


# diff wrapper to call the fn in process
def run_process_task(limit):
    sum_of_squares(limit)


def test_mul_thread(limit, num_threads):
    # tests threading which is affected by GIL
    threads = []
    start_time = time.time()

    for _ in range(num_threads):
        thread = threading.Thread(target=run_thread_task, args=(limit,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    end_time = time.time()
    print(f"Multi-threading time: {end_time - start_time}")
    # only one thread can execute Python bytecode at a time, so the performance does not
    # scale well with the number of threads for CPU-bound tasks


def test_mul_process(limit, num_process):
    processes = []
    start_time = time.time()

    for _ in range(num_process):
        process = multiprocessing.Process(target=run_process_task, args=(limit,))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

    end_time = time.time()
    print(f"Multi-process time: {end_time - start_time}")
    # process has its own Python interpreter and memory space, so the GIL does not
    # affect multi-processing. CPU-bound tasks can run in parallel on multiple cores


# save as sum_of_squares.pyx

# def sum_of_squares(int limit):
#     cdef int i, result = 0
#     for i in range(limit):
#         result += i * i
#     return result

# # Release the GIL when running the loop
# the def function is made "nogil"
# cpdef int sum_of_squares_nogil(int limit) nogil:
#     cdef int i, result = 0
#     for i in range(limit):
#         result += i * i
#     return result


LIMIT = 10000000

test_mul_thread(LIMIT, 4)
test_mul_process(LIMIT, 4)
