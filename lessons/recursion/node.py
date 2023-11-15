<<<<<<< HEAD
"""Node class for linked list."""

from __future__ import annotations

class Node:

    data: int
    next: Node | None

    def __init__ (self, data: int, next: Node | None):
        """Construct a node."""
        self.data = data
        self.next = next
    
    def __str__(self) -> str:
        if self.next is None:
            # Base Case
            return str(self.data)
        else:
            # Recursive Step
            return str(self.data) + "->" + str(self.next)
        
        
=======
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
        
    def head(self):
        return None
    
    def tail(self):
        return None
    
    def last(self):
        return None
>>>>>>> db75118 (Added cq for recursion)
