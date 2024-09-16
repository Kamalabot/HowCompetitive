import heapq

# contains the code for task management

# intuition1: use two seperate stores, maintaining priority and storing tasks
# intuition2: create the priority by adding the urgency and importance
# intuition3: push the tasks with priority int the heapq
# intuition4: poping the task from priority and deleting from tasks store
# intuition5: updating the tasks will call for re-push into heapq, and
# removing earlier taskid from tasks store
