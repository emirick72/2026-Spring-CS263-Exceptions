import pytest
from hamcrest import assert_that, close_to, equal_to, instance_of, is_, none

from exception_snippets import *


def test_outside_list_bounds(capsys):
    a_list = ["Hello", "from", "a", "list"]

    expected = f"7 does not fall in the range [0, {len(a_list)}]\n"

    outside_list_bounds(a_list, 7)

    actual = capsys.readouterr().out
    assert_that(actual, is_(equal_to(expected)))


def test_parse_an_int():
    assert_that(parse_an_int("7"), is_(equal_to(7)))
    assert_that(parse_an_int("12"), is_(equal_to(12)))
    assert_that(parse_an_int("20.0"), is_(none()))
    assert_that(parse_an_int("The number 337"), is_(none()))
    assert_that(parse_an_int("The number 337"), is_(none()))
    assert_that(parse_an_int("Twenty"), is_(none()))


def test_missing_dictionary_key(capsys):
    a_table = {
        "Hello": "Thomas",
        "from": "The World of Python",
        "a": "Rust Programmer",
        "list": "memory overhead",
    }

    expected = "'7' does not correspond to an entry in lookup_table\n"

    missing_dictionary_key(a_table, "7")

    actual = capsys.readouterr().out
    assert_that(actual, is_(equal_to(expected)))


def test_divide():
    assert_that(divide(20, 5), is_(instance_of(float)))
    assert_that(divide(7, 5), is_(instance_of(float)))
    assert_that(divide(7.0, 5), is_(instance_of(float)))
    assert_that(divide(72.0, 5.0), is_(instance_of(float)))
    assert_that(divide(72.0, 0), is_(none()))
    assert_that(divide(72, 0), is_(none()))
    assert_that(divide(72, 0.0), is_(none()))
    assert_that(divide(72.0, 0.0), is_(none()))
