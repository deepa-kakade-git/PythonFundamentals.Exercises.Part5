def is_palindrome(value: str) -> bool:
    """
    This function determines if a word or phrase is a palindrome

    :param value: A string
    :return: A boolean
    """
    # Remove spaces and punctuation, and convert to lowercase
    value = value.lower()
    value = ''.join(char for char in value if char.isalnum())
    return value == value[::-1]