import multiprocessing
import numpy as np
import time

# row multiplication function


def multiply_row(row_idx, A, B, result):
    result[row_idx] = np.dot(A[row_idx], B)


if __name__ == "__main__":
    size = 1000

    # create large matrices A and B
    A = np.random.rand(size, size)
    B = np.random.rand(size, size)
    result = np.zeros((size, size))

    # initiate the the pool
    pool = multiprocessing.Pool(processes=multiprocessing.cpu_count())
    start_time = time.time()

    # Distribute each row multiplication as a separate task
    for idx in range(size):
        pool.apply_async(multiply_row, args=(idx, A, B, result))

    # Close the pool and wait
    pool.close()
    pool.join()

    end_time = time.time()

    print(f"Matrix multiplication completion: {end_time - start_time}")
    print(f"Result matrix shape: {result.shape}")
