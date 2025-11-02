"""
HASH TABLES - Data Structure Implementation

A hash table (hash map) is a data structure that implements an associative array, mapping keys to values.
It uses a hash function to compute an index into an array of buckets/slots, from which the desired value can be found.

Key Characteristics:
- Average case: Insert, Delete, Search - O(1)
- Worst case (with collisions): O(n)
- Uses hash function to map keys to indices
- Requires collision resolution (chaining or open addressing)
- Dynamic resizing when load factor exceeds threshold
- Trade-off between space and time efficiency

Hash Function:
A hash function converts a key into an array index:
    index = hash(key) % array_size

Example: hash("apple") = 12345 → 12345 % 10 = 5 (index 5)

Collision Resolution:
1. Chaining: Each bucket contains a linked list of entries
   Index 5: → [("apple", 1)] → [("banana", 2)] → None

2. Open Addressing: Find next available slot
   - Linear Probing: Check next slot sequentially
   - Quadratic Probing: Check slots at quadratic intervals
   - Double Hashing: Use second hash function

Load Factor = number_of_entries / table_size
When load factor > threshold (typically 0.75), resize and rehash

Common Use Cases:
- Database indexing
- Caching (memorization)
- Symbol tables in compilers
- Counting frequencies
- Removing duplicates
- Implementing sets and maps
"""

class HashMapChaining:
    """
    Hash map implementation using chaining for collision resolution.
    Each bucket contains a list of (key, value) pairs.
    """
    
    def __init__(self, capacity=11):
        self._capacity = capacity
        self._size = 0
        self._buckets = [[] for _ in range(self._capacity)]
    
    def _hash(self, key):
        """Compute hash value for a key"""
        return hash(key) % self._capacity
    
    def __len__(self):
        return self._size
    
    def __getitem__(self, key):
        """Get value by key - Average O(1), Worst O(n)"""
        bucket_index = self._hash(key)
        bucket = self._buckets[bucket_index]
        
        for k, v in bucket:
            if k == key:
                return v
        raise KeyError(f"Key '{key}' not found")
    
    def __setitem__(self, key, value):
        """Set key-value pair - Average O(1), Worst O(n)"""
        bucket_index = self._hash(key)
        bucket = self._buckets[bucket_index]
        
        # Update if key exists
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return
        
        # Add new key-value pair
        bucket.append((key, value))
        self._size += 1
        
        # Resize if load factor > 0.75
        if self._size / self._capacity > 0.75:
            self._resize()
    
    def __delitem__(self, key):
        """Delete key-value pair - Average O(1), Worst O(n)"""
        bucket_index = self._hash(key)
        bucket = self._buckets[bucket_index]
        
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket.pop(i)
                self._size -= 1
                return
        raise KeyError(f"Key '{key}' not found")
    
    def __contains__(self, key):
        """Check if key exists - Average O(1), Worst O(n)"""
        try:
            self[key]
            return True
        except KeyError:
            return False
    
    def _resize(self):
        """Resize and rehash when load factor is high - O(n)"""
        old_buckets = self._buckets
        self._capacity = self._capacity * 2 + 1
        self._buckets = [[] for _ in range(self._capacity)]
        self._size = 0
        
        for bucket in old_buckets:
            for key, value in bucket:
                self[key] = value
    
    def keys(self):
        """Return all keys"""
        result = []
        for bucket in self._buckets:
            for key, value in bucket:
                result.append(key)
        return result
    
    def values(self):
        """Return all values"""
        result = []
        for bucket in self._buckets:
            for key, value in bucket:
                result.append(value)
        return result
    
    def items(self):
        """Return all key-value pairs"""
        result = []
        for bucket in self._buckets:
            for item in bucket:
                result.append(item)
        return result
    
    def __str__(self):
        items = [f"'{k}': {v}" for k, v in self.items()]
        return "{" + ", ".join(items) + "}"

