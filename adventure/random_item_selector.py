import random
from typing import Any, Iterable, Optional


class RandomItemSelector:
    def __init__(self, items: Optional[Iterable[Any]]):
        self.items: list[Any] = list(items) if items is not None else []
        self.used_items: list[Any] = []

    def add_item(self, item: Any) -> None:
        self.items.append(item)

    def pull_random_item(self):
        if not self.items:
            self.reset()
            return None

        available_items = [item for item in self.items if item not in self.used_items]
        if not available_items:
            self.reset()
            available_items = list(self.items)

        selected = random.choice(available_items)
        self.used_items.append(selected)
        return selected

    def reset(self):
        self.used_items.clear()
