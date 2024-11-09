import threading
import time


def work_print(tid: int):
    for x in range(5):
        print(f"Number is {x} in thread {tid}")
        time.sleep(2)


if __name__ == "__main__":
    thread_pool = []
    for tid in range(5):
        t_n = threading.Thread(
            target=work_print,
            args=[
                tid,
            ],
        )
        time.sleep(2)
        thread_pool.append(t_n)
        t_n.start()

    for th in thread_pool:
        th.join()
