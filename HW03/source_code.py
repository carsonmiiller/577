if __name__ == "__main__":
    with open("./GivenTest-3.txt") as f:
       data = f.read()
    instances = int(input())
    num_scheduled_jobs = []
    for i in range(instances):
        num_jobs = int(input())
        jobs = []
        for j in range(num_jobs):
            job = input()
            jobs.append([job[0],job[2]])
        jobs = sorted(jobs,key=lambda l:l[1])
        scheduled_jobs = []
        scheduled_jobs.append(jobs[0])
        for j in range(1,num_jobs):
            if jobs[j][0] > jobs[j-1][1]:
                scheduled_jobs.append(jobs[j])
        num_scheduled_jobs.append(len(scheduled_jobs))
    for num in num_scheduled_jobs:
        print(num)