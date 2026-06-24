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

    def pop(self, index=-1):
        " adding notification message "
        x = super().pop(index)
        print(f"Added [{x}] to the list.")
