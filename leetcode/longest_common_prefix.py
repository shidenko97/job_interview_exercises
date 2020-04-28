"""
https://leetcode.com/articles/longest-common-prefix/
"""

STRINGS: tuple = ("flower", "flow", "flight")


def get_longest_common_prefix(strings: tuple) -> str:
    """
    Get longest common prefix
    :param strings: The strings to analyze
    :type strings: tuple
    :return: The longest common prefix
    :rtype: str
    """

    # Make a first string as a base string and everything else as rest
    base_string: str = strings[0]
    rest_strings: tuple = strings[1:]

    # Iterate on each character in string
    for i in range(len(base_string)):

        # Filter strings that not start with the same base string
        filtered: list = [1 for string in rest_strings
                          if string.startswith(base_string[0:i])]

        # Also we can use a filter function
        # filtered: list = list(filter(lambda a: a.startswith(base_string[0:i]),
        #                             strings[1:]))

        if len(filtered) != len(rest_strings):
            break
    else:
        return base_string

    return base_string[0:i - 1]


if __name__ == "__main__":
    print(get_longest_common_prefix(STRINGS))
