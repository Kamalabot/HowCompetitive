import time
import heapq
from collections import deque

# Manage multiple tasks without real threading


class Task:
    def __init__(self, coro) -> None:
        self.coro = coro

    def run(self):
        return next(self.coro)


class EventLoop:
    def __init__(self) -> None:
        # declaring the queue and list
        self.tasks = deque()
        self.timers = []

    def create_task(self, coro):
        # simple task is wrapped to be run
        task = Task(coro)
        self.tasks.append(task)

    def call_later(self, delay, coro):
        run_time = time.time() + delay
        heapq.heappush(
            self.timers,
            (
                run_time,
                Task(coro),
            ),
        )

    def run_forever(self):
        while self.tasks or self.timers:
            if self.tasks:
                task = self.tasks.popleft()
                try:
                    task.run()
                    self.tasks.append(task)
                except StopIteration:
                    pass
            # handle timed tasks
            now = time.time()
            while self.timers and self.timers[0][0] <= now:
                _, task = heapq.heappop(self.timers)
                try:
                    task.run()
                except StopIteration:
                    pass
            time.sleep(0.01)


def simple():
    print("Simple task started")
    yield
    print("Simple task ended")


def delay():
    print("Starting delay tasks")
    yield
    print("Delay task is done")


# create the eventloop object
loop = EventLoop()
# the tasks are called as objects
ts1 = simple()
ts2 = delay()
# calls are pushed into the event loop
loop.create_task(ts1)  # this goes into self.tasks
loop.call_later(2, ts2)  # this into self.timers
# loop is started
loop.run_forever()
