from typing import Iterable, Type, TypeVar

T = TypeVar('T')


def binary_search(elements: Iterable[Type[T]], element: Type[T]) -> int:
    """Search function for element in elements list.
    Returns index of element if present in elements or -1 otherwise.

    O(log N) where N is len(elements)

    Args:
        elements (Iterable[Type[T]]): a sorted list of elements
        element (Type[T]): a element to search in the list

    Raises:
        ArgumentError: neither element or elements can be null or empty

    Returns:
        int: index of element if present in elements or -1 otherwise
    """

    if not elements:
        raise ValueError("elements")
    if not element:
        raise ValueError(element)

    low = 0
    high = len(elements) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = elements[mid]
        if guess == element:
            return mid
        if guess > element:
            high = mid - 1
        else:
            low = mid + 1
    return -1
