"""Node class for linked list."""

from __future__ import annotations

class Node:
    """My Node class for linked lists."""
    
    data: int
    next: Node | None
    
    def __init__(self, data: int, next: Node | None):
        """Construct Node."""
        self.data = data
        self. next = next
        
    def __str__(self) -> str:
        """Produce a string visualization of the linked list."""
        if self.next is None:
            # base case (where it ends!)
            return f"{self.data} -> None"
        else:
            return f"{self.data} -> {self.next}"
        
    def head(self) -> int | None:
        """Return the data in the first node of the linked list."""
        return self.data
    
    def tail(self) -> Node | None:
        """Return a linked list of every element except for the head."""
        return self.next
    
    def last(self) -> int | None:
        """Return the data in the last node of the linked list."""
        tail_node = self.tail()
        if tail_node != None:
            while tail_node.next != None:
                tail_node = tail_node.next
            return tail_node.data
        else:
            return None