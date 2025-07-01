from typing import Union, Sequence


def max_list_iter(num_list: Union[None, Sequence[float]]) -> Union[None, float]:  # must use iteration not recursion
    '''Finds the max of a list of numbers and returns the value (not the index)
    If int_list is empty, returns None. If list is None, raises ValueError'''

    if num_list == None:
        raise ValueError("list is None")

    elif len(num_list) == 0:
        return None
    else:
        max_of_list = num_list[0]
        for num in num_list:
            if max_of_list < num:
                max_of_list = num
            else:
                max_of_list = max_of_list
        return max_of_list


def reverse_rec(num_list: Union[None, Sequence[float]]) -> Sequence[float]:  # must use recursion
    '''Recursively reverses a list of numbers and returns the reversed list
    Should not mutate the input list
    If list is None, raises ValueError'''
    if num_list is None:
        raise ValueError

    # Base case if the list is 1 or 0 return the original list
    elif len(num_list) <= 1:
        return num_list

    # Recursive step, slice the list but the first index, then add the first index to the end of the list then repeat
    # Example: [1, 2, 3, 4, 5] -> [2, 3, 4, 5] (In memory is [2, 3, 4, 5, 1])
    # [2, 3, 4, 5] -> [3, 4, 5] (In memory is [3, 4, 5, 1, 2])
    # [3, 4, 5] -> [4, 5] (In memory is [4, 5, 1, 2, 3])
    # [4, 5] -> [5] (In memory os [5, 4, 3, 2, 1])
    # Then the new input list is just [5] which is equal to 1, so it returns [5, 4, 3, 2, 1]
    else:
        temp_list = num_list[1:len(num_list)]
        return reverse_rec(temp_list) + [num_list[0]]


def bin_search(target: int, low: int, high: int, int_list: list[int]) -> Union[None, int]:
    """
    Searches for the target in int_list[low..high] and returns the index if found.
    If the target is not found, returns None. If the list is None, raises ValueError.
    Assumes that int_list is sorted integers and contains no duplicates, and that low
    and high are valid indices within the list.
    """
    if int_list is None:
        raise ValueError

    if low > high:
        return None  # Target not found

    mid = (low + high) // 2
    if int_list[mid] == target:
        return mid  # Found the target

    elif int_list[mid] > target:
        # Search the left half
        return bin_search(target, low, mid - 1, int_list)

    else:
        # Search the right half
        return bin_search(target, mid + 1, high, int_list)


def reverse_list_mutate(num_list: Union[None, Sequence[float]]) -> None:
    '''Reverses a list of numbers, modifies the input list, returns None
    If list is None, raises ValueError'''
    if num_list is None:
        raise ValueError

    elif len(num_list) == 0:
        return None

    else:
        for i in range(1, len(num_list)):
            replace = num_list.pop(i)
            num_list.insert(0, replace)
