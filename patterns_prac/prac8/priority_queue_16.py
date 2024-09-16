import heapq

# contains the code for task management

# intuition1: use two seperate stores, maintaining priority and storing tasks
# intuition2: create the priority by adding the urgency and importance
# intuition3: push the tasks with priority int the heapq
# intuition4: poping the task from priority and deleting from tasks store
# intuition5: updating the tasks will call for re-push into heapq, and
# removing earlier taskid from tasks store
from heapq import (
    heappush,
    heappop,
)


class Taskmanager:
    def __init__(self):
        self.task_heap = []
        self.task_map = {}

    def add(self, imp, urg, tid):
        # the heapq is min_heap, so need
        # to make the priority negative to
        # get the max to the top
        prio = -(imp + urg)
        heappush(
            self.task_heap,
            (
                prio,
                imp,
                urg,
                tid,
            ),
        )
        self.task_map[tid] = (prio, imp, urg)

    def print_tasks(self):
        for tid, tsk in self.task_map.items():
            print(f"tid: {tid} | urg: {tsk[2]} | imp: {tsk[1]}")
        print("The actual tasks in the heap")
        for elm in self.task_heap:
            print(f"Task Data: {elm}")

    def get_task(self):
        # will pop the top most task from the heap
        # and remove it from the task_map also
        task = heappop(self.task_heap)
        if task in self.task_map:
            # task has to be in the heap
            # going to the front end
            del self.task_map[task[0]]
            # print(f"Top task is {task}")
            return task

    def updt(self, tid, imp, urg):
        if tid not in self.task_map:
            return None
        del self.task_map[tid]
        # adding the task to task_heap
        prio = -(imp + urg)
        heappush(self.task_heap, (prio, imp, urg, tid))
        self.task_map[tid] = (prio, imp, urg)


tm = Taskmanager()
tm.add(imp=1, urg=5, tid=0)
tm.add(imp=2, urg=3, tid=1)
tm.add(imp=4, urg=3, tid=2)

tm.print_tasks()

print(f"Top task is: {tm.get_task()}")
print("After getting tasks")
tm.print_tasks()

tm.updt(tid=1, urg=2, imp=3)
print("after updating tid1")
tm.print_tasks()
