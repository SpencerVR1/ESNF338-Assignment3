import random
from time import perf_counter
from matplotlib import pyplot as plt

def linear_search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1

def binary_search(arr, x):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = int((left + right)/2)
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    return -1

if __name__ == "__main__":
    arr = sorted([random.randint(1, 10000) for i in range(1000)])
    key = random.choice(arr)

    linear_times = []
    binary_times = []

    for i in range(100):
        start_linear = perf_counter()
        linear_search(arr, key)
        stop_linear = perf_counter()
        linear_times.append(stop_linear - start_linear)

        start_binary = perf_counter()
        binary_search(arr, key)
        stop_binary = perf_counter()
        binary_times.append(stop_binary - start_binary)

    linear_total = sum(linear_times)
    binary_total = sum(binary_times)
    print(f"Linear search: Total time = {linear_total:.6f}s")
    print(f"Binary search: Total time = {binary_total:.6f}s")
    
    fig, axs = plt.subplots(figsize=(9,3))
    axs1 = plt.subplot2grid(shape=(1,2), loc=(0,0))
    axs2 = plt.subplot2grid(shape=(1,2), loc=(0,1))
    plt.suptitle("Inefficient vs Efficient Sorted Array Search")

    axs1.plot(linear_times)
    axs1.set_title("Linear Search")
    axs1.set_xlabel("Frequency")
    axs1.set_ylabel("Execution Time (s)")

    axs2.plot(binary_times)
    axs2.set_title("Binary Search")
    axs2.set_xlabel("Frequency")
    axs2.set_ylabel("Execution Time (s)")

    plt.show()