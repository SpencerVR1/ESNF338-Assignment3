import requests
import json
from time import perf_counter
from matplotlib import pyplot as plt

def binary_search(arr, first, last, key, mid=None):
    if mid is None:
        mid = int((first+last)/2)
    else:
        if first <= last:
            if key == arr[mid]:
                return mid
            elif key < arr[mid]:
                return binary_search(arr, first, mid-1, key)
            elif key > arr[mid]:
                return binary_search(arr, mid+1, last, key)
        else:
            return -1
        
def choose_methods(arr, first, last, tasks_data):
    mid_len = int(len(arr)//2)
    mid_shift = int((first + last) >> 1)
    mid_standard = int((first + last)/2)
    methods = {}
    for task in tasks_data:
        start_len = perf_counter()
        binary_search(arr, first, last, task, mid_len)
        stop_len = perf_counter()
        time_len = stop_len - start_len

        start_shift = perf_counter()
        binary_search(arr, first, last, task, mid_shift)
        stop_shift = perf_counter()
        time_shift = stop_shift - start_shift

        start_standard = perf_counter()
        binary_search(arr, first, last, task, mid_standard)
        stop_standard = perf_counter()
        time_standard = stop_standard - start_standard

        times = {"len": time_len, "shift": time_shift, "standard": time_standard}
        chosen_method = min(times, key=times.get)
        methods[task] = chosen_method
    
    return methods


if __name__ == "__main__":

    array_url = "https://raw.githubusercontent.com/ldklab/ensf338w23/main/assignments/assignment3/ex2data.json"
    array_response = requests.get(array_url)
    array_data = json.loads(array_response.text)

    tasks_url = "https://raw.githubusercontent.com/ldklab/ensf338w23/main/assignments/assignment3/ex2tasks.json"
    tasks_response = requests.get(tasks_url)
    tasks_data = json.loads(tasks_response.text)

    chosen_methods = choose_methods(array_data, 0, len(array_data)-1, tasks_data)
    task = [task for task in chosen_methods]
    methods = [mid for mid in chosen_methods.values()]
    colors_d = {'len': 'red', 'shift': 'green', 'standard': 'blue'}
    colors = [colors_d[method] for method in methods]

    plt.scatter(task, methods, c=colors)
    plt.xlabel("Task")
    plt.ylabel("Chosen midpoint")
    plt.show()

    




