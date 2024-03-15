import math
from typing import List
from math import ceil


def get_item_at_position(list_in: List, pos: int) -> List:
    """
    Returns the item at pos.

    :param list_in: Input list
    :param pos: Position of desired item in list_in
    :return: Item in pos
    """
    #pass  # remove pass statement and implement me
    return (list_in[pos])


def print_list_items(list_in: List) -> None:
    """
    Given a list, this function iterates through it and prints each element.

    :param list_in: Input list
    :return: None
    """
    for item in range(len(list_in)):
        print(list_in[item])

#print_list_items()
    #pass  # remove pass statement and implement me



def sort_by_commit_count(list_in: List) -> List:
    """
    Given a list of entries, return a new list sorted based on the commit count.

    :param list_in: A list where each entry is a list containing a name and the commit count corresponding to a user
    :return: The same list sorted in ascending order based on the commit count
    """
    #pass  # remove pass statement and implement me

    sorted_list = sorted(list_in, key=lambda x: x[1])
    return sorted_list



def gen_list_of_nums(n: int) -> List[int]:
    """
    Given a number (N), this function returns a list of integers from 0 to N (exclusive).

    :param n: The number of items the result should contain
    :return: A list of integers
    """

    return list(range(n))   # generate a sequence of numbers from 0 to n using range and covert tha to list

    # Example usage:
    result = generate_integer_list(n)  # call the function and store the list in result variable
    print(result)


def half_list(list_in: List, half: int) -> List:
    """
    Given a list, this function will return a new list that contains half of the items in the list_in parameter.

    :param list_in: The list which will be used to generate the return value
    :param half: 1 will use the first half of the input list. 2 will use the second half of the input list.
    If the length of list_in is an odd number, round the half value up (hint: math.ceil()).
    :return: A list.
    """
    length = len(list_in)
    half_len = math.ceil(length / 2)
    first_half = list_in[: half_len]
    second_half = list_in[half_len:]
    if length % 2 != 0:
        second_half = list_in[half_len - 1:]

    # print(first_half)
    # print(second_half)

    if half == 1:
        return first_half
    elif half == 2:
        return second_half
    else:
        raise ValueError("The 'half' parameter must be either 1 or 2.")


def remove_odds(list_in: List[int]) -> None:
    """
    Given a list of integers, this function removes the odd numbers from the same list.

    :return: None
    """
    evens = [num for num in list_in if num % 2 == 0]  #create a new list containing only even numbers
    list_in.clear()  # clear the list
    list_in.extend(evens)  #add all the even numbers to the list


def remove_evens(list_in: List[int]) -> None:
    """
    Given a list of integers, this function removes the even numbers from the same list.

    :return: None
    """
    odds = [num for num in list_in if num % 2 != 0]
    list_in.clear()
    list_in.extend(odds)


def concatenate_lists(list_a: List, list_b: List) -> List:
    """
    Given two lists, this function combines them and returns the result as a new list.

    :param list_a: A list
    :param list_b: Another list
    :return: A list containing all elements from list_a and list_b
    """
    list_3 = list_a + list_b
    return list_3


def multiply_list(list_in: List, scalar: int) -> List:
    """
    Given a list and an integer, this function will return a new list which is the result of multiplying
    the input list by the value of the scalar.

    :param list_in: A list
    :param scalar: An integer
    :return: A list
    """
    new_list = scalar * list_in
    return new_list
