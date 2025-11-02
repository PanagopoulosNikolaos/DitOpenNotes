"""
DSA_Python - Data Structures and Algorithms in Python

A comprehensive collection of data structure and algorithm implementations
with detailed explanations and examples.

Modules:
- data_structures: Core data structures (arrays, linked lists, stacks, queues, 
                   hash tables, trees, graphs)
- algorithms: Sorting, searching, and graph algorithms
"""

__version__ = '1.0.0'
__author__ = 'Nikolaos Panagopoulos'

# Import main classes for easy access
from .data_structures.arrays import DynamicArray, StaticArray
from .data_structures.linked_lists import SinglyLinkedList, DoublyLinkedList
from .data_structures.stacks import ArrayStack, LinkedStack
from .data_structures.queues import ArrayQueue, CircularQueue, LinkedQueue, Deque
from .data_structures.hash_tables import HashMapChaining, HashMapLinearProbing, HashSet
from .data_structures.trees import BinaryTree, BinarySearchTree, AVLTree
from .data_structures.graphs import GraphAdjacencyList, GraphAdjacencyMatrix, WeightedGraph

from .algorithms.sorting import SortingAlgorithms
from .algorithms.searching import SearchingAlgorithms, AdvancedSearching
from .algorithms.graph_algorithms import ShortestPathAlgorithms, MinimumSpanningTree, MaximumFlow

__all__ = [
    # Data Structures
    'DynamicArray', 'StaticArray',
    'SinglyLinkedList', 'DoublyLinkedList',
    'ArrayStack', 'LinkedStack',
    'ArrayQueue', 'CircularQueue', 'LinkedQueue', 'Deque',
    'HashMapChaining', 'HashMapLinearProbing', 'HashSet',
    'BinaryTree', 'BinarySearchTree', 'AVLTree',
    'GraphAdjacencyList', 'GraphAdjacencyMatrix', 'WeightedGraph',
    
    # Algorithms
    'SortingAlgorithms',
    'SearchingAlgorithms', 'AdvancedSearching',
    'ShortestPathAlgorithms', 'MinimumSpanningTree', 'MaximumFlow',
]
