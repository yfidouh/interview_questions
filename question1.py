from typing import List, Union
from copy import deepcopy
from random import randint

from LinkedList import ListNode, LinkedList


def merge_linkedLists3(linked_lists: List[LinkedList]) -> LinkedList:
    linked_lists = deepcopy(linked_lists)
    final_linked_list, *rest = linked_lists
    for linked_list in rest:
        for node in linked_list:
            final_linked_list.insert(ListNode(node.val))
    return final_linked_list


def minpop(linked_lists: List[LinkedList]) -> Union[ListNode, None]:
    # find the min and it's index:
    _min = min(
        [
            (linked_list.head, i)
            for i, linked_list in enumerate(linked_lists)
            if linked_list.head is not None
        ],
        key=lambda x: x[0],
    )
    if _min:
        return linked_lists[_min[-1]].pop()
    return None


def maxpop(linked_lists: List[LinkedList]) -> Union[ListNode, None]:
    # find the max and it's index:
    _max = max(
        [
            (linked_list.head, i)
            for i, linked_list in enumerate(linked_lists)
            if linked_list.head is not None
        ],
        key=lambda x: x[0],
    )
    if _max:
        return linked_lists[_max[-1]].pop()
    return None


def merge_linkedLists2(linked_lists: List[LinkedList]) -> LinkedList:
    linked_lists = deepcopy(linked_lists)
    final_linked_list = LinkedList()
    while not all(ll.head is None for ll in linked_lists):
        final_linked_list.append(minpop(linked_lists))
    return final_linked_list


def merge_linkedLists1(linked_lists: List[LinkedList]) -> LinkedList:
    linked_lists = deepcopy(linked_lists)
    for linked_list in linked_lists:
        linked_list.reverse()
    final_linked_list = LinkedList()
    while not all(ll.head is None for ll in linked_lists):
        final_linked_list.push(maxpop(linked_lists))
    return final_linked_list


def pretty_print(x: Union[List[LinkedList], LinkedList]) -> None:
    if isinstance(x, LinkedList):
        print(x)
        return
    print("[")
    for node in x:
        print("\t", node, ",")
    print("]")


def generate_input(n: int = 1, k: int = 1) -> List[LinkedList]:
    return [
        LinkedList(sorted([randint(-3, 1000) for _ in range(randint(1, max(1, n)))]))
        for _ in range(k)
    ]


test_input = generate_input(10, 3)

pretty_print(test_input)


# pretty_print(merge_linkedLists2(test_input))
pretty_print(merge_linkedLists1(test_input))

# assert str(merge_linkedLists2(test_input)) == str(merge_linkedLists1(test_input))
