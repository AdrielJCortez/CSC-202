import random
import time

'''Returns the number of comparisons between the objects being sorted.'''
def selection_sort(list):
    comparisons = 0
    for i in range(len(list) - 1):
        min_spot = i
        for j in range(i + 1, len(list)):
            comparisons += 1
            if list[j] < list[min_spot]:
                min_spot = j
        if i != min_spot:
            swap(list, i, min_spot)  # Could also say list[i], list[min_spot] = list[min_spot], list[i]
    return comparisons

# Not needed in Python, but useful in other languages
def swap(list, i, j):
    temp = list[i]
    list[i] = list[j]
    list[j] = temp
    
'''Returns the number of comparisons between the objects being sorted.
   Do not count comparisons of loop variables.'''
def insertion_sort(list):
    comp = 0
    for i in range(1, len(list)):
        item = list[i]
        j = i
        while j > 0:
            comp += 1
            if list[j - 1] > item:
                list[j] = list[j - 1]
                j -= 1
            else:
                 break
        list[j] = item
    return comp
   

def main():
    # Code coverage NOT required for main
    # Give the random number generator a seed, so the same sequence of 
    # random numbers is generated at each run
    random.seed(1234) 
    
    # Generate 5000 random numbers from 0 to 999,999
    randoms = random.sample(range(1000000), 32000)
    start_time = time.time() 
    comps = insertion_sort(randoms)
    stop_time = time.time()
    print(comps, stop_time - start_time)

if __name__ == '__main__': 
    main()
