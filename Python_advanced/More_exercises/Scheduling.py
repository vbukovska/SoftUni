from collections import deque
jobs = [int(t) for t in input(). split(", ")]

important_job = int(input())
passed_cycles = 0
jobs = deque(sorted([(index, job) for index, job in enumerate(jobs)], key=lambda x: (x[1], x[0])))

while jobs:
    job = jobs.popleft()
    job_index = job[0]
    job_time = job[1]
    passed_cycles += job[1]
    if job_index == important_job:
        break
print(passed_cycles)
