from concurrent.futures import ProcessPoolExecutor
from time import sleep


def calculate_square(n):
    sleep(5)
    return n * n


# processes the list of numbers on 4 diff
# cores
if __name__ == "__main__":
    numbers = [1, 2, 4, 7, 10, 78, 95, 86]
    with ProcessPoolExecutor(max_workers=4) as exec:
        # executor maps calculate_square and numbers
        results = exec.map(calculate_square, numbers)

    for number, resl in zip(numbers, results):
        print(f"Square of {number} is {resl}")
