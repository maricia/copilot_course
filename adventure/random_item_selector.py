import random


class RandomItemSelector:
    def __init__(self, items):
        self.items = list(items) if items is not None else []
        self.used_items = []

    def add_item(self, item):
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
