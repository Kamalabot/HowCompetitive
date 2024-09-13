import threading
import time
from concurrent.futures import ThreadPoolExecutor

start = time.time()
data = list(range(1000))
result = []

lock = threading.Lock()

threads = []


def compute_threads(num):
    squared = num * num
    with lock:
        result.append(squared)


for num in data:
    thread = threading.Thread(target=compute_threads, args=(num,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print(f"Pdata: {result[:5]}")
end = time.time()
print(f"Time elapsed plain threading: {(end - start) * 1000}ms")

start_np = time.time()

np_data = list(map(lambda x: x * x, data))

print(f"Non Parallel no threading: {np_data[:5]}")

end_np = time.time()
print(f"Time elapsed: {(end_np - start_np) * 1000}ms")

result = []

start_np = time.time()
with ThreadPoolExecutor(max_workers=5) as executor:
    futures = executor.map(lambda x: x * x, data)
    result.extend(futures)

print(f"Concurrent result: {result[:5]}")
end_np = time.time()
print(f"Time elapsed for concurrent : {(end_np - start_np) * 1000}ms")
