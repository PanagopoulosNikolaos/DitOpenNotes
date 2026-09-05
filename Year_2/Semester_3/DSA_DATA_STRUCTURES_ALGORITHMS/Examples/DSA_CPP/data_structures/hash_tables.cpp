#include <iostream>
#include <vector>
#include <list>
#include <unordered_map>
#include <memory>
#include <functional>
#include <stdexcept>

/**
 * @brief HASH TABLES - Data Structure Implementation in C++
 * 
 * A hash table (hash map) is a data structure that implements an associative array, mapping keys to values.
 * It uses a hash function to compute an index into an array of buckets/slots, from which the desired value can be found.
 * 
 * Key Characteristics:
 * - Average case: Insert, Delete, Search - O(1)
 * - Worst case (with collisions): O(n)
 * - Uses hash function to map keys to indices
 * - Requires collision resolution (chaining or open addressing)
 * - Dynamic resizing when load factor exceeds threshold
 * - Trade-off between space and time efficiency
 * 
 * Hash Function:
 * A hash function converts a key into an array index:
 *     index = hash(key) % array_size
 * 
 * Example: hash("apple") = 12345 → 12345 % 10 = 5 (index 5)
 * 
 * Collision Resolution:
 * 1. Chaining: Each bucket contains a linked list of entries
 *    Index 5: → [("apple", 1)] → [("banana", 2)] → NULL
 * 
 * 2. Open Addressing: Find next available slot
 *    - Linear Probing: Check next slot sequentially
 *    - Quadratic Probing: Check slots at quadratic intervals
 *    - Double Hashing: Use second hash function
 * 
 * Load Factor = number_of_entries / table_size
 * When load factor > threshold (typically 0.75), resize and rehash
 * 
 * Common Use Cases:
 * - Database indexing
 * - Caching (memorization)
 * - Symbol tables in compilers
 * - Counting frequencies
 * - Removing duplicates
 * - Implementing sets and maps
 */

template<typename K, typename V>
class HashMapChaining {
private:
    struct KeyValuePair {
        K key;
        V value;
        
        KeyValuePair(const K& k, const V& v) : key(k), value(v) {}
    };
    
    std::vector<std::list<KeyValuePair>> _buckets;
    size_t _capacity;
    size_t _size;
    std::hash<K> _hashFunc;
    
    void _resize() {
        std::vector<std::list<KeyValuePair>> oldBuckets = _buckets;
        _capacity = _capacity * 2 + 1;
        _buckets.resize(_capacity);
        for (auto& bucket : _buckets) {
            bucket.clear();
        }
        _size = 0;
        
        for (const auto& bucket : oldBuckets) {
            for (const auto& kvp : bucket) {
                put(kvp.key, kvp.value);
            }
        }
    }
    
    size_t _hash(const K& key) const {
        return _hashFunc(key) % _capacity;
    }

public:
    /**
     * @brief Hash map implementation using chaining for collision resolution.
     * Each bucket contains a list of (key, value) pairs.
     */
    explicit HashMapChaining(size_t capacity = 11) : _capacity(capacity), _size(0) {
        _buckets.resize(_capacity);
    }

    size_t size() const {
        return _size;
    }

    bool empty() const {
        return _size == 0;
    }

    /**
     * @brief Get value by key - Average O(1), Worst O(n)
     */
    V& get(const K& key) {
        size_t bucketIndex = _hash(key);
        auto& bucket = _buckets[bucketIndex];
        
        for (auto& kvp : bucket) {
            if (kvp.key == key) {
                return kvp.value;
            }
        }
        throw std::out_of_range("Key not found");
    }

    /**
     * @brief Set key-value pair - Average O(1), Worst O(n)
     */
    void put(const K& key, const V& value) {
        size_t bucketIndex = _hash(key);
        auto& bucket = _buckets[bucketIndex];
        
        // Update if key exists
        for (auto& kvp : bucket) {
            if (kvp.key == key) {
                kvp.value = value;
                return;
            }
        }
        
        // Add new key-value pair
        bucket.emplace_back(key, value);
        ++_size;
        
        // Resize if load factor > 0.75
        if (static_cast<double>(_size) / _capacity > 0.75) {
            _resize();
        }
    }

    /**
     * @brief Delete key-value pair - Average O(1), Worst O(n)
     */
    void remove(const K& key) {
        size_t bucketIndex = _hash(key);
        auto& bucket = _buckets[bucketIndex];
        
        for (auto it = bucket.begin(); it != bucket.end(); ++it) {
            if (it->key == key) {
                bucket.erase(it);
                --_size;
                return;
            }
        }
        throw std::out_of_range("Key not found");
    }

