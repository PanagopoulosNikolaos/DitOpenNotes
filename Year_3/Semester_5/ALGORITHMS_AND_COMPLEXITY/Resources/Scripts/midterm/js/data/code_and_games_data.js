(function (global_scope) {
  'use strict';

  /**
   * Builds Python code examples, Drop-In puzzles, and True/False drills for Prerequisites and Units 00-07.
   *
   * Returns:
   *     object: Bundle containing code_examples, dropin_puzzles, and true_false_drills maps.
   */
  function buildCodeAndGamesBundle() {
    const code_examples = {
      prereq: [
        {
          title: 'Βασικές Συναρτήσεις Επανάληψης (Λογάριθμος & Τριγωνικό Άθροισμα)',
          source_tag: 'Προαπαιτούμενα — Εργαλεία Ανάλυσης',
          complexity: 'O(log n) vs Θ(n^2)',
          code: [
            'def countHalvings(initial_size: int) -> int:',
            '    """Counts how many integer halvings reduce initial_size to 1.',
            '',
            '    Args:',
            '        initial_size (int): Positive starting input size.',
            '',
            '    Returns:',
            '        int: Number of halving steps (floor(log2(initial_size))).',
            '    """',
            '    halving_steps = 0',
            '    remaining_size = initial_size',
            '    while remaining_size > 1:',
            '        remaining_size //= 2  # Integer floor division cuts problem size in half.',
            '        halving_steps += 1',
            '    return halving_steps',
            '',
            'def computeTriangularSum(limit_count: int) -> int:',
            '    """Computes 1 + 2 + ... + limit_count in O(1) using closed form.',
            '',
            '    Args:',
            '        limit_count (int): Non-negative upper integer limit.',
            '',
            '    Returns:',
            '        int: Exact arithmetic series sum.',
            '    """',
            '    return limit_count * (limit_count + 1) // 2'
          ].join('\n')
        }
      ],
      '00': [
        {
          title: 'Επιλογή Στρατηγικής Προόδου (Strategy Chooser)',
          source_tag: 'Σημείωση 00 — Ενότητα 3.3',
          complexity: 'Οδηγός Απόφασης Προόδου',
          code: [
            'def chooseMidtermStrategy(problem_category: str, constraint_key: str) -> str:',
            '    """Maps a Midterm exam problem specification to the optimal strategy.',
            '',
            '    Args:',
            '        problem_category (str): Category such as "sets", "sort", or "optimization".',
            '        constraint_key (str): Key constraint from the problem statement.',
            '',
            '    Returns:',
            '        str: Recommended algorithm or data structure with case bound.',
            '    """',
            '    if problem_category == "sets":',
            '        if constraint_key == "min_extract":',
            '            return "Binary Heap: O(log n) worst, Bottom-Up O(n)"',
            '        if constraint_key == "worst_o1_lookup":',
            '            return "Cuckoo Hashing: O(1) worst get/remove"',
            '        if constraint_key == "disjoint_union":',
            '            return "Union-Find: O((n + m) * alpha(n))"',
            '    if problem_category == "sort":',
            '        if constraint_key == "disk_sequential":',
            '            return "Merge-Sort: O(n log n) worst, O(n) space"',
            '        return "inPlaceQuickSort: O(n log n) expected"',
            '    return "Greedy (exchange proof) or Divide & Conquer (Master Theorem)"'
          ].join('\n')
        },
        {
          title: 'Επαλήθευση Διπλασιασμού Επτά Συναρτήσεων',
          source_tag: 'Σημείωση 00 — Ενότητα 2.4',
          complexity: '1 < log n < n < n log n < n^2 < n^3 < 2^n',
          code: [
            'import math',
            '',
            'def compareGrowthRates(input_size: int) -> dict[str, float]:',
            '    """Computes the seven core growth rates for input_size.',
            '',
            '    Args:',
            '        input_size (int): Input size (input_size >= 2).',
            '',
            '    Returns:',
            '        dict[str, float]: Growth values for each complexity class.',
            '    """',
            '    log2_size = math.log2(input_size)',
            '    return {',
            '        "constant": 1.0,',
            '        "log_n": log2_size,',
            '        "linear": float(input_size),',
            '        "n_log_n": input_size * log2_size,',
            '        "quadratic": float(input_size ** 2),',
            '        "cubic": float(input_size ** 3),',
            '        "exponential": float(2 ** min(input_size, 30))  # Caps exponent to avoid overflow.',
            '    }'
          ].join('\n')
        }
      ],
      '01': [
        {
          title: 'Αντιστροφή Πίνακα Επί-Τόπου σε O(1) Χώρο',
          source_tag: 'Φροντιστήριο A — Κεφ. 1 #10',
          complexity: 'Θ(n) χρόνος, O(1) επιπλέον χώρος',
          code: [
            'def reverseInPlace(numbers: list[int]) -> list[int]:',
            '    """Reverses a list in place using constant auxiliary space.',
            '',
            '    Args:',
            '        numbers (list[int]): Mutable sequence of integers.',
            '',
            '    Returns:',
            '        list[int]: The same list reversed in place.',
            '    """',
            '    total_count = len(numbers)',
            '    for left_index in range(total_count // 2):',
            '        right_index = total_count - 1 - left_index',
            '        # Swaps symmetric endpoints without allocating a second array.',
            '        numbers[left_index], numbers[right_index] = numbers[right_index], numbers[left_index]',
            '    return numbers'
          ].join('\n')
        },
        {
          title: 'Μέγιστο Άθροισμα Υπο-Πίνακα: MaxsubFastest',
          source_tag: 'Σημείωση 01 — Ενότητα 3.3',
          complexity: 'O(n) χειρότερη περίπτωση',
          code: [
            'def maxsubFastest(numbers: list[int]) -> int:',
            '    """Finds maximum contiguous subarray sum using Kadane suffix recurrence.',
            '',
            '    Args:',
            '        numbers (list[int]): Input sequence of integers.',
            '',
            '    Returns:',
            '        int: Maximum subarray sum (0 for empty subarray).',
            '    """',
            '    current_suffix_sum = 0',
            '    max_subarray_sum = 0',
            '    for current_value in numbers:',
            '        # Resets negative suffix to 0 because negative prefix never helps.',
            '        current_suffix_sum = max(0, current_suffix_sum + current_value)',
            '        max_subarray_sum = max(max_subarray_sum, current_suffix_sum)',
            '    return max_subarray_sum'
          ].join('\n')
        }
      ],
      '02': [
        {
          title: 'Εξαγωγή 10 Μικρότερων Τιμών με Δυαδικό Σωρό',
          source_tag: 'Φροντιστήριο A — Κεφ. 5 #7 & #3',
          complexity: 'O(n + k log n) χειρότερη',
          code: [
            'import heapq',
            '',
            'def extractSmallestKeys(input_keys: list[int], smallest_count: int) -> list[int]:',
            '    """Extracts the smallest_count minimum keys via O(n) heapify and k pops.',
            '',
            '    Args:',
            '        input_keys (list[int]): Unsorted list of integer keys.',
            '        smallest_count (int): Number of smallest keys to extract.',
            '',
            '    Returns:',
            '        list[int]: Ascending list of the smallest_count minimum keys.',
            '    """',
            '    min_heap = list(input_keys)',
            '    heapq.heapify(min_heap)  # Bottom-up construction runs in O(n) time.',
            '    smallest_keys = []',
            '    for _ in range(min(smallest_count, len(min_heap))):',
            '        smallest_keys.append(heapq.heappop(min_heap))',
            '    return smallest_keys'
          ].join('\n')
        },
        {
          title: '1-Indexed ArrayHeap (upheap & downheap)',
          source_tag: 'Σημείωση 02 — Ενότητες 3.2 & 3.3',
          complexity: 'insert / removeMin: O(log n) χειρότερη',
          code: [
            'class ArrayHeap:',
            '    """1-indexed binary min-heap implementing textbook array layout.',
            '',
            '    Attributes:',
            '        heap_array (list): Internal 1-indexed array with sentinel None at index 0.',
            '    """',
            '',
            '    def __init__(self) -> None:',
            '        """Initializes an empty 1-indexed heap with sentinel at index 0."""',
            '        self.heap_array = [None]',
            '',
            '    def insertKey(self, new_key: int) -> None:',
            '        """Inserts new_key at end and restores heap order via upheap."""',
            '        self.heap_array.append(new_key)',
            '        child_index = len(self.heap_array) - 1',
            '        while child_index > 1 and self.heap_array[child_index // 2] > self.heap_array[child_index]:',
            '            parent_index = child_index // 2',
            '            self.heap_array[parent_index], self.heap_array[child_index] = (',
            '                self.heap_array[child_index],',
            '                self.heap_array[parent_index]',
            '            )',
            '            child_index = parent_index'
          ].join('\n')
        }
      ],
      '03': [
        {
          title: 'Έλεγχος Ξένων Ακολουθιών με Σύνολο Κατακερματισμού',
          source_tag: 'Φροντιστήριο A — Κεφ. 6 #6',
          complexity: 'O(M + N) αναμενόμενη (hash set στη μικρότερη Μ)',
          code: [
            'def areDisjoint(smaller_sequence: list[int], larger_sequence: list[int]) -> bool:',
            '    """Checks whether two sequences share no common element.',
            '',
            '    Args:',
            '        smaller_sequence (list[int]): Shorter sequence of length M.',
            '        larger_sequence (list[int]): Longer sequence of length N (M << N).',
            '',
            '    Returns:',
            '        bool: True if disjoint, False if any common element exists.',
            '    """',
            '    # Hashes the smaller sequence so hash-table space stays O(M).',
            '    smaller_lookup_set = set(smaller_sequence)',
            '    for element in larger_sequence:',
            '        if element in smaller_lookup_set:',
            '            return False',
            '    return True'
          ].join('\n')
        },
        {
          title: 'Κώδικας Κατακερματισμού με Κανόνα Horner (z = 33)',
          source_tag: 'Σημείωση 03 — Ενότητα 3.2',
          complexity: 'Θ(n) χειρότερη (n = μήκος συμβολοσειράς)',
          code: [
            'def polynomialHashCode(input_word: str, polynomial_base: int = 33) -> int:',
            '    """Computes polynomial hash code of a string via Horner rule.',
            '',
            '    Args:',
            '        input_word (str): Input character string.',
            '        polynomial_base (int): Polynomial base (33 = 32 + 1 for fast shift-add).',
            '',
            '    Returns:',
            '        int: Integer hash code h1 before compression.',
            '    """',
            '    hash_accumulator = 0',
            '    for character in input_word:',
            '        hash_accumulator = hash_accumulator * polynomial_base + ord(character)',
            '    return hash_accumulator'
          ].join('\n')
        }
      ],
      '04': [
        {
          title: 'Δεντρικό Union-Find (Μέγεθος + Συμπίεση Διαδρομής)',
          source_tag: 'Σημείωση 04 — Ενότητα 3.2',
          complexity: 'O((n + m) α(n)) χειρότερη / επιμερισμένη',
          code: [
            'class UnionFind:',
            '    """Disjoint-set structure with union-by-size and path compression."""',
            '',
            '    def __init__(self, element_count: int) -> None:',
            '        """Initializes element_count singleton sets indexed 0..element_count-1."""',
            '        self.parent_links = list(range(element_count))',
            '        self.subtree_sizes = [1] * element_count',
            '',
            '    def findRoot(self, node_id: int) -> int:',
            '        """Finds representative root and compresses traversed path."""',
            '        if self.parent_links[node_id] != node_id:',
            '            # Redirects every visited node directly to root on unwind.',
            '            self.parent_links[node_id] = self.findRoot(self.parent_links[node_id])',
            '        return self.parent_links[node_id]',
            '',
            '    def unionSets(self, first_node: int, second_node: int) -> bool:',
            '        """Unites sets containing first_node and second_node by attaching smaller tree."""',
            '        first_root = self.findRoot(first_node)',
            '        second_root = self.findRoot(second_node)',
            '        if first_root == second_root:',
            '            return False',
            '        if self.subtree_sizes[first_root] < self.subtree_sizes[second_root]:',
            '            first_root, second_root = second_root, first_root',
            '        self.parent_links[second_root] = first_root',
            '        self.subtree_sizes[first_root] += self.subtree_sizes[second_root]',
            '        return True'
          ].join('\n')
        },
        {
          title: 'Ομάδες Φιλίας με Union-Find',
          source_tag: 'Φροντιστήριο A — Κεφ. 7 #4',
          complexity: 'O((n + m) α(n)) χειρότερη',
          code: [
            'def findFriendGroups(user_count: int, friendships: list[list[int]]) -> dict[int, list[int]]:',
            '    """Partitions users into connected friendship components.',
            '',
            '    Args:',
            '        user_count (int): Total number of users indexed 0..user_count-1.',
            '        friendships (list[list[int]]): Pairs [first_user, second_user] representing edges.',
            '',
            '    Returns:',
            '        dict[int, list[int]]: Components keyed by root representative.',
            '    """',
            '    union_find = UnionFind(user_count)',
            '    for first_user, second_user in friendships:',
            '        union_find.unionSets(first_user, second_user)',
            '    friend_groups: dict[int, list[int]] = {}',
            '    for person_id in range(user_count):',
            '        group_root = union_find.findRoot(person_id)',
            '        friend_groups.setdefault(group_root, []).append(person_id)',
            '    return friend_groups'
          ].join('\n')
        }
      ],
      '05': [
        {
          title: 'Συγχώνευση των N Μικρότερων Στοιχείων από 2 Ταξινομημένους Πίνακες',
          source_tag: 'Φροντιστήριο A — Κεφ. 8 #6',
          complexity: 'O(N) χειρότερη',
          code: [
            'def mergeSmallestN(first_sorted: list[int], second_sorted: list[int], target_count: int) -> list[int]:',
            '    """Merges two sorted arrays and returns the smallest target_count values in O(N).',
            '',
            '    Args:',
            '        first_sorted (list[int]): First ascending sorted array.',
            '        second_sorted (list[int]): Second ascending sorted array.',
            '        target_count (int): Count of smallest elements to return.',
            '',
            '    Returns:',
            '        list[int]: Sorted list of the target_count smallest elements.',
            '    """',
            '    merged_result = [0] * target_count',
            '    first_index = 0',
            '    second_index = 0',
            '    for output_index in range(target_count):',
            '        if first_sorted[first_index] <= second_sorted[second_index]:',
            '            merged_result[output_index] = first_sorted[first_index]',
            '            first_index += 1',
            '        else:',
            '            merged_result[output_index] = second_sorted[second_index]',
            '            second_index += 1',
            '    return merged_result'
          ].join('\n')
        },
        {
          title: 'Επί-Τόπου Διαμερισμός (inPlacePartition)',
          source_tag: 'Σημείωση 05 — Ενότητα 3.3',
          complexity: 'O(r - l + 1) ανά κλήση, O(n log n) αναμενόμενη',
          code: [
            'def inPlacePartition(array: list[int], left_bound: int, right_bound: int) -> tuple[int, int]:',
            '    """Partitions array[left_bound..right_bound] around pivot array[right_bound] in place.',
            '',
            '    Args:',
            '        array (list[int]): Target array modified in place.',
            '        left_bound (int): Left inclusive boundary.',
            '        right_bound (int): Right inclusive boundary (pivot index).',
            '',
            '    Returns:',
            '        tuple[int, int]: Boundaries (equal_start, equal_end) of equal-pivot block.',
            '    """',
            '    pivot_value = array[right_bound]',
            '    scan_left, scan_right = left_bound, right_bound - 1',
            '    while scan_left <= scan_right:',
            '        while scan_left <= scan_right and array[scan_left] < pivot_value:',
            '            scan_left += 1',
            '        while scan_right >= scan_left and array[scan_right] >= pivot_value:',
            '            scan_right -= 1',
            '        if scan_left < scan_right:',
            '            array[scan_left], array[scan_right] = array[scan_right], array[scan_left]',
            '            scan_left += 1',
            '            scan_right -= 1',
            '    equal_start = scan_left',
            '    # Places pivot equal block into array[equal_start..pivot_scan_right].',
            '    pivot_scan_left, pivot_scan_right = equal_start, right_bound',
            '    while pivot_scan_left <= pivot_scan_right:',
            '        while pivot_scan_left <= pivot_scan_right and array[pivot_scan_left] == pivot_value:',
            '            pivot_scan_left += 1',
            '        while pivot_scan_right >= pivot_scan_left and array[pivot_scan_right] > pivot_value:',
            '            pivot_scan_right -= 1',
            '        if pivot_scan_left < pivot_scan_right:',
            '            array[pivot_scan_left], array[pivot_scan_right] = array[pivot_scan_right], array[pivot_scan_left]',
            '    return equal_start, pivot_scan_right'
          ].join('\n')
        }
      ],
      '06': [
        {
          title: 'Κλασματικό Πρόβλημα Σακιδίου (fractionalKnapsack)',
          source_tag: 'Φροντιστήριο A — Κεφ. 10 #3 & Σημείωση 06',
          complexity: 'O(n log n) χειρότερη',
          code: [
            'def fractionalKnapsack(items: list[dict], total_capacity: float) -> float:',
            '    """Maximizes total benefit for divisible items via greedy density sort.',
            '',
            '    Args:',
            '        items (list[dict]): Items with "weight" and "benefit" keys.',
            '        total_capacity (float): Total knapsack weight limit.',
            '',
            '    Returns:',
            '        float: Globally optimal total benefit.',
            '    """',
            '    ordered_items = sorted(items, key=lambda item: item["benefit"] / item["weight"], reverse=True)',
            '    total_benefit = 0.0',
            '    remaining_capacity = total_capacity',
            '    for item in ordered_items:',
            '        if remaining_capacity <= 0:',
            '            break',
            '        taken_weight = min(item["weight"], remaining_capacity)',
            '        total_benefit += taken_weight * (item["benefit"] / item["weight"])',
            '        remaining_capacity -= taken_weight',
            '    return total_benefit'
          ].join('\n')
        },
        {
          title: 'Ελάχιστες Μηχανές Χρονοπρογραμματισμού (Min-Heap)',
          source_tag: 'Φροντιστήριο A — Κεφ. 10 #4 & Σημείωση 06',
          complexity: 'O(n log n) χειρότερη',
          code: [
            'import heapq',
            '',
            'def scheduleMinMachines(tasks: list[tuple[int, int]]) -> int:',
            '    """Assigns all tasks (start_time, finish_time) to minimum non-conflicting machines.',
            '',
            '    Args:',
            '        tasks (list[tuple[int, int]]): Intervals (start_time, finish_time).',
            '',
            '    Returns:',
            '        int: Minimum number of machines required.',
            '    """',
            '    # Sorts strictly by ascending start_time s_i (never by finish_time f_i).',
            '    sorted_tasks = sorted(tasks, key=lambda task: task[0])',
            '    machine_finishes: list[int] = []',
            '    for start_time, finish_time in sorted_tasks:',
            '        if machine_finishes and machine_finishes[0] <= start_time:',
            '            heapq.heapreplace(machine_finishes, finish_time)',
            '        else:',
            '            heapq.heappush(machine_finishes, finish_time)',
            '    return len(machine_finishes)'
          ].join('\n')
        }
      ],
      '07': [
        {
          title: 'Γραμμική Συγχώνευση Δύο Ταξινομημένων Λιστών',
          source_tag: 'Φροντιστήριο B — Κεφ. 11 #4',
          complexity: 'Θ(n1 + n2) χειρότερη',
          code: [
            'def mergeSorted(first_sorted: list[int], second_sorted: list[int]) -> list[int]:',
            '    """Merges two sorted lists into a single sorted list in linear time.',
            '',
            '    Args:',
            '        first_sorted (list[int]): First ascending sorted list.',
            '        second_sorted (list[int]): Second ascending sorted list.',
            '',
            '    Returns:',
            '        list[int]: Combined ascending sorted list.',
            '    """',
            '    merged_list: list[int] = []',
            '    first_index, second_index = 0, 0',
            '    while first_index < len(first_sorted) and second_index < len(second_sorted):',
            '        if first_sorted[first_index] <= second_sorted[second_index]:',
            '            merged_list.append(first_sorted[first_index])',
            '            first_index += 1',
            '        else:',
            '            merged_list.append(second_sorted[second_index])',
            '            second_index += 1',
            '    return merged_list + first_sorted[first_index:] + second_sorted[second_index:]'
          ].join('\n')
        },
        {
          title: 'Πολλαπλασιασμός Karatsuba (3 Αναδρομές)',
          source_tag: 'Σημείωση 07 — Ενότητα 3.1',
          complexity: 'Θ(n^{log_2 3}) ~ Θ(n^1.585)',
          code: [
            'def karatsuba(first_number: int, second_number: int, base: int = 10) -> int:',
            '    """Multiplies two integers using 3 recursive sub-products.',
            '',
            '    Args:',
            '        first_number (int): First non-negative integer.',
            '        second_number (int): Second non-negative integer.',
            '        base (int): Positional base (10 or 2).',
            '',
            '    Returns:',
            '        int: Exact integer product first_number * second_number.',
            '    """',
            '    if first_number < base or second_number < base:',
            '        return first_number * second_number',
            '    half_digits = max(len(str(first_number)), len(str(second_number))) // 2',
            '    split_power = base ** half_digits',
            '    first_high, first_low = divmod(first_number, split_power)',
            '    second_high, second_low = divmod(second_number, split_power)',
            '    high_product = karatsuba(first_high, second_high, base)',
            '    low_product = karatsuba(first_low, second_low, base)',
            '    diff_product = karatsuba(first_high - first_low, second_low - second_high, base)',
            '    middle_term = diff_product + high_product + low_product',
            '    return high_product * (split_power ** 2) + middle_term * split_power + low_product'
          ].join('\n')
        }
      ]
    };

    const dropin_puzzles = {
      '00': [
        {
          id: 'drop_00_1',
          unit_id: '00',
          title: 'Συμπλήρωση Κώδικα: Επιλογέας Στρατηγικής Προόδου',
          source_tag: 'Σημείωση 00 — Strategy Chooser',
          description: 'Τοποθετήστε τις σωστές δομές και αλγορίθμους στα κενά ώστε η συνάρτηση να αντιστοιχίζει τις απαιτήσεις Προόδου.',
          lines: [
            'def pickStructure(requirement: str) -> str:',
            '    if requirement == "worst_o1_get_remove":',
            '        return {{s0}}',
            '    if requirement == "disk_over_1m_stable":',
            '        return {{s1}}',
            '    if requirement == "dynamic_connected_components":',
            '        return {{s2}}',
            '    return {{s3}}'
          ],
          slots: {
            s0: { label: 'O(1) χειρότερη αναζήτηση', expected: 't_cuckoo', hint: 'Μόνο μία δομή κατακερματισμού εγγυάται O(1) χειρότερη στην αναζήτηση.' },
            s1: { label: 'ταξινόμηση δίσκου >1M', expected: 't_merge', hint: 'Σειριακή προσπέλαση σε δίσκο + σταθερότητα + O(n log n) χειρότερη.' },
            s2: { label: 'δυναμικές συνιστώσες', expected: 't_uf', hint: 'Διαχείριση ξένων συνόλων με ένωση κατά μέγεθος & συμπίεση διαδρομής.' },
            s3: { label: 'συνεχής εξαγωγή ελαχίστου', expected: 't_heap', hint: 'Συνεχής εξαγωγή ελάχιστου κλειδιού σε O(log n) χειρότερη.' }
          },
          tokens: [
            { id: 't_cuckoo', label: '"Cuckoo Hashing"' },
            { id: 't_merge', label: '"Merge-Sort"' },
            { id: 't_uf', label: '"Union-Find"' },
            { id: 't_heap', label: '"Binary Heap"' },
            { id: 't_d1', label: '"Linear Probing"' },
            { id: 't_d2', label: '"Quick-Sort"' }
          ]
        }
      ],
      '01': [
        {
          id: 'drop_01_1',
          unit_id: '01',
          title: 'Drop-In #1: Αντιστροφή Ακολουθίας σε Χώρο O(1)',
          source_tag: 'Φροντιστήριο A — Κεφ. 1 #10',
          description: 'Συμπληρώστε το όριο του βρόχου και τον συμμετρικό δείκτη ώστε ο αλγόριθμος να αντιστρέφει τη λίστα numbers επί-τόπου.',
          lines: [
            'def reverseInPlace(numbers: list[int]) -> list[int]:',
            '    total_count = len(numbers)',
            '    for left_index in range({{s0}}):',
            '        right_index = {{s1}}',
            '        numbers[left_index], numbers[right_index] = {{s2}}',
            '    return numbers'
          ],
          slots: {
            s0: { label: 'όριο επαναλήψεων', expected: 't_half', hint: 'Αν διατρέξουμε όλο το total_count, θα αντιστραφούν τα στοιχεία δύο φορές!' },
            s1: { label: 'συμμετρικός δείκτης', expected: 't_mirror', hint: 'Ο συμμετρικός δείκτης του left_index ξεκινώντας από το τέλος total_count - 1.' },
            s2: { label: 'ανταλλαγή τιμών', expected: 't_swap', hint: 'Ανταλλαγή των στοιχείων στις θέσεις left_index και right_index.' }
          },
          tokens: [
            { id: 't_half', label: 'total_count // 2' },
            { id: 't_mirror', label: 'total_count - 1 - left_index' },
            { id: 't_swap', label: 'numbers[right_index], numbers[left_index]' },
            { id: 't_d1', label: 'total_count' },
            { id: 't_d2', label: 'total_count - left_index' }
          ]
        },
        {
          id: 'drop_01_2',
          unit_id: '01',
          title: 'Drop-In #2: Αναδρομική Σχέση MaxsubFastest',
          source_tag: 'Σημείωση 01 — Ενότητα 3.3',
          description: 'Συμπληρώστε την ενημέρωση του τρέχοντος επιθεματικού αθροίσματος (current_suffix_sum) και του καθολικού μεγίστου (max_subarray_sum).',
          lines: [
            'def maxsubFastest(numbers: list[int]) -> int:',
            '    current_suffix_sum = 0',
            '    max_subarray_sum = 0',
            '    for current_value in numbers:',
            '        current_suffix_sum = {{s0}}',
            '        max_subarray_sum = {{s1}}',
            '    return max_subarray_sum'
          ],
          slots: {
            s0: { label: 'νέο επίθεμα M_t', expected: 't_mt', hint: 'Αν το επίθεμα γίνει αρνητικό, το μηδενίζουμε (max(0, current_suffix_sum + current_value)).' },
            s1: { label: 'μέγιστο m', expected: 't_best', hint: 'Ενημερώνουμε το μέγιστο άθροισμα που είδαμε μέχρι τώρα.' }
          },
          tokens: [
            { id: 't_mt', label: 'max(0, current_suffix_sum + current_value)' },
            { id: 't_best', label: 'max(max_subarray_sum, current_suffix_sum)' },
            { id: 't_d1', label: 'current_suffix_sum + current_value' },
            { id: 't_d2', label: 'min(0, current_suffix_sum + current_value)' }
          ]
        }
      ],
      '02': [
        {
          id: 'drop_02_1',
          unit_id: '02',
          title: 'Drop-In #1: Εξαγωγή k Μικρότερων Στοιχείων με Σωρό',
          source_tag: 'Φροντιστήριο A — Κεφ. 5 #7',
          description: 'Οργανώστε τη λίστα input_keys σε σωρό ελαχίστων σε χρόνο O(n) και εξαγάγετε τα smallest_count μικρότερα στοιχεία.',
          lines: [
            'import heapq',
            'def extractSmallestKeys(input_keys: list[int], smallest_count: int) -> list[int]:',
            '    {{s0}}',
            '    smallest_keys = []',
            '    for _ in range(smallest_count):',
            '        smallest_keys.append({{s1}})',
            '    return smallest_keys'
          ],
          slots: {
            s0: { label: 'κατασκευή σωρού O(n)', expected: 't_heapify', hint: 'Bottom-up μετατροπή της λίστας σε σωρό επί-τόπου.' },
            s1: { label: 'εξαγωγή ελαχίστου', expected: 't_pop', hint: 'Αφαίρεση και επιστροφή της ελάχιστης ρίζας σε O(log n).' }
          },
          tokens: [
            { id: 't_heapify', label: 'heapq.heapify(input_keys)' },
            { id: 't_pop', label: 'heapq.heappop(input_keys)' },
            { id: 't_d1', label: 'input_keys.sort()' },
            { id: 't_d2', label: 'input_keys.pop()' }
          ]
        },
        {
          id: 'drop_02_2',
          unit_id: '02',
          title: 'Drop-In #2: Επιλογή Μικρότερου Παιδιού στο downheap (1-indexed)',
          source_tag: 'Σημείωση 02 — Ενότητα 3.3',
          description: 'Συμπληρώστε τους 1-indexed τύπους παιδιών και τη σύγκριση ώστε το downheap να επιλέγει πάντα το μικρότερο παιδί.',
          lines: [
            'def chooseSmallerChildIndex(heap_array: list[int], parent_index: int, heap_size: int) -> int:',
            '    left_child_index = {{s0}}',
            '    right_child_index = {{s1}}',
            '    smaller_child_index = left_child_index',
            '    if right_child_index <= heap_size and {{s2}}:',
            '        smaller_child_index = right_child_index',
            '    return smaller_child_index'
          ],
          slots: {
            s0: { label: 'αριστερό παιδί', expected: 't_left', hint: '1-indexed τύπος αριστερού παιδιού.' },
            s1: { label: 'δεξιό παιδί', expected: 't_right', hint: '1-indexed τύπος δεξιού παιδιού.' },
            s2: { label: 'έλεγχος μικρότερου παιδιού', expected: 't_cmp', hint: 'Επιλέγουμε το δεξιό παιδί μόνο αν είναι αυστηρά μικρότερο από το αριστερό.' }
          },
          tokens: [
            { id: 't_left', label: '2 * parent_index' },
            { id: 't_right', label: '2 * parent_index + 1' },
            { id: 't_cmp', label: 'heap_array[right_child_index] < heap_array[left_child_index]' },
            { id: 't_d1', label: '2 * parent_index + 2' },
            { id: 't_d2', label: 'heap_array[right_child_index] > heap_array[left_child_index]' }
          ]
        }
      ],
      '03': [
        {
          id: 'drop_03_1',
          unit_id: '03',
          title: 'Drop-In #1: Έλεγχος Ξένων Ακολουθιών (Μικρότερη M << Μεγαλύτερη N)',
          source_tag: 'Φροντιστήριο A — Κεφ. 6 #6',
          description: 'Επιλέξτε τη μικρότερη ακολουθία (smaller_sequence, μήκους M) για μετατροπή σε σύνολο κατακερματισμού ώστε η μνήμη του set να είναι O(M), και σαρώστε τη larger_sequence (μήκους N).',
          lines: [
            'def areDisjoint(smaller_sequence: list[int], larger_sequence: list[int]) -> bool:',
            '    smaller_lookup_set = {{s0}}',
            '    for element in {{s1}}:',
            '        if {{s2}}:',
            '            return False',
            '    return True'
          ],
          slots: {
            s0: { label: 'set της μικρότερης (O(M))', expected: 't_setm', hint: 'Μετατρέπουμε σε set τη ΜΙΚΡΟΤΕΡΗ ακολουθία (smaller_sequence).' },
            s1: { label: 'σάρωση μεγαλύτερης (O(N))', expected: 't_seqn', hint: 'Σαρώνουμε τα N στοιχεία της larger_sequence σε O(1) αναμενόμενα ανά έλεγχο.' },
            s2: { label: 'έλεγχος κοινού στοιχείου', expected: 't_in', hint: 'Ελέγχουμε αν το element υπάρχει μέσα στο smaller_lookup_set.' }
          },
          tokens: [
            { id: 't_setm', label: 'set(smaller_sequence)' },
            { id: 't_seqn', label: 'larger_sequence' },
            { id: 't_in', label: 'element in smaller_lookup_set' },
            { id: 't_d1', label: 'set(larger_sequence)' },
            { id: 't_d2', label: 'smaller_sequence' }
          ]
        },
        {
          id: 'drop_03_2',
          unit_id: '03',
          title: 'Drop-In #2: Αναζήτηση με DEFUNCT στη Γραμμική Ανίχνευση',
          source_tag: 'Σημείωση 03 — Ενότητα 3.3',
          description: 'Χειριστείτε σωστά τα κενά κελιά και τους δείκτες DEFUNCT κατά τη σάρωση γραμμικής ανίχνευσης.',
          lines: [
            'def probeFind(hash_table: list, target_key: int, table_capacity: int) -> int:',
            '    for probe_step in range(table_capacity):',
            '        slot_index = {{s0}}',
            '        if hash_table[slot_index] is None:',
            '            {{s1}}',
            '        if hash_table[slot_index] != "DEFUNCT" and hash_table[slot_index] == target_key:',
            '            return slot_index',
            '    return -1'
          ],
          slots: {
            s0: { label: 'δείκτης γραμμικής ανίχνευσης', expected: 't_lp', hint: 'Βήμα γραμμικής ανίχνευσης modulo χωρητικότητα table_capacity.' },
            s1: { label: 'τερματισμός σε κενό κελί', expected: 't_stop', hint: 'Μόνο ένα πραγματικά κενό (None) τερματίζει την αναζήτηση· το DEFUNCT προσπερνάται.' }
          },
          tokens: [
            { id: 't_lp', label: '((target_key % table_capacity) + probe_step) % table_capacity' },
            { id: 't_stop', label: 'return -1' },
            { id: 't_d1', label: 'continue' },
            { id: 't_d2', label: '(target_key + probe_step * probe_step) % table_capacity' }
          ]
        }
      ],
      '04': [
        {
          id: 'drop_04_1',
          unit_id: '04',
          title: 'Drop-In #1: Συμπίεση Διαδρομής (findRoot)',
          source_tag: 'Σημείωση 04 — Ενότητα 3.2',
          description: 'Συμπληρώστε τη συνθήκη βάσης και την ανακατεύθυνση γονέα στη ρίζα για τη Συμπίεση Διαδρομής.',
          lines: [
            'def findRoot(parent_links: list[int], node_id: int) -> int:',
            '    if {{s0}}:',
            '        return node_id',
            '    {{s1}} = findRoot(parent_links, parent_links[node_id])',
            '    return parent_links[node_id]'
          ],
          slots: {
            s0: { label: 'συνθήκη ρίζας', expected: 't_root', hint: 'Μία ρίζα έχει δείκτη γονέα στον εαυτό της.' },
            s1: { label: 'συμπίεση γονέα', expected: 't_comp', hint: 'Αποθηκεύουμε την επιστρεφόμενη ρίζα απευθείας στο parent_links[node_id].' }
          },
          tokens: [
            { id: 't_root', label: 'parent_links[node_id] == node_id' },
            { id: 't_comp', label: 'parent_links[node_id]' },
            { id: 't_d1', label: 'parent_links[node_id] == 0' },
            { id: 't_d2', label: 'subtree_sizes[node_id]' }
          ]
        },
        {
          id: 'drop_04_2',
          unit_id: '04',
          title: 'Drop-In #2: Ένωση κατά Μέγεθος (Union by Size)',
          source_tag: 'Σημείωση 04 — Ενότητα 3.2',
          description: 'Προσαρτήστε τη μικρότερη ρίζα (second_root) κάτω από τη μεγαλύτερη (first_root) και ενημερώστε το μέγεθος μόνο της νέας ρίζας.',
          lines: [
            'def unionBySize(parent_links: list[int], subtree_sizes: list[int], first_node: int, second_node: int) -> None:',
            '    first_root, second_root = findRoot(parent_links, first_node), findRoot(parent_links, second_node)',
            '    if {{s0}}:',
            '        return',
            '    if subtree_sizes[first_root] < subtree_sizes[second_root]:',
            '        first_root, second_root = second_root, first_root',
            '    {{s1}}',
            '    subtree_sizes[first_root] += subtree_sizes[second_root]'
          ],
          slots: {
            s0: { label: 'έλεγχος ίδιου συνόλου', expected: 't_same', hint: 'Παγίδα: αν ανήκουν ήδη στο ίδιο σύνολο δεν αλλάζουμε ούτε parent_links ούτε subtree_sizes!' },
            s1: { label: 'σύνδεση μικρότερου δέντρου', expected: 't_attach', hint: 'Ο second_root είναι το μικρότερο δέντρο· ο γονέας του γίνεται ο first_root.' }
          },
          tokens: [
            { id: 't_same', label: 'first_root == second_root' },
            { id: 't_attach', label: 'parent_links[second_root] = first_root' },
            { id: 't_d1', label: 'parent_links[first_root] = second_root' },
            { id: 't_d2', label: 'first_node == second_node' }
          ]
        }
      ],
      '05': [
        {
          id: 'drop_05_1',
          unit_id: '05',
          title: 'Drop-In #1: Συγχώνευση N Μικρότερων Στοιχείων σε O(N)',
          source_tag: 'Φροντιστήριο A — Κεφ. 8 #6',
          description: 'Συμπληρώστε τη σύγκριση και την αύξηση των δεικτών για τα target_count μικρότερα στοιχεία από δύο ταξινομημένους πίνακες.',
          lines: [
            'def mergeSmallestN(first_sorted: list[int], second_sorted: list[int], target_count: int) -> list[int]:',
            '    merged_result = [0] * target_count',
            '    first_index, second_index = 0, 0',
            '    for output_index in range(target_count):',
            '        if {{s0}}:',
            '            merged_result[output_index] = first_sorted[first_index]',
            '            {{s1}}',
            '        else:',
            '            merged_result[output_index] = second_sorted[second_index]',
            '            second_index += 1',
            '    return merged_result'
          ],
          slots: {
            s0: { label: 'σύγκριση μετώπων', expected: 't_cmp', hint: 'Συγκρίνουμε τα τρέχοντα στοιχεία first_sorted[first_index] και second_sorted[second_index].' },
            s1: { label: 'προώθηση δείκτη', expected: 't_inc', hint: 'Προχωράμε τον δείκτη first_index από τον οποίο πήραμε στοιχείο.' }
          },
          tokens: [
            { id: 't_cmp', label: 'first_sorted[first_index] <= second_sorted[second_index]' },
            { id: 't_inc', label: 'first_index += 1' },
            { id: 't_d1', label: 'second_index += 1' },
            { id: 't_d2', label: 'first_sorted[first_index] >= second_sorted[second_index]' }
          ]
        },
        {
          id: 'drop_05_2',
          unit_id: '05',
          title: 'Drop-In #2: Διαμερισμός με Βοηθητικό Πίνακα',
          source_tag: 'Φροντιστήριο A — Κεφ. 8 #7',
          description: 'Τοποθετήστε τα μικρότερα του pivot αριστερά και τα μεγαλύτερα/ίσα δεξιά στον βοηθητικό πίνακα.',
          lines: [
            'def partitionAuxiliary(numbers: list[int]) -> list[int]:',
            '    auxiliary_array = [0] * len(numbers)',
            '    pivot_value = numbers[-1]',
            '    left_write_index, right_write_index = 0, len(numbers) - 1',
            '    for element in numbers[:-1]:',
            '        if element < pivot_value:',
            '            auxiliary_array[left_write_index] = element; {{s0}}',
            '        else:',
            '            auxiliary_array[right_write_index] = element; {{s1}}',
            '    {{s2}}',
            '    return auxiliary_array'
          ],
          slots: {
            s0: { label: 'μετακίνηση αριστερού δείκτη', expected: 't_pi', hint: 'Μετακινούμε τον αριστερό δείκτη left_write_index προς τα δεξιά.' },
            s1: { label: 'μετακίνηση δεξιού δείκτη', expected: 't_pj', hint: 'Μετακινούμε τον δεξιό δείκτη right_write_index προς τα αριστερά.' },
            s2: { label: 'τοποθέτηση pivot', expected: 't_piv', hint: 'Το pivot τοποθετείται στην τελική του θέση συνάντησης left_write_index.' }
          },
          tokens: [
            { id: 't_pi', label: 'left_write_index += 1' },
            { id: 't_pj', label: 'right_write_index -= 1' },
            { id: 't_piv', label: 'auxiliary_array[left_write_index] = pivot_value' },
            { id: 't_d1', label: 'right_write_index += 1' },
            { id: 't_d2', label: 'auxiliary_array[0] = pivot_value' }
          ]
        }
      ],
      '06': [
        {
          id: 'drop_06_1',
          unit_id: '06',
          title: 'Drop-In #1: Κλασματικό Σακίδιο (Ταξινόμηση & Ποσότητα)',
          source_tag: 'Φροντιστήριο A — Κεφ. 10 #3',
          description: 'Συμπληρώστε το κλειδί ταξινόμησης πυκνότητας (benefit / weight) και τον υπολογισμό κλασματικής ποσότητας.',
          lines: [
            'def fractionalKnapsack(items: list[dict], remaining_capacity: float) -> float:',
            '    ordered_items = sorted(items, key={{s0}}, reverse=True)',
            '    total_benefit = 0.0',
            '    for item in ordered_items:',
            '        if remaining_capacity >= item["weight"]:',
            '            total_benefit += item["benefit"]; remaining_capacity -= item["weight"]',
            '        else:',
            '            total_benefit += {{s1}}',
            '            break',
            '    return total_benefit'
          ],
          slots: {
            s0: { label: 'κριτήριο πυκνότητας', expected: 't_dens', hint: 'Φθίνουσα πυκνότητα αξίας = benefit / weight.' },
            s1: { label: 'κλασματικό όφελος', expected: 't_frac', hint: 'Παίρνουμε αναλογικά όση χωρητικότητα remaining_capacity απέμεινε.' }
          },
          tokens: [
            { id: 't_dens', label: 'lambda item: item["benefit"] / item["weight"]' },
            { id: 't_frac', label: 'item["benefit"] * (remaining_capacity / item["weight"])' },
            { id: 't_d1', label: 'lambda item: item["benefit"]' },
            { id: 't_d2', label: 'item["weight"] / item["benefit"]' }
          ]
        },
        {
          id: 'drop_06_2',
          unit_id: '06',
          title: 'Drop-In #2: Task Scheduling (Κριτήριο Ταξινόμησης & Επαναχρησιμοποίηση)',
          source_tag: 'Φροντιστήριο A — Κεφ. 10 #4',
          description: 'Επιλέξτε το κριτήριο ταξινόμησης (ώρα έναρξης task[0]) και τη συνθήκη μη σύγκρουσης μηχανής.',
          lines: [
            'def scheduleMinMachines(tasks: list[tuple[int, int]]) -> int:',
            '    ordered_tasks = sorted(tasks, key={{s0}})',
            '    machine_finishes = []',
            '    for start_time, finish_time in ordered_tasks:',
            '        if machine_finishes and {{s1}}:',
            '            heapq.heapreplace(machine_finishes, finish_time)',
            '        else:',
            '            heapq.heappush(machine_finishes, finish_time)',
            '    return len(machine_finishes)'
          ],
          slots: {
            s0: { label: 'ταξινόμηση κατά s_i', expected: 't_start', hint: 'Για ελαχιστοποίηση μηχανών ταξινομούμε κατά ώρα έναρξης task[0] (ΟΧΙ λήξης task[1]).' },
            s1: { label: 'έλεγχος ελεύθερης μηχανής', expected: 't_reuse', hint: 'Μία μηχανή επαναχρησιμοποιείται αν η παλιά εργασία τελείωσε <= start_time.' }
          },
          tokens: [
            { id: 't_start', label: 'lambda task: task[0]' },
            { id: 't_reuse', label: 'machine_finishes[0] <= start_time' },
            { id: 't_d1', label: 'lambda task: task[1]' },
            { id: 't_d2', label: 'machine_finishes[0] > start_time' }
          ]
        }
      ],
      '07': [
        {
          id: 'drop_07_1',
          unit_id: '07',
          title: 'Drop-In #1: Γραμμική Συγχώνευση Λιστών',
          source_tag: 'Φροντιστήριο B — Κεφ. 11 #4',
          description: 'Ολοκληρώστε τον βρόχο συγχώνευσης δύο ταξινομημένων λιστών (first_sorted, second_sorted) σε χρόνο O(n1 + n2).',
          lines: [
            'def mergeSorted(first_sorted: list[int], second_sorted: list[int]) -> list[int]:',
            '    merged_list = []; first_index = 0; second_index = 0',
            '    while {{s0}}:',
            '        if first_sorted[first_index] <= second_sorted[second_index]:',
            '            merged_list.append(first_sorted[first_index]); first_index += 1',
            '        else:',
            '            merged_list.append(second_sorted[second_index]); second_index += 1',
            '    return {{s1}}'
          ],
          slots: {
            s0: { label: 'συνθήκη βρόχου', expected: 't_cond', hint: 'Και οι δύο λίστες πρέπει να έχουν ακόμη ανεπεξέργαστα στοιχεία.' },
            s1: { label: 'υπόλοιπα στοιχεία', expected: 't_tail', hint: 'Επισυνάπτουμε όσα στοιχεία απέμειναν από first_sorted[first_index:] και second_sorted[second_index:].' }
          },
          tokens: [
            { id: 't_cond', label: 'first_index < len(first_sorted) and second_index < len(second_sorted)' },
            { id: 't_tail', label: 'merged_list + first_sorted[first_index:] + second_sorted[second_index:]' },
            { id: 't_d1', label: 'first_index < len(first_sorted) or second_index < len(second_sorted)' },
            { id: 't_d2', label: 'merged_list' }
          ]
        },
        {
          id: 'drop_07_2',
          unit_id: '07',
          title: 'Drop-In #2: Σύνθεση 3 Γινομένων Karatsuba',
          source_tag: 'Σημείωση 07 — Ενότητα 3.1',
          description: 'Εφαρμόστε την αλγεβρική ταυτότητα Karatsuba ώστε το γινόμενο να υπολογίζεται με 3 αντί 4 πολλαπλασιασμούς.',
          lines: [
            'def combineKaratsuba(high_product: int, low_product: int, first_high: int, first_low: int, second_high: int, second_low: int, split_power: int) -> int:',
            '    diff_product = {{s0}}',
            '    middle_term = {{s1}}',
            '    return high_product * (split_power ** 2) + middle_term * split_power + low_product'
          ],
          slots: {
            s0: { label: '3ο αναδρομικό γινόμενο', expected: 't_p3', hint: 'Το τρίτο γινόμενο πολλαπλασιάζει διαφορές (first_high - first_low) και (second_low - second_high).' },
            s1: { label: 'μεσαίος όρος', expected: 't_mid', hint: 'Προσθέτοντας high_product + low_product αλληλοαναιρούνται οι όροι -I_h J_h - I_l J_l.' }
          },
          tokens: [
            { id: 't_p3', label: 'karatsuba(first_high - first_low, second_low - second_high)' },
            { id: 't_mid', label: 'diff_product + high_product + low_product' },
            { id: 't_d1', label: 'diff_product - high_product - low_product' },
            { id: 't_d2', label: 'karatsuba(first_high, second_low)' }
          ]
        }
      ]
    };

    const true_false_drills = {
      prereq: [
        { statement: 'Στην ανάλυση αλγορίθμων του μαθήματος, όταν γράφουμε log n εννοούμε λογάριθμο βάσης 2 (log_2 n).', answer: true, explanation: 'Σωστό: οι δυαδικές διαιρέσεις και τα δυαδικά δέντρα ορίζουν φυσικά βάση 2.' },
        { statement: 'Το άθροισμα 1 + 2 + 3 + ... + n ανήκει στην κλάση Θ(n).', answer: false, explanation: 'Λάθος: 1 + 2 + ... + n = n(n + 1) / 2 = Θ(n^2).' },
        { statement: 'Στον 1-indexed πίνακα ενός δυαδικού σωρού, το αριστερό παιδί της θέσης i είναι στη θέση 2i και ο γονέας στη θέση floor(i/2).', answer: true, explanation: 'Σωστό: το A[0] παραμένει κενό για να ισχύουν οι καθαροί τύποι 2i, 2i+1 και floor(i/2).' },
        { statement: 'Η ακέραια διαίρεση 9 // 2 στην Python επιστρέφει 5.', answer: false, explanation: 'Λάθος: ο τελεστής // στρογγυλεύει προς τα κάτω (floor), άρα 9 // 2 == 4.' }
      ],
      '00': [
        { statement: 'Στην Πρόοδο εξετάζονται τα Κεφάλαια 1, 5, 6, 7, 8, 10 και 11 (όχι τα 2, 3, 4, 9, 12–17).', answer: true, explanation: 'Σωστό: Η ύλη της Προόδου καλύπτει αυτά τα 7 κεφάλαια με τις ρητές εξαιρέσεις (1.4.1, 5.5, Chernoff, Λήμμα 6.1, 6.5, 7.3.1, απόδειξη Huffman).' },
        { statement: 'Ο αλγόριθμος Huffman και η πολυπλοκότητά του O(n + d log d) είναι εκτός ύλης Προόδου.', answer: false, explanation: 'Λάθος: Μόνο η τυπική απόδειξη βελτιστότητας (σελ. 294–297) εξαιρείται. Ο αλγόριθμος, η ιχνηλάτηση και το O(n + d log d) εξετάζονται κανονικά.' },
        { statement: 'Η επιμερισμένη ανάλυση (amortized) στηρίζεται σε τυχαίες κατανομές πιθανότητας επί των εισόδων.', answer: false, explanation: 'Λάθος: Η επιμερισμένη ανάλυση είναι ντετερμινιστική στη χειρότερη ακολουθία (χωρίς πιθανότητες).' },
        { statement: 'Το Φράγμα Chernoff και η απόδειξη Ackermann (7.3.1) εξαιρούνται από την Πρόοδο.', answer: true, explanation: 'Σωστό: Καταγράφονται ρητά στον πίνακα εξαιρέσεων της Ενότητας 00.' }
      ],
      '01': [
        { statement: 'Ένας αλγόριθμος O(n log n) εκτελείται ταχύτερα από έναν O(n^2) για ΟΛΕΣ τις περιπτώσεις εισόδου (ακόμα και πολύ μικρά n).', answer: false, explanation: 'Λάθος (Φροντιστήριο A, Κεφ. 1 #1a): Τα ασυμπτωτικά όρια αφορούν μεγάλα n (>= n_0)· για μικρό n οι σταθερές μπορούν να δώσουν προβάδισμα στο O(n^2).' },
        { statement: 'Ο συμβολισμός του μεγάλου Ο παρέχει ένα κάτω όριο απόδοσης.', answer: false, explanation: 'Λάθος (Φροντιστήριο A, Κεφ. 1 #1b): Το Big-Oh είναι ασυμπτωτικό ΑΝΩ όριο, ενώ το Big-Omega (Ω) είναι κάτω όριο.' },
        { statement: 'Ο συμβολισμός του μεγάλου Ω παρέχει ένα κάτω όριο απόδοσης.', answer: true, explanation: 'Σωστό (Φροντιστήριο A, Κεφ. 1 #1c): f(n) = Ω(g(n)) <=> f(n) >= c * g(n) για n >= n_0.' },
        { statement: 'Ο συμβολισμός του μεγάλου Θ παρέχει περισσότερη πληροφορία από τον συμβολισμό του μεγάλου Ο.', answer: true, explanation: 'Σωστό (Φροντιστήριο A, Κεφ. 1 #1d): Το Θ(g(n)) δίνει ταυτόχρονα σφιχτό άνω (O) και κάτω (Ω) όριο.' },
        { statement: 'Οι συμβολισμοί O, Ω και Θ αφορούν τον ρυθμό αύξησης του χρόνου εκτέλεσης καθώς τα δεδομένα εισόδου γίνονται πολύ μεγάλα.', answer: true, explanation: 'Σωστό (Φροντιστήριο A, Κεφ. 1 #1e).' },
        { statement: 'Το πρόβλημα της μέγιστης υποακολουθίας (Maximum Subarray) λύνεται τόσο σε O(n^2) όσο και σε O(n).', answer: true, explanation: 'Σωστό (Φροντιστήριο A, Κεφ. 1 #1f): MaxsubFaster O(n^2) με προθεματικά, MaxsubFastest O(n) με Kadane M_t.' }
      ],
      '02': [
        { statement: 'Η έννοια της ουράς προτεραιότητας και του σωρού είναι ταυτόσημες.', answer: false, explanation: 'Λάθος (Φροντιστήριο A, Κεφ. 5 #1a): Η ουρά προτεραιότητας είναι ΑΤΔ, ενώ ο σωρός είναι μία από τις υλοποιήσεις της.' },
        { statement: 'Ένας σωρός μπορεί να περιέχει διπλότυπα κλειδιά.', answer: true, explanation: 'Σωστό (Φροντιστήριο A, Κεφ. 5 #1b): Η σχέση σωρού είναι key(v) >= key(parent(v)), επιτρέποντας ισότητες.' },
        { statement: 'Η δημιουργία σωρού με διαδοχικές εισαγωγές είναι ταχύτερη από την κατασκευή με heapify (Bottom-Up).', answer: false, explanation: 'Λάθος (Φροντιστήριο A, Κεφ. 5 #1c): Διαδοχικές εισαγωγές κοστίζουν O(n log n), ενώ η Bottom-Up / heapify κοστίζει O(n).' },
        { statement: 'Η ουρά προτεραιότητας είναι Αφηρημένος Τύπος Δεδομένων (ΑΤΔ).', answer: true, explanation: 'Σωστό (Φροντιστήριο A, Κεφ. 5 #1d).' },
        { statement: 'Ένας σωρός ελαχίστων είναι Αφηρημένος Τύπος Δεδομένων (ΑΤΔ).', answer: false, explanation: 'Λάθος (Φροντιστήριο A, Κεφ. 5 #1e): Είναι συγκεκριμένη δομή δεδομένων υλοποίησης της ΑΤΔ Ουράς Προτεραιότητας.' },
        { statement: 'Η αποδοτικότερη υλοποίηση σωρού είναι με δέντρα δεικτών (2 δείκτες ανά κόμβο) αντί 1-indexed πίνακα.', answer: false, explanation: 'Λάθος (Φροντιστήριο A, Κεφ. 5 #1f): Ο 1-indexed πίνακας εξοικονομεί δείκτες και επιτρέπει O(1) πρόσβαση στον τελευταίο κόμβο.' },
        { statement: 'Η λίστα [2, 4, 6, 10, 8, 15] μπορεί να αντιπροσωπεύει έναν έγκυρο σωρό ελαχίστων.', answer: true, explanation: 'Σωστό (Φροντιστήριο A, Κεφ. 5 #1i): 2 <= 4, 6 | 4 <= 10, 8 | 6 <= 15 (η ιδιότητα σωρού ισχύει).' }
      ],
      '03': [
        { statement: 'Ο κατακερματισμός με αλυσίδες (separate chaining) μπορεί να έχει συντελεστή φόρτωσης α πάνω από 100% (α > 1).', answer: true, explanation: 'Σωστό (Φροντιστήριο A, Κεφ. 6 #1a): Κάθε κάδος διατηρεί συνδεδεμένη λίστα που χωρά πάνω από 1 στοιχείο.' },
        { statement: 'Ο κατακερματισμός ανοιχτής διευθυνσιοδότησης μπορεί να έχει load factor πάνω από 100%.', answer: false, explanation: 'Λάθος (Φροντιστήριο A, Κεφ. 6 #1b): Κάθε κελί χωρά το πολύ 1 εγγραφή, άρα α <= 1 (και απαιτείται α <= 1/2 για O(1)).' },
        { statement: 'Μία συνάρτηση κατακερματισμού πρέπει για δύο διαφορετικές εισόδους να επιστρέφει υποχρεωτικά την ίδια τιμή.', answer: false, explanation: 'Λάθος (Φροντιστήριο A, Κεφ. 6 #1c): Επιδιώκεται ακριβώς το αντίθετο (ελαχιστοποίηση συγκρούσεων).' },
        { statement: 'Μπορούμε αποδοτικά να διασχίσουμε ταξινομημένα τα κλειδιά σε έναν πίνακα κατακερματισμού.', answer: false, explanation: 'Λάθος (Φροντιστήριο A, Κεφ. 6 #1d): Οι πίνακες κατακερματισμού διασκορπίζουν τα κλειδιά χωρίς διάταξη.' },
        { statement: 'Ο διπλός κατακερματισμός είναι επέκταση του κατακερματισμού με αλυσίδες.', answer: false, explanation: 'Λάθος (Φροντιστήριο A, Κεφ. 6 #1f): Είναι τεχνική ανοιχτής διευθυνσιοδότησης.' },
        { statement: 'Οι πίνακες κατακερματισμού συνήθως έχουν ως μέγεθος N έναν πρώτο αριθμό.', answer: true, explanation: 'Σωστό (Φροντιστήριο A, Κεφ. 6 #1h): Ο πρώτος N αποτρέπει συσσώρευση λόγω κοινών διαιρετών (Πρόταση 2.4).' },
        { statement: 'Η συνάρτηση murmur είναι κρυπτογραφική, ενώ η SHA256 δεν είναι.', answer: false, explanation: 'Λάθος (Φροντιστήριο A, Κεφ. 6 #1i-j): Ισχύει το αντίστροφο — η murmur είναι μη-κρυπτογραφική, ενώ η SHA256 είναι κρυπτογραφική.' }
      ],
      '04': [
        { statement: 'Η υλοποίηση Union-Find με συνδεδεμένες λίστες είναι ασυμπτωτικά αποδοτικότερη από την υλοποίηση με δέντρα και ευρετικούς.', answer: false, explanation: 'Λάθος (Φροντιστήριο A, Κεφ. 7 #1a): Η λίστα δίνει O(n log n + m), ενώ τα δέντρα με ένωση κατά μέγεθος + συμπίεση διαδρομής δίνουν O((n + m) α(n)).' },
        { statement: 'Η δεντρική υλοποίηση Union-Find στηρίζεται σε δείκτες από τον κάθε κόμβο γονέα προς τα παιδιά του.', answer: false, explanation: 'Λάθος (Φροντιστήριο A, Κεφ. 7 #1b): Κάθε κόμβος έχει δείκτη προς τον ΓΟΝΕΑ του (parent pointer) ώστε η find να ανεβαίνει στη ρίζα.' },
        { statement: 'Η δομή ένωσης-εύρεσης είναι γνωστή και ως δομή ξένων συνόλων (disjoint sets).', answer: true, explanation: 'Σωστό (Φροντιστήριο A, Κεφ. 7 #1c).' },
        { statement: 'Η συμπίεση διαδρομής (path compression) εφαρμόζεται κατά τη λειτουργία makeSet.', answer: false, explanation: 'Λάθος (Φροντιστήριο A, Κεφ. 7 #1d): Εφαρμόζεται κατά την αναζήτηση find(e), συνδέοντας όλους τους κόμβους της διαδρομής στη ρίζα.' },
        { statement: 'Στην ένωση κατά μέγεθος (union by size), το μεγαλύτερο δέντρο προσαρτάται ως παιδί στο μικρότερο.', answer: false, explanation: 'Λάθος (Φροντιστήριο A, Κεφ. 7 #1e): Το ΜΙΚΡΟΤΕΡΟ δέντρο γίνεται παιδί της ρίζας του ΜΕΓΑΛΥΤΕΡΟΥ.' }
      ],
      '05': [
        { statement: 'Το κάτω όριο για αλγορίθμους ταξινόμησης βάσει συγκρίσεων είναι Ω(n log n).', answer: true, explanation: 'Σωστό (Φροντιστήριο A, Κεφ. 8 #1a).' },
        { statement: 'Το κάτω όριο για αλγορίθμους ταξινόμησης βάσει συγκρίσεων είναι O(n log n).', answer: false, explanation: 'Λάθος (Φροντιστήριο A, Κεφ. 8 #1b): Τα κάτω όρια εκφράζονται με Ω(n log n), όχι με O(n log n).' },
        { statement: 'Ο Quick-Sort είναι συνήθως ταχύτερος στην πράξη από τον Merge-Sort για μεγάλα δεδομένα στην κύρια μνήμη (RAM).', answer: true, explanation: 'Σωστό (Φροντιστήριο A, Κεφ. 8 #1d).' },
        { statement: 'Ο Merge-Sort είναι τυχαιοποιημένος αλγόριθμος.', answer: false, explanation: 'Λάθος (Φροντιστήριο A, Κεφ. 8 #1e): Ο Merge-Sort είναι καθοριστικός (ντετερμινιστικός)· ο Quick-Sort χρησιμοποιεί τυχαιοποίηση.' },
        { statement: 'Μία σταθερή ταξινόμηση (stable sort) επιτρέπει ταξινόμηση κατά όνομα και έπειτα κατά έτος διατηρώντας την αλφαβητική σειρά ανά έτος.', answer: true, explanation: 'Σωστό (Φροντιστήριο A, Κεφ. 8 #1f): Διατηρεί τη σχετική σειρά των ίσων κλειδιών.' },
        { statement: 'Η MergeSort περιέχει δύο αναδρομικές κλήσεις, ενώ η BinarySearch περιέχει μόνο μία.', answer: true, explanation: 'Σωστό (Φροντιστήριο A, Κεφ. 8 #1g-h): MergeSort: 2T(n/2)+n, BinarySearch: T(n/2)+1.' },
        { statement: 'Η QuickSort προκαλεί πάντα αναδρομικές κλήσεις σε 2 υποακολουθίες ακριβώς μεγέθους n/2.', answer: false, explanation: 'Λάθος (Φροντιστήριο A, Κεφ. 8 #1i): Τα μεγέθη εξαρτώνται από το pivot (στη χειρότερη περίπτωση 0 και n-1).' }
      ],
      '06': [
        { statement: 'Η άπληστη μέθοδος επιστρέφει τη βέλτιστη λύση για το Κλασματικό Πρόβλημα Σακιδίου.', answer: true, explanation: 'Σωστό (Φροντιστήριο A, Κεφ. 10 #1a): Με φθίνουσα πυκνότητα b_i / w_i (επιχείρημα ανταλλαγής).' },
        { statement: 'Η άπληστη μέθοδος επιστρέφει τη βέλτιστη λύση για το 0-1 Πρόβλημα Σακιδίου.', answer: false, explanation: 'Λάθος (Φροντιστήριο A, Κεφ. 10 #1b): Αποτυγχάνει σε αδιαίρετα αντικείμενα (π.χ. W=10: (6,36), (5,25), (5,25)).' },
        { statement: 'Στον χρονοπρογραμματισμό ελαχιστοποίησης μηχανών, η ανάθεση κατά σειρά ώρας έναρξης (s_i) είναι βέλτιστη.', answer: true, explanation: 'Σωστό (Φροντιστήριο A, Κεφ. 10 #1d): Θεώρημα 2.2 (k ταυτόχρονες συγκρούσεις τη στιγμή s_i).' },
        { statement: 'Η κωδικοποίηση Huffman χρησιμοποιεί το ίδιο πλήθος bits για κάθε χαρακτήρα και αποτελεί μέθοδο κρυπτογράφησης.', answer: false, explanation: 'Λάθος (Φροντιστήριο A, Κεφ. 10 #1f-h): Χρησιμοποιεί κωδικούς μεταβλητού μήκους (prefix-free) για συμπίεση, όχι κρυπτογράφηση.' }
      ],
      '07': [
        { statement: 'Τα προβλήματα Διαίρει και Βασίλευε επιλύονται τυπικά με αναδρομή.', answer: true, explanation: 'Σωστό (Φροντιστήριο B, Κεφ. 11 #1a).' },
        { statement: 'Στο Διαίρει και Βασίλευε το πρόβλημα χωρίζεται σε επικαλυπτόμενα υποπροβλήματα.', answer: false, explanation: 'Λάθος (Φροντιστήριο B, Κεφ. 11 #1b): Τα υποπροβλήματα είναι ΑΝΕΞΑΡΤΗΤΑ (ξένα)· τα επικαλυπτόμενα αφορούν τον Δυναμικό Προγραμματισμό (εκτός Προόδου).' },
        { statement: 'Ο ταχύτερος αλγόριθμος πολλαπλασιασμού δύο n-bit ακεραίων στην ύλη μας έχει πολυπλοκότητα O(n^2).', answer: false, explanation: 'Λάθος (Φροντιστήριο B, Κεφ. 11 #1d): Ο αλγόριθμος Karatsuba επιτυγχάνει Θ(n^{log_2 3}) ~ Θ(n^1.585).' },
        { statement: 'Το Master Theorem εφαρμόζεται σε διαιρετικές αναδρομικές εξισώσεις μορφής T(n) = aT(n/b) + f(n).', answer: true, explanation: 'Σωστό (Φροντιστήριο B, Κεφ. 11 #1e).' }
      ]
    };

    return {
      code_examples: code_examples,
      dropin_puzzles: dropin_puzzles,
      true_false_drills: true_false_drills
    };
  }

  const bundle = buildCodeAndGamesBundle();
  global_scope.MidtermApp = global_scope.MidtermApp || {};
  global_scope.MidtermApp.code_examples = bundle.code_examples;
  global_scope.MidtermApp.dropin_puzzles = bundle.dropin_puzzles;
  global_scope.MidtermApp.true_false_drills = bundle.true_false_drills;
})(window);
