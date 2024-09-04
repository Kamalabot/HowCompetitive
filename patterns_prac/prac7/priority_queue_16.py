import heapq


class TaskManager:
    def __init__(self):
        # tasks is the heap in which the tasks are pushed in
        self.tasks = []
        # tasks map store the tasks with task_id as key
        self.tasks_map = {}

    def add_task(self, task_id, urgency, importance):
        # create priority
        priority = -(urgency + importance)
        # push tasks into the heap with priority as the first tuple element
        heapq.heappush(self.tasks, (priority, task_id, urgency, importance))
        # add the task_id to the task_map
        self.tasks_map[task_id] = (priority, urgency, importance)

    def get_task(self):
        # pop the high priority task
        _, task_id, urgency, importance = heapq.heappop(self.tasks)
        # check if the task_id in task_map and del it
        if task_id in self.tasks_map:
            del self.tasks_map[task_id]
            print(
                f"Here is urgent task of {task_id}, with urge: {urgency} and imp: {importance}"
            )
            return (task_id, urgency, importance)
        print("No Tasks...")
        return None

    def update_task(self, task_id, new_urge, new_imp):
        if task_id in self.tasks_map:
            # delete the old task completely
            del self.tasks_map[task_id]
            # need to remove it from tasks also, so find the index
            # not required, as it is not present in tasks map
            # create new priority
            priority = -(new_imp + new_urge)
            # push the new task into the tasks heap
            task = (priority, task_id, new_urge, new_imp)
            heapq.heappush(self.tasks, task)

    def print_tasks(self):
        for _, task in self.tasks_map.items():
            print(f"Task is: Priority: {-1 * task[0]}, urge: {task[1]}, imp: {task[2]}")


tm1 = TaskManager()
tm1.add_task(task_id=0, urgency=1, importance=1)
tm1.add_task(task_id=2, urgency=5, importance=2)
tm1.add_task(task_id=1, urgency=0, importance=3)

tm1.print_tasks()

print(tm1.get_task())

print("After getting the urgent task\n")

tm1.print_tasks()

tm1.update_task(task_id=1, new_imp=5, new_urge=5)
print("After updating task_id: 1\n")
tm1.print_tasks()
