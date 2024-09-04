import heapq


# information 1: heapq is a array where a[k] <= a[2*k + 1]
# and a[2*k + 2]

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
        # tasks is the heap, which is simply an array
        # look at information above
        heapq.heappush(self.tasks, task)
        # heap will contain higher priority tasks
        # at the front
        self.task_map[task_id] = task
        # task_map is the actual store

    def get_task(self):
        while self.tasks:
            # simply pop the highest priority element
            _, task_id, urgency, importance = heapq.heappop(self.tasks)
            # move to task_map, and check if the task_id is present
            if task_id in self.task_map:
                # delete the task_id from the map
                del self.task_map[task_id]
                # return the task details
                print(f"Task {task_id} with urgency: {urgency} is retrieved ")
                return (task_id, urgency, importance)
        # if the id is not available, return none
        print("No tasks available")
        return None

    def update_task(self, task_id, urgency, importance):
        # go to the task map, and find if id present
        if task_id in self.task_map:
            # Remove the old task from the map
            _, _, old_urgency, old_importance = self.task_map[task_id]
            del self.task_map[task_id]

            # Add the updated task
            priority = -(urgency + importance)  # Calculate new priority
            # task_id is same
            updated_task = (priority, task_id, urgency, importance)
            # need to push into the heap again
            heapq.heappush(self.tasks, updated_task)
            # add the task to the task_map
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
