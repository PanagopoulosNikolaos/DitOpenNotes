"""
Data Structures Module

Contains implementations of fundamental data structures:
- Arrays (Dynamic and Static)
- Linked Lists (Singly and Doubly)
- Stacks (Array-based and Linked)
- Queues (Array, Circular, Linked, and Deque)
- Hash Tables (Chaining and Linear Probing)
- Trees (Binary, BST, AVL)
- Graphs (Adjacency List and Matrix)
"""

from .arrays import DynamicArray, StaticArray
from .linked_lists import SinglyLinkedList, DoublyLinkedList
from .stacks import ArrayStack, LinkedStack, StackApplications
from .queues import ArrayQueue, CircularQueue, LinkedQueue, Deque
from .hash_tables import HashMapChaining, HashMapLinearProbing, HashSet
from .trees import BinaryTree, BinarySearchTree, AVLTree
from .graphs import GraphAdjacencyList, GraphAdjacencyMatrix, WeightedGraph

__all__ = [
    'DynamicArray', 'StaticArray',
    'SinglyLinkedList', 'DoublyLinkedList',
    'ArrayStack', 'LinkedStack', 'StackApplications',
    'ArrayQueue', 'CircularQueue', 'LinkedQueue', 'Deque',
    'HashMapChaining', 'HashMapLinearProbing', 'HashSet',
    'BinaryTree', 'BinarySearchTree', 'AVLTree',
    'GraphAdjacencyList', 'GraphAdjacencyMatrix', 'WeightedGraph',
]
