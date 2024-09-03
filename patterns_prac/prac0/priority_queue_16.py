import heapq


# intuition 1: Uses heapq to store the tasks
# intuition 2: tasks are stored twice, once in dict,
# and other time for priority in heapq


class TaskManager:
    def __init__(self):
        self.tasks = []
        self.task_map = {}
        self.task_id_counter = 0
        # manages insertion order

    def add_task(self, urgency, importance):
        task_id = self.task_id_counter
        self.task_id_counter += 1
        # counter id is updated manually

        # Calculate priority (Urgency)
        priority = -(urgency + importance)
        # task tuple is created
        task = (priority, task_id, urgency)
        # heap takes only lists
        heapq.heappush(self.tasks, task)
        self.task_map[task_id] = task

    def get_task(self):
        while self.tasks:
            _, task_id, urgency, importance = heapq.heappop(self.tasks)

            if task_id in self.task_map:
                del self.task_map[task_id]
                print(f"Task {task_id} with urgency: {urgency} is retrieved ")
                return (task_id, urgency, importance)

        print("No tasks available")
        return None

    def update_task(self, task_id, urgency, importance):
        if task_id in self.task_map:
            # Remove the old task from the map
            _, _, old_urgency, old_importance = self.task_map[task_id]
            del self.task_map[task_id]

            # Add the updated task
            priority = -(urgency + importance)  # Calculate new priority
            updated_task = (priority, task_id, urgency, importance)
            heapq.heappush(self.tasks, updated_task)
            self.task_map[task_id] = updated_task

            print(
                f"Task {task_id} updated from urgency {old_urgency}, importance {old_importance} to urgency {urgency}, importance {importance}."
            )
        else:
            print(f"Task ID {task_id} not found.")


tm = TaskManager()

tm.add_task(urgency=5, importance=3)
tm.add_task(urgency=8, importance=2)
tm.add_task(urgency=3, importance=6)

tm.get_task()
tm.update_task(0, urgency=10, importance=5)
tm.get_task()
tm.get_task()