    bool contains(const K& key) const {
        size_t bucketIndex = _hash(key);
        const auto& bucket = _buckets[bucketIndex];
        for (const auto& kvp : bucket) {
            if (kvp.key == key) {
                return true;
            }
        }
        return false;
    }

    std::vector<K> keys() const {
        std::vector<K> result;
        for (const auto& bucket : _buckets) {
            for (const auto& kvp : bucket) {
                result.push_back(kvp.key);
            }
        }
        return result;
    }

    std::vector<V> values() const {
        std::vector<V> result;
        for (const auto& bucket : _buckets) {
            for (const auto& kvp : bucket) {
                result.push_back(kvp.value);
            }
        }
        return result;
    }

    void print() const {
        std::cout << "{";
        bool first = true;
        for (const auto& bucket : _buckets) {
            for (const auto& kvp : bucket) {
                if (!first) std::cout << ", ";
                std::cout << kvp.key << ": " << kvp.value;
                first = false;
            }
        }
        std::cout << "}" << std::endl;
    }
};

template<typename K, typename V>
class HashMapLinearProbing {
private:
    std::vector<std::unique_ptr<K>> _keys;
    std::vector<std::unique_ptr<V>> _values;
    std::vector<bool> _occupied;  // Tracks if slot is occupied
    std::vector<bool> _deleted;   // Tracks if slot was deleted
    size_t _capacity;
    size_t _size;
    std::hash<K> _hashFunc;
    
    void _resize() {
        std::vector<std::unique_ptr<K>> oldKeys = std::move(_keys);
        std::vector<std::unique_ptr<V>> oldValues = std::move(_values);
        std::vector<bool> oldOccupied = std::move(_occupied);
        std::vector<bool> oldDeleted = std::move(_deleted);
        
        _capacity = _capacity * 2 + 1;
        _keys.resize(_capacity);
        _values.resize(_capacity);
        _occupied.resize(_capacity, false);
        _deleted.resize(_capacity, false);
        _size = 0;
        
        for (size_t i = 0; i < oldKeys.size(); ++i) {
            if (oldOccupied[i] && !oldDeleted[i]) {
                put(*oldKeys[i], *oldValues[i]);
            }
        }
    }
    
    size_t _hash(const K& key) const {
        return _hashFunc(key) % _capacity;
    }
    
    size_t _findSlot(const K& key) const {
        size_t index = _hash(key);
        size_t firstDeleted = _capacity;  // Use _capacity as invalid index
        
        while (_occupied[index]) {
            if (_deleted[index]) {
                if (firstDeleted == _capacity) {
                    firstDeleted = index;
                }
            } else if (*_keys[index] == key) {
                return index;
            }
            index = (index + 1) % _capacity;
        }
        
        return (firstDeleted != _capacity) ? firstDeleted : index;
    }

public:
    /**
     * @brief Hash map using open addressing with linear probing.
     * When collision occurs, linearly search for next empty slot.
     */
    explicit HashMapLinearProbing(size_t capacity = 11) : _capacity(capacity), _size(0) {
        _keys.resize(_capacity);
        _values.resize(_capacity);
        _occupied.resize(_capacity, false);
        _deleted.resize(_capacity, false);
    }

    size_t size() const {
        return _size;
    }

    bool empty() const {
        return _size == 0;
    }

    /**
     * @brief Get value by key - Average O(1), Worst O(n)
     */
    V& get(const K& key) {
        size_t index = _findSlot(key);
        if (_occupied[index] && !_deleted[index] && *_keys[index] == key) {
            return *_values[index];
        }
        throw std::out_of_range("Key not found");
    }

    /**
     * @brief Set key-value pair - Average O(1), Worst O(n)
     */
    void put(const K& key, const V& value) {
        if (static_cast<double>(_size) / _capacity > 0.5) {
            _resize();
        }
        
        size_t index = _findSlot(key);
        
        if (!_occupied[index] || _deleted[index] || *_keys[index] != key) {
            ++_size;
        }
        
        _keys[index] = std::make_unique<K>(key);
        _values[index] = std::make_unique<V>(value);
        _occupied[index] = true;
        _deleted[index] = false;
    }

