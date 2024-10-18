import multiprocessing
import time


def print_numbers():
    for i in range(1, 6):  # its for 1 to 5
        print(f"process {multiprocessing.current_process().name} prints: {i}")
        time.sleep(15)
        # every iteration is executed by all three processes
        # basically three different processes in three cores,
        # runn parallel, with its own parameters


if __name__ == "__main__":
    processes = []
    # 3 processes are starting, in three cores
    for i in range(6):
        # process requires target function and a name,
        p = multiprocessing.Process(target=print_numbers, name=f"Processs-{i + 1}")
        processes.append(p)
        p.start()

    for p in processes:
        p.join()
