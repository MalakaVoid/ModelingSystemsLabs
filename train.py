def get_time_in_buffer_together(arrivals, buffers):
    count_of_programs = 1
    buffers_pr_time = [0 for i in range(0, 10)]
    arrival = 0
    exit_time = 0
    for i in range(0, len(arrivals)):
        if exit_time > arrivals[i]:
            arrival = exit_time
        else:
            arrival = arrivals[i]

        count_of_programs = 0

        if buffers[i] != 0:
            count_of_programs = 1

        exit_time = arrivals[i] + buffers[i]

        for j in range(i+1, len(arrivals)):
            if arrival < arrivals[j] and arrivals[j] < exit_time:
                buffers_pr_time[count_of_programs] += arrivals[j] - arrival
                count_of_programs += 1
                arrival = arrivals[j]

        buffers_pr_time[count_of_programs] += exit_time - arrival
    return buffers_pr_time


print("TRYYYYYYYYYYYYYYYYYYYYYYY")
print(get_time_in_buffer_together([1,2,3,4], [1.5, 2,1 ,1]))