    /**
     * @brief Delete key-value pair - Average O(1), Worst O(n)
     */
    void remove(const K& key) {
        size_t index = _findSlot(key);
        if (_occupied[index] && !_deleted[index] && *_keys[index] == key) {
            _deleted[index] = true;
            --_size;
        } else {
            throw std::out_of_range("Key not found");
        }
    }

    bool contains(const K& key) const {
        try {
            get(key);
            return true;
        } catch (const std::out_of_range&) {
            return false;
        }
    }

    void print() const {
        std::cout << "{";
        bool first = true;
        for (size_t i = 0; i < _capacity; ++i) {
            if (_occupied[i] && !_deleted[i]) {
                if (!first) std::cout << ", ";
                std::cout << *_keys[i] << ": " << *_values[i];
                first = false;
            }
        }
        std::cout << "}" << std::endl;
    }
};

template<typename T>
class HashSet {
private:
    HashMapChaining<T, bool> _map;

public:
    /**
     * @brief Hash set implementation - stores unique elements only.
     * Built on top of hash map, storing only keys.
     */
    explicit HashSet(size_t capacity = 11) : _map(capacity) {}

    size_t size() const {
        return _map.size();
    }

    /**
     * @brief Add element to set - O(1) average
     */
    void add(const T& element) {
        _map.put(element, true);
    }

    /**
     * @brief Remove element from set - O(1) average
     */
    void remove(const T& element) {
        _map.remove(element);
    }

    /**
     * @brief Check if element exists - O(1) average
     */
    bool contains(const T& element) const {
        return _map.contains(element);
    }

    void print() const {
        std::cout << "{";
        auto keys = _map.keys();
        for (size_t i = 0; i < keys.size(); ++i) {
            if (i > 0) std::cout << ", ";
            std::cout << keys[i];
        }
        std::cout << "}" << std::endl;
    }
};

// Example usage
#ifndef SKIP_STANDALONE_MAIN
int main() {
    std::cout << "=== Hash Map with Chaining Demo ===" << std::endl;
    HashMapChaining<std::string, int> hashMap;

    // Insert key-value pairs
    hashMap.put("apple", 5);
    hashMap.put("banana", 7);
    hashMap.put("orange", 3);
    hashMap.put("grape", 12);
    std::cout << "Hash map: ";
    hashMap.print();
    std::cout << "Size: " << hashMap.size() << std::endl;

    // Access values
    std::cout << "apple: " << hashMap.get("apple") << std::endl;
    std::cout << "grape: " << hashMap.get("grape") << std::endl;

    // Update value
    hashMap.put("apple", 10);
    std::cout << "After update: ";
    hashMap.print();

    // Check existence
    std::cout << "'banana' in map: " << (hashMap.contains("banana") ? "true" : "false") << std::endl;
    std::cout << "'mango' in map: " << (hashMap.contains("mango") ? "true" : "false") << std::endl;

    // Delete entry
    hashMap.remove("orange");
    std::cout << "After deleting 'orange': ";
    hashMap.print();

    // Iterate
    auto keys = hashMap.keys();
    std::cout << "Keys: {";
    for (size_t i = 0; i < keys.size(); ++i) {
        if (i > 0) std::cout << ", ";
        std::cout << keys[i];
    }
    std::cout << "}" << std::endl;

    auto values = hashMap.values();
    std::cout << "Values: {";
    for (size_t i = 0; i < values.size(); ++i) {
        if (i > 0) std::cout << ", ";
        std::cout << values[i];
    }
    std::cout << "}" << std::endl;

    std::cout << "\n=== Hash Map with Linear Probing Demo ===" << std::endl;
    HashMapLinearProbing<std::string, int> lpMap;

    lpMap.put("one", 1);
    lpMap.put("two", 2);
    lpMap.put("three", 3);
    std::cout << "Linear probing map: ";
    lpMap.print();

    std::cout << "\n=== Hash Set Demo ===" << std::endl;
    HashSet<int> hashSet;

    // Add elements
    std::vector<int> nums = {1, 2, 3, 2, 4, 3, 5};
    for (int num : nums) {
        hashSet.add(num);
    }
    std::cout << "Set (duplicates removed): ";
    hashSet.print();

    // Check membership
    std::cout << "3 in set: " << (hashSet.contains(3) ? "true" : "false") << std::endl;
    std::cout << "10 in set: " << (hashSet.contains(10) ? "true" : "false") << std::endl;

    // Remove element
    hashSet.remove(2);
    std::cout << "After removing 2: ";
    hashSet.print();

    return 0;
}
#endif // SKIP_STANDALONE_MAIN
