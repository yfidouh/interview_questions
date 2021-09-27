from typing import Iterator, List, Union


class ListNode:
    def __init__(self, val=0, next=None) -> None:
        self.val = val
        self.next = next

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.val})"

    def __str__(self) -> str:
        return str(self.val)

    def __lt__(self, other):
        return self.val < other.val


class LinkedList:
    def __init__(self, nodes: List[int] = [], head: ListNode = None) -> None:
        self.head = head
        self.butt = None
        for node in nodes:
            self.append(ListNode(node, None))

    def __iter__(self) -> Iterator[ListNode]:
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def append(self, node: ListNode) -> None:
        if self.head is None:
            self.head = node
            self.butt = node
            return
        self.butt.next = node
        self.butt = self.butt.next
        # for current_node in self:
        #     pass
        # current_node.next = node

    def pop(self) -> Union[ListNode, None]:
        """pops off the first element if not None, otherwise returns none"""

        if self.head is None:
            return None

        val = self.head.val
        self.head = self.head.next
        return ListNode(val)

    def push(self, node: ListNode) -> None:
        """push first node onto head"""

        if self.head is None:
            self.head = node
            return

        temp_head = self.head
        self.head = node
        self.head.next = temp_head

    def insert(self, node: ListNode) -> None:
        last_node: ListNode = None
        for current_node in self:
            if current_node.val >= node.val:
                if last_node is None:
                    self.head = node
                    self.head.next = current_node
                else:
                    last_node.next = node
                    last_node.next.next = current_node
                return
            last_node = current_node
        else:
            self.append(node)

    def reverse(self):
        prev_node = None
        current_node = self.head
        while current_node is not None:
            current_node.next, prev_node, current_node = (
                prev_node,
                current_node,
                current_node.next,
            )
        self.head = prev_node

    def __repr__(self) -> str:
        nodes = [node.val for node in self]
        return f"{self.__class__.__name__}({nodes})"

    def __str__(self) -> str:
        nodes = [str(node) for node in self] + [str(None)]
        return " -> ".join(nodes)
