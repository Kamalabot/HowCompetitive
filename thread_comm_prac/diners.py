import threading
import time


class Philosopher(threading.Thread):
    def __init__(self, name, left_fork, right_fork):
        super().__init__()
        self.name = name
        self.left_fork = left_fork
        self.right_fork = right_fork

    def run(self):
        while True:
            with self.left_fork, self.right_fork:
                # print(self.left_fork.locked())
                # print(f"{self.name} is eating.")
                time.sleep(1)
            print(f"{self.name} is thinking.")
            time.sleep(1)


forks = [threading.Lock() for _ in range(5)]
philosophers = [
    Philosopher(f"Philosopher {i}", forks[i], forks[(i + 1) % 5]) for i in range(5)
]

for philosopher in philosophers:
    philosopher.start()
