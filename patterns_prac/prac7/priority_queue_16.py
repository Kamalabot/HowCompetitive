import heapq

# intuition1: use two seperate stores, maintaining priority and storing tasks
# intuition2: create the priority by adding the urgency and importance
# intuition3: push the tasks with priority int the heapq
# intuition4: poping the task from priority and deleting from tasks store
# intuition5: updating the tasks will call for re-push into heapq, and
# removing earlier taskid from tasks store


class TaskManager:
    def __init__(self):
        self.task_heap = []
        self.task_map = {}

    def add_task(self, tid, urg, imp):
        pri = -(urg + imp)
        heapq.heappush(self.task_heap, (pri, tid, urg, imp))
        self.task_map[tid] = (pri, urg, imp)
        # print(f"pushed to heap: {self.task_heap}")

    def print_tasks(self):
        for tid, task in self.task_map.items():
            print(f"tid: {tid} urge: {task[1]} impo: {task[2]}")

    def get_task(self):
        _, tid, urg, imp = heapq.heappop(self.task_heap)
        if tid in self.task_map:
            del self.task_map[tid]
            print(f"Returning tid: {tid} urge: {urg} impo: {imp}")
            return (tid, urg, imp)
        print("No tasks found")
        return None

    def update_task(self, tid, nurg, nimp):
        if tid in self.task_map:
            del self.task_map[tid]
            new_pri = -(nurg + nimp)
            heapq.heappush(self.task_heap, (new_pri, tid, nurg, nimp))
            self.task_map[tid] = (new_pri, nurg, nimp)
        else:
            print("check taskid, given taskid is missing...")


tm1 = TaskManager()
tm1.add_task(tid=0, urg=1, imp=1)
tm1.add_task(tid=1, urg=3, imp=2)
tm1.add_task(tid=2, urg=1, imp=1)

tm1.print_tasks()

print(tm1.get_task())

print("After getting the urgent task\n")

tm1.print_tasks()

tm1.update_task(tid=2, nimp=5, nurg=5)
print("After updating task_id: 1\n")
tm1.print_tasks()
