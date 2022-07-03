class Solution:
    def leastInterval(self, tasks, n):
        task_count = dict()
        for t in tasks:
            task_count[t] = task_count.get(t, 0) + 1
        sorted_tasks = sorted(task_count, key=task_count.get, reverse=True)
        
        max_num = task_count[sorted_tasks[0]]
        length = (max_num - 1) * (n + 1) + 1
        for t in sorted_tasks[1:]:
            if task_count[t] == max_num:
                length += 1

        return max(length, len(tasks))
