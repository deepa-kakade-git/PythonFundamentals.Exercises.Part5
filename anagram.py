def is_anagram(first_string: str, second_string: str) -> bool:
    """
    Given two strings, this functions determines if they are an anagram of one another.
    """
    #first_string = first_string.lower()
    #second_string = second_string.lower()

    first_string = ' '.join(char for char in first_string if char.isalnum())
    second_string = ' '.join(char for char in second_string if char.isalnum())

    first_string = sorted(first_string)
    second_string = sorted(second_string)


    return first_string == second_string


    #pass  # remove pass statement and implement me

