#!/usr/bin/python3
"""
list
"""

class VerboseList(list):
    " edeting "
    def append(self, item):
        " adding notification message "
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, item):
        " adding notification message "
        super().extend(item)
        print(f"Extended the list with [{len(item)}] items.")

    def remove(self, item):
        " adding notification message "
        super().remove(item)
        print(f"Removed [{item}] from the list.")

    def pop(self, item):
        " adding notification message "
        super().pop(item)
        print(f"Added [{item}] to the list.")

    def pop(self):
        " adding notification message "
        super().pop()
        print(f"Popped [{self[len(self) - 1]}] from the list.")
