import multiprocessing
import time


def calculate_cube(n):
    time.sleep(20)
    return n * n * n


if __name__ == "__main__":
    numbers = [1, 2, 3, 4]
    with multiprocessing.Pool(processes=6) as pool:
        results = pool.map(calculate_cube, numbers)

    for num, res in zip(numbers, results):
        print(f"Cube of {num} is {res}")