class HashMapLinearProbing:
    """
    Hash map using open addressing with linear probing.
    When collision occurs, linearly search for next empty slot.
    """
    
    def __init__(self, capacity=11):
        self._capacity = capacity
        self._size = 0
        self._keys = [None] * self._capacity
        self._values = [None] * self._capacity
        self._deleted = object()  # Marker for deleted entries
    
    def _hash(self, key):
        """Compute hash value for a key"""
        return hash(key) % self._capacity
    
    def __len__(self):
        return self._size
    
    def _find_slot(self, key):
        """Find slot for key using linear probing"""
        index = self._hash(key)
        first_deleted = None
        
        while self._keys[index] is not None:
            if self._keys[index] is self._deleted:
                if first_deleted is None:
                    first_deleted = index
            elif self._keys[index] == key:
                return index
            index = (index + 1) % self._capacity
        
        return first_deleted if first_deleted is not None else index
    
    def __getitem__(self, key):
        """Get value by key - Average O(1), Worst O(n)"""
        index = self._find_slot(key)
        if self._keys[index] == key:
            return self._values[index]
        raise KeyError(f"Key '{key}' not found")
    
    def __setitem__(self, key, value):
        """Set key-value pair - Average O(1), Worst O(n)"""
        if self._size / self._capacity > 0.5:
            self._resize()
        
        index = self._find_slot(key)
        
        if self._keys[index] != key:
            self._size += 1
        
        self._keys[index] = key
        self._values[index] = value
    
    def __delitem__(self, key):
        """Delete key-value pair - Average O(1), Worst O(n)"""
        index = self._find_slot(key)
        if self._keys[index] == key:
            self._keys[index] = self._deleted
            self._values[index] = None
            self._size -= 1
        else:
            raise KeyError(f"Key '{key}' not found")
    
    def __contains__(self, key):
        """Check if key exists"""
        try:
            self[key]
            return True
        except KeyError:
            return False
    
    def _resize(self):
        """Resize and rehash - O(n)"""
        old_keys = self._keys
        old_values = self._values
        
        self._capacity = self._capacity * 2 + 1
        self._keys = [None] * self._capacity
        self._values = [None] * self._capacity
        self._size = 0
        
        for i in range(len(old_keys)):
            if old_keys[i] is not None and old_keys[i] is not self._deleted:
                self[old_keys[i]] = old_values[i]
    
    def __str__(self):
        items = []
        for i in range(self._capacity):
            if self._keys[i] is not None and self._keys[i] is not self._deleted:
                items.append(f"'{self._keys[i]}': {self._values[i]}")
        return "{" + ", ".join(items) + "}"

class HashSet:
    """
    Hash set implementation - stores unique elements only.
    Built on top of hash map, storing only keys.
    """
    
    def __init__(self, capacity=11):
        self._map = HashMapChaining(capacity)
    
    def __len__(self):
        return len(self._map)
    
    def add(self, element):
        """Add element to set - O(1) average"""
        self._map[element] = True
    
    def remove(self, element):
        """Remove element from set - O(1) average"""
        del self._map[element]
    
    def __contains__(self, element):
        """Check if element exists - O(1) average"""
        return element in self._map
    
    def __iter__(self):
        """Iterate over elements"""
        return iter(self._map.keys())
    
    def __str__(self):
        return "{" + ", ".join(str(x) for x in self) + "}"

# Example usage
if __name__ == "__main__":
    print("=== Hash Map with Chaining Demo ===")
    hash_map = HashMapChaining()
    
    # Insert key-value pairs
    hash_map["apple"] = 5
    hash_map["banana"] = 7
    hash_map["orange"] = 3
    hash_map["grape"] = 12
    print(f"Hash map: {hash_map}")
    print(f"Size: {len(hash_map)}")
    
    # Access values
    print(f"apple: {hash_map['apple']}")
    print(f"grape: {hash_map['grape']}")
    
    # Update value
    hash_map["apple"] = 10
    print(f"After update: {hash_map}")
    
    # Check existence
    print(f"'banana' in map: {'banana' in hash_map}")
    print(f"'mango' in map: {'mango' in hash_map}")
    
    # Delete entry
    del hash_map["orange"]
    print(f"After deleting 'orange': {hash_map}")
    
    # Iterate
    print(f"Keys: {hash_map.keys()}")
    print(f"Values: {hash_map.values()}")
    
    print("\n=== Hash Map with Linear Probing Demo ===")
    lp_map = HashMapLinearProbing()
    
    lp_map["one"] = 1
    lp_map["two"] = 2
    lp_map["three"] = 3
    print(f"Linear probing map: {lp_map}")
    
    print("\n=== Hash Set Demo ===")
    hash_set = HashSet()
    
    # Add elements
    for num in [1, 2, 3, 2, 4, 3, 5]:
        hash_set.add(num)
    print(f"Set (duplicates removed): {hash_set}")
    
    # Check membership
    print(f"3 in set: {3 in hash_set}")
    print(f"10 in set: {10 in hash_set}")
    
    # Remove element
    hash_set.remove(2)
    print(f"After removing 2: {hash_set}")
