def find_peak(list_of_integers):
    """
    Finds a peak in a list of unsorted integers.

    Args:
        list_of_integers: A list of unsorted integers.

    Returns:
        A peak element from the list if found, otherwise None.
    """
    if not list_of_integers:
        return None

    mid = len(list_of_integers) // 2

    if (mid == 0 or list_of_integers[mid] >= list_of_integers[mid - 1]) and \
            (mid == len(list_of_integers) - 1 or list_of_integers[mid] >= list_of_integers[mid + 1]):
        return list_of_integers[mid]

    elif mid > 0 and list_of_integers[mid] < list_of_integers[mid - 1]:
        return find_peak(list_of_integers[:mid])

    else:
        return find_peak(list_of_integers[mid + 1:])

