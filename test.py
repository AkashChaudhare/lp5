from multiprocessing import Process, Manager

def parallel_min(data, shared_result):
    min_val = min(data)
    shared_result.append(min_val)

def parallel_max(data, shared_result):
    max_val = max(data)
    shared_result.append(max_val)

def parallel_sum(data, shared_result):
    sum_val = sum(data)
    shared_result.append(sum_val)

def parallel_average(data, shared_result):
    avg_val = sum(data) / len(data)
    shared_result.append(avg_val)

if __name__ == '__main__':
    input_data = [4, 8, 2, 1, 6, 7, 5, 3]

    with Manager() as manager:
        shared_result = manager.list()

        process_list = []

        min_process = Process(target=parallel_min, args=(input_data, shared_result))
        min_process.start()
        process_list.append(min_process)

        max_process = Process(target=parallel_max, args=(input_data, shared_result))
        max_process.start()
        process_list.append(max_process)

        sum_process = Process(target=parallel_sum, args=(input_data, shared_result))
        sum_process.start()
        process_list.append(sum_process)

        average_process = Process(target=parallel_average, args=(input_data, shared_result))
        average_process.start()
        process_list.append(average_process)

        for process in process_list:
            process.join()

        result = list(shared_result)
        min_val, max_val, sum_val, avg_val = result

        print("Minimum:", min_val)
        print("Maximum:", max_val)
        print("Sum:", sum_val)
        print("Average:", avg_val)
