import heapq

class TaskManager:
    def __init__(self):
        self.heap = []          # Priority Queue
        self.task_map = {}      # HashMap for fast lookup
        self.counter = 0        # To handle same priority

    def add_task(self, name, priority):
        entry = (priority, self.counter, name)
        heapq.heappush(self.heap, entry)
        self.task_map[name] = entry
        self.counter += 1
        print("Task added")

    def execute_task(self):
        if not self.heap:
            print("No tasks")
            return
        task = heapq.heappop(self.heap)
        del self.task_map[task[2]]
        print("Executing:", task[2])

    def search_task(self, name):
        if name in self.task_map:
            print("Task found:", name)
        else:
            print("Task not found")

    def delete_task(self, name):
        if name not in self.task_map:
            print("Task not found")
            return
        entry = self.task_map.pop(name)
        self.heap.remove(entry)
        heapq.heapify(self.heap)
        print("Task deleted")

    def show_tasks(self):
        for t in sorted(self.heap):
            print(t[2], "Priority:", t[0])


tm = TaskManager()
tm.add_task("Coding", 2)
tm.add_task("Interview Prep", 1)
tm.add_task("Report", 3)

tm.show_tasks()
tm.execute_task()
tm.search_task("Coding")
tm.delete_task("Report")