import sys

if __name__ == "__main__":
    lst = []
    prev_size = sys.getsizeof(lst) / sys.getsizeof(0)

    for i in range(64):
        lst.append(i)
        size = sys.getsizeof(lst) / sys.getsizeof(0)
        if size > prev_size:
            print(f"Capacity changed by {size - prev_size}")
            prev_size = size
