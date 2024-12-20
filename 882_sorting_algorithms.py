import random
import math

import matplotlib.pyplot as plt

def bubble_sort(list):
    operation = 0
    # Iterate through the length of the list
    for i in range(len(list) - 1):
        swap = False

        # Iterate through the list comparing adjacent values
        for j in (range(len(list) - 1 - i)):
            operation += 1
            # Swap two values to order
            if list[j] > list[j+1]:
                x = list[j]
                list[j] = list[j+1]
                list[j+1] = x
                swap = True

        # Break the loop if no swaps in the current operation
        if swap == False:
            break
    return operation

def insertion_sort(list):
    operation = 0
    # Iterate through the length of the list
    for i in range(1, len(list)):
        key = list[i]
        j = i - 1
        
        # Compare key to sorted elements
        while j >= 0 and key < list[j]:
            operation += 1
            list[j + 1] = list[j]
            j -= 1
        # Put key to right place
        list[j + 1] = key

        if j >= 0:  
            operation += 1
    return operation

def selection_sort(list):
    operation = 0
    for i in range(len(list) - 1):
        min_idx = i
        for j in range(i + 1, len(list)):
            operation += 1
            if list[j] < list[min_idx]:
                min_idx = j
        
        if min_idx != i:
            list[i], list[min_idx] = list[min_idx], list[i]
    return operation

def merge(left, right, operation):
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        operation += 1
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
            
    result.extend(left[i:])
    result.extend(right[j:])
    
    return result, operation

def merge_sort(list):
    operation = 0
    step = 1
    length = len(list)
    
    while step < length:
        for i in range(0, length, 2 * step):
            left = list[i:i + step]
            right = list[i + step:i + 2 * step]
            
            merged, operation = merge(left, right, operation)
            
            # Place the merged array back into the original array
            for j, val in enumerate(merged):
                list[i + j] = val
                
        # Double the sub-array length for the next iteration
        step *= 2  
        
    return operation

def plot_graph(data1, data2, data3, data4, sample, size, test_name):
    # Calculate complexity baseline
    O_n = []
    O_n_squared = []
    O_n_logn = []
    for i in range(0, size):
        O_n_squared.append((i/2) * i)
        O_n.append(i)
        if i > 0:
            O_n_logn.append(i * (math.log(i,2)))
    O_n_logn.insert(0,0)

    # Plot the data
    plt.figure(figsize=(10, 6)) 
    plt.plot(range(size),  O_n, label='O(n)', linestyle = 'dashed', c = 'green', lw = 0.7)
    plt.plot(range(size), O_n_squared, label='O(n²)', linestyle = 'dashed', c = 'red', lw = 0.7)
    plt.plot(range(size),  O_n_logn, label='O(n log n)', linestyle = 'dashed', c = 'blue', lw = 0.7)

    plt.scatter(sample, data1, label='Bubble', marker='x', zorder = 3)
    plt.scatter(sample, data2, label='Insertion', marker='o', c = 'hotpink', zorder = 2, lw = 0.7)
    plt.scatter(sample, data3, label='Selection', marker='v', c = 'purple', zorder = 2, lw = 0.7)
    plt.scatter(sample, data4, label='Merge', marker='>', zorder = 2, lw = 0.7)

    plt.title(f"Sorting Algorithm Operations Comparison for {test_name} Case")
    plt.xlabel("Sample Size")
    plt.ylabel("Operations")
    plt.legend()

    plt.grid(True)
    plt.show()


def test(size, test_count, test_type):
    try:
        size = int(size)
        test_count = int(test_count)
    except ValueError:
        print(f"Invalid input.")
        return
    
    bubble_operations = []
    insertion_operations = []
    selection_operations = []
    merge_operations = []
    sample_size = []

    for i in range(test_count):
        if test_type.lower() == 'best':
            list = [x for x in range(random.randint(1, size))]
        elif test_type.lower() == 'worst':
            list = [x for x in range(random.randint(1, size), 0, -1)]
        elif test_type.lower() == 'randomized':
            temp_size = random.randint(1, size)
            list = [random.randint(1, 100) for _ in range(temp_size)]
        else:
            print(f"Invalid input.")
            return
        
        sample_size.append(len(list))
        list1 = list.copy()
        list2 = list.copy()
        list3 = list.copy()
        list4 = list.copy()        

        bubble_operations.append(bubble_sort(list1))
        insertion_operations.append(insertion_sort(list2))
        selection_operations.append(selection_sort(list3))
        merge_operations.append(merge_sort(list4))
    
    plot_graph(bubble_operations, insertion_operations, selection_operations, merge_operations, sample_size, size, test_type)


test(200, 20, "Randomized")
test(200, 20, "Best")
test(200, 20, "Worst")