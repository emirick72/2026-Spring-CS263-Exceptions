from typing import Any


def outside_list_bounds(a_list: list[Any], idx: int):
    """
    Handle an IndexError for an arbitrary list. If an IndexError does occur...
    the message...

    {idx} does not fall in the range [0, {len(a_list)}]

    should be written to standard out... where the values denoted by {} are
    placeholders
    """

    entry = a_list[idx]


def parse_an_int(raw_value: str) -> int | None:
    """
    Parse a string into an int. If the supplied value cannot be parsed...
    return None
    """

    return int(raw_value)


def missing_dictionary_key(lookup_table: dict[str, Any], key: str):
    """
    Retrieve a specified key from a dictionary. If the key is not present...
    output the message...

    '{key}' does not correspond to an entry in lookup_table

    where the values denoted by {} are placeholders
    """

    entry = lookup_table[key]


def divide(lhs: int | float, rhs: int | float) -> float | None:
    """
    Divide lhs by rhs. If a ZeroDivisionError occurs... return None
    """

    return lhs / rhs
