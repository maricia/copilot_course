import pytest

from adventure.random_item_selector import RandomItemSelector


def test_pull_random_item_returns_items_without_repetition_before_reset():
    selector = RandomItemSelector(["a", "b", "c"])
    first = selector.pull_random_item()
    second = selector.pull_random_item()
    third = selector.pull_random_item()

    assert {first, second, third} == {"a", "b", "c"}
    assert len({first, second, third}) == 3


def test_pull_random_item_resets_after_exhausting_items():
    selector = RandomItemSelector(["a"])
    first = selector.pull_random_item()
    second = selector.pull_random_item()

    assert first == "a"
    assert second == "a"


def test_add_item_increases_item_pool():
    selector = RandomItemSelector(["a"])
    selector.add_item("b")

    assert set(selector.items) == {"a", "b"}
