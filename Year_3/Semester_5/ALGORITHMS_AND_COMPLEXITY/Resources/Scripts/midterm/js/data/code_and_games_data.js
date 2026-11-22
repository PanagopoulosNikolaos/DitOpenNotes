(function (global_scope) {
  'use strict';

  /**
   * Builds Python code examples, Drop-In puzzles, and Recitation True/False drills for Units 00-07.
   *
   * Returns:
   *     object: Bundle containing code_examples, dropin_puzzles, and true_false_drills maps.
   */
  function buildCodeAndGamesBundle() {
    const code_examples = {
      '00': [
        {
          title: 'Επιλογή Στρατηγικής Προόδου (Strategy Chooser)',
          source_tag: 'Σημείωση 00 — Ενότητα 3.3',
          complexity: 'Οδηγός Απόφασης Προόδου',
          code: [
            'def chooseMidtermStrategy(problem_type: str, req: str) -> str:',
            '    """Maps a Midterm exam problem specification to the optimal strategy.',
            '',
            '    Args:',
            '        problem_type (str): Category such as "sets", "sort", or "opt".',
            '        req (str): Key constraint from the problem statement.',
            '',
            '    Returns:',
            '        str: Recommended algorithm or data structure with case bound.',
            '    """',
            '    if problem_type == "sets":',
            '        if req == "min_extract":',
            '            return "Binary Heap: O(log n) worst, Bottom-Up O(n)"',
            '        if req == "worst_o1_lookup":',
            '            return "Cuckoo Hashing: O(1) worst get/remove"',
            '        if req == "disjoint_union":',
            '            return "Union-Find: O((n + m) * alpha(n))"',
            '    if problem_type == "sort":',
            '        if req == "disk_sequential":',
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
            'def compareDoublingEffect(n_val: int) -> dict[str, float]:',
            '    """Computes the seven core growth rates for input size n_val.',
            '',
            '    Args:',
            '        n_val (int): Input size (n_val >= 2).',
            '',
            '    Returns:',
            '        dict[str, float]: Growth values for each complexity class.',
            '    """',
            '    log_n = math.log2(n_val)',
            '    return {',
            '        "constant": 1.0,',
            '        "log_n": log_n,',
            '        "linear": float(n_val),',
            '        "n_log_n": n_val * log_n,',
            '        "quadratic": float(n_val ** 2),',
            '        "cubic": float(n_val ** 3),',
            '        "exponential": float(2 ** min(n_val, 30))  # Caps exponent to avoid overflow.',
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
            'def reverseInPlace(arr: list[int]) -> list[int]:',
            '    """Reverses a list in place using constant auxiliary space.',
            '',
            '    Args:',
            '        arr (list[int]): Mutable sequence of elements.',
            '',
            '    Returns:',
            '        list[int]: The same list reversed in place.',
            '    """',
            '    n_len = len(arr)',
            '    for idx in range(n_len // 2):',
            '        mirror_idx = n_len - 1 - idx',
            '        # Swaps symmetric endpoints without allocating a second array.',
            '        arr[idx], arr[mirror_idx] = arr[mirror_idx], arr[idx]',
            '    return arr'
          ].join('\n')
        },
        {
          title: 'Μέγιστο Άθροισμα Υπο-Πίνακα: MaxsubFastest',
          source_tag: 'Σημείωση 01 — Ενότητα 3.3',
          complexity: 'O(n) χειρότερη περίπτωση',
          code: [
            'def maxsubFastest(arr: list[int]) -> int:',
            '    """Finds maximum contiguous subarray sum using Kadane suffix recurrence.',
            '',
            '    Args:',
            '        arr (list[int]): Input sequence of integers.',
            '',
            '    Returns:',
            '        int: Maximum subarray sum (0 for empty subarray).',
            '    """',
            '    current_suffix = 0',
            '    best_sum = 0',
            '    for value in arr:',
            '        # Resets negative suffix to 0 because negative prefix never helps.',
            '        current_suffix = max(0, current_suffix + value)',
            '        best_sum = max(best_sum, current_suffix)',
            '    return best_sum'
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
            'def extractSmallestKeys(values: list[int], k_count: int) -> list[int]:',
            '    """Extracts the k_count smallest elements via O(n) heapify and k pops.',
            '',
            '    Args:',
            '        values (list[int]): Unsorted list of integer keys.',
            '        k_count (int): Number of smallest keys to extract.',
            '',
            '    Returns:',
            '        list[int]: Ascending list of the k_count smallest keys.',
            '    """',
            '    heap_copy = list(values)',
            '    heapq.heapify(heap_copy)  # Bottom-up construction runs in O(n) time.',
            '    smallest = []',
            '    for _ in range(min(k_count, len(heap_copy))):',
            '        smallest.append(heapq.heappop(heap_copy))',
            '    return smallest'
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
            '        data (list): Internal 1-indexed array with unused index 0.',
            '    """',
            '',
            '    def __init__(self) -> None:',
            '        """Initializes an empty 1-indexed heap with sentinel at index 0."""',
            '        self.data = [None]',
            '',
            '    def insertKey(self, key: int) -> None:',
            '        """Inserts key at end and restores heap order via upheap."""',
            '        self.data.append(key)',
            '        idx = len(self.data) - 1',
            '        while idx > 1 and self.data[idx // 2] > self.data[idx]:',
            '            parent = idx // 2',
            '            self.data[parent], self.data[idx] = self.data[idx], self.data[parent]',
            '            idx = parent'
          ].join('\n')
        }
      ],
      '03': [
        {
          title: 'Έλεγχος Ξένων Ακολουθιών με Σύνολο Κατακερματισμού',
          source_tag: 'Φροντιστήριο A — Κεφ. 6 #6',
          complexity: 'O(M + N) αναμενόμενη (hash set στη μικρότερη Μ)',
          code: [
            'def areDisjoint(seq_small: list[int], seq_large: list[int]) -> bool:',
            '    """Checks whether two sequences share no common element.',
            '',
            '    Args:',
            '        seq_small (list[int]): Smaller sequence of length M.',
            '        seq_large (list[int]): Larger sequence of length N.',
            '',
            '    Returns:',
            '        bool: True if disjoint, False if any common element exists.',
            '    """',
            '    # Hashes the smaller sequence so hash-table space stays O(M).',
            '    lookup_set = set(seq_small)',
            '    for item in seq_large:',
            '        if item in lookup_set:',
            '            return False',
            '    return True'
          ].join('\n')
        },
        {
          title: 'Κώδικας Κατακερματισμού με Κανόνα Horner (z = 33)',
          source_tag: 'Σημείωση 03 — Ενότητα 3.2',
          complexity: 'Θ(n) χειρότερη (n = μήκος συμβολοσειράς)',
          code: [
            'def polynomialHashCode(word: str, base_z: int = 33) -> int:',
            '    """Computes polynomial hash code of a string via Horner rule.',
            '',
            '    Args:',
            '        word (str): Input character string.',
            '        base_z (int): Polynomial base (33 = 32 + 1 for fast shift-add).',
            '',
            '    Returns:',
            '        int: Integer hash code h1 before compression.',
            '    """',
            '    acc_hash = 0',
            '    for ch in word:',
            '        acc_hash = acc_hash * base_z + ord(ch)',
            '    return acc_hash'
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
            '    def __init__(self, count: int) -> None:',
            '        """Initializes count singleton sets indexed 0..count-1."""',
            '        self.parent = list(range(count))',
            '        self.size = [1] * count',
            '',
            '    def findRoot(self, node: int) -> int:',
            '        """Finds representative root and compresses traversed path."""',
            '        if self.parent[node] != node:',
            '            # Redirects every visited node directly to root on unwind.',
            '            self.parent[node] = self.findRoot(self.parent[node])',
            '        return self.parent[node]',
            '',
            '    def unionSets(self, u_node: int, v_node: int) -> bool:',
            '        """Unites sets containing u_node and v_node by attaching smaller tree."""',
            '        r_u = self.findRoot(u_node)',
            '        r_v = self.findRoot(v_node)',
            '        if r_u == r_v:',
            '            return False',
            '        if self.size[r_u] < self.size[r_v]:',
            '            r_u, r_v = r_v, r_u',
            '        self.parent[r_v] = r_u',
            '        self.size[r_u] += self.size[r_v]',
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
            '        friendships (list[list[int]]): Pairs [u, v] representing edges.',
            '',
            '    Returns:',
            '        dict[int, list[int]]: Components keyed by root representative.',
            '    """',
            '    uf = UnionFind(user_count)',
            '    for u_val, v_val in friendships:',
            '        uf.unionSets(u_val, v_val)',
            '    groups: dict[int, list[int]] = {}',
            '    for person in range(user_count):',
            '        root = uf.findRoot(person)',
            '        groups.setdefault(root, []).append(person)',
            '    return groups'
          ].join('\n')
        }
      ],
      '05': [
        {
          title: 'Συγχώνευση των N Μικρότερων Στοιχείων από 2 Ταξινομημένους Πίνακες',
          source_tag: 'Φροντιστήριο A — Κεφ. 8 #6',
          complexity: 'O(N) χειρότερη',
          code: [
            'def mergeSmallestN(arr_a: list[int], arr_b: list[int], n_limit: int) -> list[int]:',
            '    """Merges two sorted arrays and returns the smallest n_limit values in O(N).',
            '',
            '    Args:',
            '        arr_a (list[int]): First ascending sorted array.',
            '        arr_b (list[int]): Second ascending sorted array.',
            '        n_limit (int): Count of smallest elements to return.',
            '',
            '    Returns:',
            '        list[int]: Sorted list of the n_limit smallest elements.',
            '    """',
            '    merged = [0] * n_limit',
            '    idx_a = 0',
            '    idx_b = 0',
            '    for out_idx in range(n_limit):',
            '        if arr_a[idx_a] <= arr_b[idx_b]:',
            '            merged[out_idx] = arr_a[idx_a]',
            '            idx_a += 1',
            '        else:',
            '            merged[out_idx] = arr_b[idx_b]',
            '            idx_b += 1',
            '    return merged'
          ].join('\n')
        },
        {
          title: 'Επί-Τόπου Διαμερισμός (inPlacePartition)',
          source_tag: 'Σημείωση 05 — Ενότητα 3.3',
          complexity: 'O(r - l + 1) ανά κλήση, O(n log n) αναμενόμενη',
          code: [
            'def inPlacePartition(seq: list[int], left: int, right: int) -> tuple[int, int]:',
            '    """Partitions seq[left..right] around pivot seq[right] in place.',
            '',
            '    Args:',
            '        seq (list[int]): Target array modified in place.',
            '        left (int): Left inclusive boundary.',
            '        right (int): Right inclusive boundary (pivot index).',
            '',
            '    Returns:',
            '        tuple[int, int]: Boundaries (h_idx, k_idx) of equal-pivot block.',
            '    """',
            '    pivot = seq[right]',
            '    j_ptr, k_ptr = left, right - 1',
            '    while j_ptr <= k_ptr:',
            '        while j_ptr <= k_ptr and seq[j_ptr] < pivot: j_ptr += 1',
            '        while k_ptr >= j_ptr and seq[k_ptr] >= pivot: k_ptr -= 1',
            '        if j_ptr < k_ptr:',
            '            seq[j_ptr], seq[k_ptr] = seq[k_ptr], seq[j_ptr]',
            '            j_ptr += 1; k_ptr -= 1',
            '    h_idx = j_ptr',
            '    # Places pivot equal block into seq[h_idx..k2_ptr].',
            '    j2_ptr, k2_ptr = h_idx, right',
            '    while j2_ptr <= k2_ptr:',
            '        while j2_ptr <= k2_ptr and seq[j2_ptr] == pivot: j2_ptr += 1',
            '        while k2_ptr >= j2_ptr and seq[k2_ptr] > pivot: k2_ptr -= 1',
            '        if j2_ptr < k2_ptr:',
            '            seq[j2_ptr], seq[k2_ptr] = seq[k2_ptr], seq[j2_ptr]',
            '    return h_idx, k2_ptr'
          ].join('\n')
        }
      ],
      '06': [
        {
          title: 'Κλασματικό Πρόβλημα Σακιδίου (fractionalKnapsack)',
          source_tag: 'Φροντιστήριο A — Κεφ. 10 #3 & Σημείωση 06',
          complexity: 'O(n log n) χειρότερη',
          code: [
            'def fractionalKnapsack(items: list[dict], capacity: float) -> float:',
            '    """Maximizes total value for divisible items via greedy density sort.',
            '',
            '    Args:',
            '        items (list[dict]): Items with "weight" and "value" keys.',
            '        capacity (float): Total knapsack weight limit.',
            '',
            '    Returns:',
            '        float: Globally optimal total benefit.',
            '    """',
            '    ordered = sorted(items, key=lambda x: x["value"] / x["weight"], reverse=True)',
            '    total_val = 0.0',
            '    rem_cap = capacity',
            '    for item in ordered:',
            '        if rem_cap <= 0:',
            '            break',
            '        take_w = min(item["weight"], rem_cap)',
            '        total_val += take_w * (item["value"] / item["weight"])',
            '        rem_cap -= take_w',
            '    return total_val'
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
            '    """Assigns all tasks [start, finish] to minimum non-conflicting machines.',
            '',
            '    Args:',
            '        tasks (list[tuple[int, int]]): Intervals (start_time, finish_time).',
            '',
            '    Returns:',
            '        int: Minimum number of machines required.',
            '    """',
            '    # Sorts strictly by ascending start time s_i (never by finish time f_i).',
            '    sorted_tasks = sorted(tasks, key=lambda t: t[0])',
            '    machine_finishes: list[int] = []',
            '    for start_t, finish_t in sorted_tasks:',
            '        if machine_finishes and machine_finishes[0] <= start_t:',
            '            heapq.heapreplace(machine_finishes, finish_t)',
            '        else:',
            '            heapq.heappush(machine_finishes, finish_t)',
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
            'def mergeSorted(list_one: list[int], list_two: list[int]) -> list[int]:',
            '    """Merges two sorted lists into a single sorted list in linear time.',
            '',
            '    Args:',
            '        list_one (list[int]): First sorted list.',
            '        list_two (list[int]): Second sorted list.',
            '',
            '    Returns:',
            '        list[int]: Combined ascending sorted list.',
            '    """',
            '    result: list[int] = []',
            '    i_idx, j_idx = 0, 0',
            '    while i_idx < len(list_one) and j_idx < len(list_two):',
            '        if list_one[i_idx] <= list_two[j_idx]:',
            '            result.append(list_one[i_idx])',
            '            i_idx += 1',
            '        else:',
            '            result.append(list_two[j_idx])',
            '            j_idx += 1',
            '    return result + list_one[i_idx:] + list_two[j_idx:]'
          ].join('\n')
        },
        {
          title: 'Πολλαπλασιασμός Karatsuba (3 Αναδρομές)',
          source_tag: 'Σημείωση 07 — Ενότητα 3.1',
          complexity: 'Θ(n^{log_2 3}) ~ Θ(n^1.585)',
          code: [
            'def karatsuba(num_a: int, num_b: int, base: int = 10) -> int:',
            '    """Multiplies two integers using 3 recursive sub-products.',
            '',
            '    Args:',
            '        num_a (int): First non-negative integer.',
            '        num_b (int): Second non-negative integer.',
            '        base (int): Positional base (10 or 2).',
            '',
            '    Returns:',
            '        int: Exact integer product num_a * num_b.',
            '    """',
            '    if num_a < base or num_b < base:',
            '        return num_a * num_b',
            '    half_len = max(len(str(num_a)), len(str(num_b))) // 2',
            '    split_pow = base ** half_len',
            '    a_high, a_low = divmod(num_a, split_pow)',
            '    b_high, b_low = divmod(num_b, split_pow)',
            '    p1 = karatsuba(a_high, b_high, base)',
            '    p2 = karatsuba(a_low, b_low, base)',
            '    p3 = karatsuba(a_high - a_low, b_low - b_high, base)',
            '    mid_term = p3 + p1 + p2',
            '    return p1 * (split_pow ** 2) + mid_term * split_pow + p2'
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
          description: 'Τοποθετήστε τα σωστά σχήματα απόφασης στα κενά ώστε η συνάρτηση να αντιστοιχίζει τις απαιτήσεις Προόδου στη σωστή δομή/αλγόριθμο.',
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
            s0: { expected: 't_cuckoo', hint: 'Μόνο μία δομή κατακερματισμού εγγυάται O(1) χειρότερη στην αναζήτηση.' },
            s1: { expected: 't_merge', hint: 'Σειριακή προσπέλαση σε δίσκο + σταθερότητα + O(n log n) χειρότερη.' },
            s2: { expected: 't_uf', hint: 'Διαχείριση ξένων συνόλων με ένωση κατά μέγεθος & συμπίεση διαδρομής.' },
            s3: { expected: 't_heap', hint: 'Συνεχής εξαγωγή ελάχιστου κλειδιού σε O(log n) χειρότερη.' }
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
          description: 'Συμπληρώστε το όριο του βρόχου και τον συμμετρικό δείκτη ώστε ο αλγόριθμος να αντιστρέφει τον πίνακα επί-τόπου.',
          lines: [
            'def reverseInPlace(arr: list[int]) -> list[int]:',
            '    n_len = len(arr)',
            '    for i in range({{s0}}):',
            '        j = {{s1}}',
            '        arr[i], arr[j] = {{s2}}',
            '    return arr'
          ],
          slots: {
            s0: { expected: 't_half', hint: 'Αν διατρέξουμε όλο το n_len, θα αντιστραφούν τα στοιχεία δύο φορές!' },
            s1: { expected: 't_mirror', hint: 'Ο συμμετρικός δείκτης του i ξεκινώντας από το τέλος n_len - 1.' },
            s2: { expected: 't_swap', hint: 'Ανταλλαγή των στοιχείων στις θέσεις i και j.' }
          },
          tokens: [
            { id: 't_half', label: 'n_len // 2' },
            { id: 't_mirror', label: 'n_len - 1 - i' },
            { id: 't_swap', label: 'arr[j], arr[i]' },
            { id: 't_d1', label: 'n_len' },
            { id: 't_d2', label: 'n_len - i' }
          ]
        },
        {
          id: 'drop_01_2',
          unit_id: '01',
          title: 'Drop-In #2: Αναδρομική Σχέση MaxsubFastest',
          source_tag: 'Σημείωση 01 — Ενότητα 3.3',
          description: 'Συμπληρώστε την ενημέρωση του επιθεματικού αθροίσματος M_t και του καθολικού μεγίστου m.',
          lines: [
            'def maxsubFastest(arr: list[int]) -> int:',
            '    m_t = 0',
            '    best_m = 0',
            '    for val in arr:',
            '        m_t = {{s0}}',
            '        best_m = {{s1}}',
            '    return best_m'
          ],
          slots: {
            s0: { expected: 't_mt', hint: 'Αν το επίθεμα γίνει αρνητικό, το μηδενίζουμε (M_t = max{0, M_{t-1} + val}).' },
            s1: { expected: 't_best', hint: 'Ενημερώνουμε το μέγιστο m που είδαμε μέχρι τώρα.' }
          },
          tokens: [
            { id: 't_mt', label: 'max(0, m_t + val)' },
            { id: 't_best', label: 'max(best_m, m_t)' },
            { id: 't_d1', label: 'm_t + val' },
            { id: 't_d2', label: 'min(0, m_t + val)' }
          ]
        }
      ],
      '02': [
        {
          id: 'drop_02_1',
          unit_id: '02',
          title: 'Drop-In #1: Εξαγωγή 10 Μικρότερων με Heap',
          source_tag: 'Φροντιστήριο A — Κεφ. 5 #7',
          description: 'Οργανώστε τη λίστα σε σωρό ελαχίστων σε χρόνο O(n) και εξαγάγετε τα k μικρότερα στοιχεία.',
          lines: [
            'import heapq',
            'def printSmallestTen(items: list[int], k: int) -> list[int]:',
            '    {{s0}}',
            '    res = []',
            '    for _ in range(k):',
            '        res.append({{s1}})',
            '    return res'
          ],
          slots: {
            s0: { expected: 't_heapify', hint: 'Bottom-up μετατροπή της λίστας σε σωρό επί-τόπου.' },
            s1: { expected: 't_pop', hint: 'Αφαίρεση και επιστροφή της ελάχιστης ρίζας σε O(log n).' }
          },
          tokens: [
            { id: 't_heapify', label: 'heapq.heapify(items)' },
            { id: 't_pop', label: 'heapq.heappop(items)' },
            { id: 't_d1', label: 'items.sort()' },
            { id: 't_d2', label: 'items.pop()' }
          ]
        },
        {
          id: 'drop_02_2',
          unit_id: '02',
          title: 'Drop-In #2: Επιλογή Μικρότερου Παιδιού στο downheap (1-indexed)',
          source_tag: 'Σημείωση 02 — Ενότητα 3.3',
          description: 'Αποφύγετε την παγίδα της ανταλλαγής με το μεγαλύτερο παιδί συμπληρώνοντας τους 1-indexed τύπους.',
          lines: [
            'def downheapStep(arr: list[int], idx: int, n_size: int) -> int:',
            '    left = {{s0}}',
            '    right = {{s1}}',
            '    smaller = left',
            '    if right <= n_size and {{s2}}:',
            '        smaller = right',
            '    return smaller'
          ],
          slots: {
            s0: { expected: 't_left', hint: '1-indexed τύπος αριστερού παιδιού.' },
            s1: { expected: 't_right', hint: '1-indexed τύπος δεξιού παιδιού.' },
            s2: { expected: 't_cmp', hint: 'Επιλέγουμε το δεξιό παιδί μόνο αν είναι αυστηρά μικρότερο από το αριστερό.' }
          },
          tokens: [
            { id: 't_left', label: '2 * idx' },
            { id: 't_right', label: '2 * idx + 1' },
            { id: 't_cmp', label: 'arr[right] < arr[left]' },
            { id: 't_d1', label: '2 * idx + 2' },
            { id: 't_d2', label: 'arr[right] > arr[left]' }
          ]
        }
      ],
      '03': [
        {
          id: 'drop_03_1',
          unit_id: '03',
          title: 'Drop-In #1: Έλεγχος Ξένων Ακολουθιών (M << N)',
          source_tag: 'Φροντιστήριο A — Κεφ. 6 #6',
          description: 'Επιλέξτε τη σωστή ακολουθία για μετατροπή σε σύνολο κατακερματισμού ώστε η μνήμη του set να είναι O(M).',
          lines: [
            'def areDisjoint(seq_m: list[int], seq_n: list[int]) -> bool:',
            '    fast_lookup = {{s0}}',
            '    for elem in {{s1}}:',
            '        if {{s2}}:',
            '            return False',
            '    return True'
          ],
          slots: {
            s0: { expected: 't_setm', hint: 'Μετατρέπουμε σε set τη ΜΙΚΡΟΤΕΡΗ ακολουθία M.' },
            s1: { expected: 't_seqn', hint: 'Σαρώνουμε τα N στοιχεία της μεγαλύτερης ακολουθίας σε O(1) ανά έλεγχο.' },
            s2: { expected: 't_in', hint: 'Έλεγχος ύπαρξης κοινού στοιχείου.' }
          },
          tokens: [
            { id: 't_setm', label: 'set(seq_m)' },
            { id: 't_seqn', label: 'seq_n' },
            { id: 't_in', label: 'elem in fast_lookup' },
            { id: 't_d1', label: 'set(seq_n)' },
            { id: 't_d2', label: 'seq_m' }
          ]
        },
        {
          id: 'drop_03_2',
          unit_id: '03',
          title: 'Drop-In #2: Αναζήτηση με DEFUNCT στη Γραμμική Ανίχνευση',
          source_tag: 'Σημείωση 03 — Ενότητα 3.3',
          description: 'Χειριστείτε σωστά τα κενά κελιά και τους δείκτες DEFUNCT κατά τη σάρωση γραμμικής ανίχνευσης.',
          lines: [
            'def probeFind(table: list, key: int, cap: int) -> int:',
            '    for j in range(cap):',
            '        idx = {{s0}}',
            '        if table[idx] is None:',
            '            {{s1}}',
            '        if table[idx] != "DEFUNCT" and table[idx] == key:',
            '            return idx',
            '    return -1'
          ],
          slots: {
            s0: { expected: 't_lp', hint: 'Βήμα γραμμικής ανίχνευσης modulo χωρητικότητα cap.' },
            s1: { expected: 't_stop', hint: 'Μόνο ένα πραγματικά κενό (None) τερματίζει την αναζήτηση· το DEFUNCT προσπερνάται.' }
          },
          tokens: [
            { id: 't_lp', label: '((key % cap) + j) % cap' },
            { id: 't_stop', label: 'return -1' },
            { id: 't_d1', label: 'continue' },
            { id: 't_d2', label: '(key + j * j) % cap' }
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
            'def findRoot(parent: list[int], x: int) -> int:',
            '    if {{s0}}:',
            '        return x',
            '    {{s1}} = findRoot(parent, parent[x])',
            '    return parent[x]'
          ],
          slots: {
            s0: { expected: 't_root', hint: 'Μία ρίζα έχει δείκτη γονέα στον εαυτό της.' },
            s1: { expected: 't_comp', hint: 'Αποθηκεύουμε την επιστρεφόμενη ρίζα απευθείας ως γονέα του x.' }
          },
          tokens: [
            { id: 't_root', label: 'parent[x] == x' },
            { id: 't_comp', label: 'parent[x]' },
            { id: 't_d1', label: 'parent[x] == 0' },
            { id: 't_d2', label: 'size[x]' }
          ]
        },
        {
          id: 'drop_04_2',
          unit_id: '04',
          title: 'Drop-In #2: Ένωση κατά Μέγεθος (Union by Size)',
          source_tag: 'Σημείωση 04 — Ενότητα 3.2',
          description: 'Προσαρτήστε τη μικρότερη ρίζα κάτω από τη μεγαλύτερη και ενημερώστε το μέγεθος μόνο της νέας ρίζας.',
          lines: [
            'def unionBySize(parent: list[int], size: list[int], u: int, v: int) -> None:',
            '    r_u, r_v = findRoot(parent, u), findRoot(parent, v)',
            '    if {{s0}}:',
            '        return',
            '    if size[r_u] < size[r_v]:',
            '        r_u, r_v = r_v, r_u',
            '    {{s1}}',
            '    size[r_u] += size[r_v]'
          ],
          slots: {
            s0: { expected: 't_same', hint: 'Παγίδα: αν ανήκουν ήδη στο ίδιο σύνολο δεν αλλάζουμε ούτε parent ούτε size!' },
            s1: { expected: 't_attach', hint: 'Ο r_v είναι το μικρότερο δέντρο· ο γονέας του γίνεται ο r_u.' }
          },
          tokens: [
            { id: 't_same', label: 'r_u == r_v' },
            { id: 't_attach', label: 'parent[r_v] = r_u' },
            { id: 't_d1', label: 'parent[r_u] = r_v' },
            { id: 't_d2', label: 'u == v' }
          ]
        }
      ],
      '05': [
        {
          id: 'drop_05_1',
          unit_id: '05',
          title: 'Drop-In #1: Συγχώνευση N Μικρότερων Στοιχείων σε O(N)',
          source_tag: 'Φροντιστήριο A — Κεφ. 8 #6',
          description: 'Συμπληρώστε τη σύγκριση και την αύξηση των δεικτών για τα N μικρότερα στοιχεία από δύο ταξινομημένους πίνακες.',
          lines: [
            'def mergeN(a: list[int], b: list[int], n: int) -> list[int]:',
            '    c = [0] * n',
            '    i, j = 0, 0',
            '    for k in range(n):',
            '        if {{s0}}:',
            '            c[k] = a[i]',
            '            {{s1}}',
            '        else:',
            '            c[k] = b[j]',
            '            j += 1',
            '    return c'
          ],
          slots: {
            s0: { expected: 't_cmp', hint: 'Συγκρίνουμε τα τρέχοντα μέτωπα a[i] και b[j].' },
            s1: { expected: 't_inc', hint: 'Προχωράμε τον δείκτη του πίνακα από τον οποίο πήραμε στοιχείο.' }
          },
          tokens: [
            { id: 't_cmp', label: 'a[i] <= b[j]' },
            { id: 't_inc', label: 'i += 1' },
            { id: 't_d1', label: 'j += 1' },
            { id: 't_d2', label: 'a[i] >= b[j]' }
          ]
        },
        {
          id: 'drop_05_2',
          unit_id: '05',
          title: 'Drop-In #2: Διαμερισμός με Βοηθητικό Πίνακα',
          source_tag: 'Φροντιστήριο A — Κεφ. 8 #7',
          description: 'Τοποθετήστε τα μικρότερα του pivot αριστερά και τα μεγαλύτερα/ίσα δεξιά στον βοηθητικό πίνακα.',
          lines: [
            'def partitionAux(a: list[int]) -> list[int]:',
            '    temp = [0] * len(a)',
            '    pivot = a[-1]',
            '    i, j = 0, len(a) - 1',
            '    for x in a[:-1]:',
            '        if x < pivot:',
            '            temp[i] = x; {{s0}}',
            '        else:',
            '            temp[j] = x; {{s1}}',
            '    {{s2}}',
            '    return temp'
          ],
          slots: {
            s0: { expected: 't_pi', hint: 'Μετακινούμε τον αριστερό δείκτη i προς τα δεξιά.' },
            s1: { expected: 't_pj', hint: 'Μετακινούμε τον δεξιό δείκτη j προς τα αριστερά.' },
            s2: { expected: 't_piv', hint: 'Το pivot τοποθετείται στην τελική του θέση συνάντησης i.' }
          },
          tokens: [
            { id: 't_pi', label: 'i += 1' },
            { id: 't_pj', label: 'j -= 1' },
            { id: 't_piv', label: 'temp[i] = pivot' },
            { id: 't_d1', label: 'j += 1' },
            { id: 't_d2', label: 'temp[0] = pivot' }
          ]
        }
      ],
      '06': [
        {
          id: 'drop_06_1',
          unit_id: '06',
          title: 'Drop-In #1: Κλασματικό Σακίδιο (Ταξινόμηση & Ποσότητα x_i)',
          source_tag: 'Φροντιστήριο A — Κεφ. 10 #3',
          description: 'Συμπληρώστε το κλειδί ταξινόμησης πυκνότητας και τον υπολογισμό κλασματικής ποσότητας.',
          lines: [
            'def fractionalKnapsack(items: list[dict], cap: float) -> float:',
            '    ordered = sorted(items, key={{s0}}, reverse=True)',
            '    total = 0.0',
            '    for it in ordered:',
            '        if cap >= it["w"]:',
            '            total += it["b"]; cap -= it["w"]',
            '        else:',
            '            total += {{s1}}',
            '            break',
            '    return total'
          ],
          slots: {
            s0: { expected: 't_dens', hint: 'Φθίνουσα πυκνότητα αξίας v_i = b_i / w_i.' },
            s1: { expected: 't_frac', hint: 'Παίρνουμε αναλογικά όση χωρητικότητα cap απέμεινε.' }
          },
          tokens: [
            { id: 't_dens', label: 'lambda x: x["b"] / x["w"]' },
            { id: 't_frac', label: 'it["b"] * (cap / it["w"])' },
            { id: 't_d1', label: 'lambda x: x["b"]' },
            { id: 't_d2', label: 'it["w"] / it["b"]' }
          ]
        },
        {
          id: 'drop_06_2',
          unit_id: '06',
          title: 'Drop-In #2: Task Scheduling (Κριτήριο Ταξινόμησης & Συνθήκη Επαναχρησιμοποίησης)',
          source_tag: 'Φροντιστήριο A — Κεφ. 10 #4',
          description: 'Επιλέξτε το κριτήριο ταξινόμησης και τη συνθήκη μη σύγκρουσης μηχανής.',
          lines: [
            'def scheduleMinMachines(tasks: list[tuple[int, int]]) -> int:',
            '    ordered = sorted(tasks, key={{s0}})',
            '    finishes = []',
            '    for start_t, finish_t in ordered:',
            '        if finishes and {{s1}}:',
            '            heapq.heapreplace(finishes, finish_t)',
            '        else:',
            '            heapq.heappush(finishes, finish_t)',
            '    return len(finishes)'
          ],
          slots: {
            s0: { expected: 't_start', hint: 'Για ελαχιστοποίηση μηχανών ταξινομούμε κατά ώρα έναρξης t[0] (ΟΧΙ λήξης t[1]).' },
            s1: { expected: 't_reuse', hint: 'Μία μηχανή επαναχρησιμοποιείται αν η παλιά εργασία τελείωσε <= start_t.' }
          },
          tokens: [
            { id: 't_start', label: 'lambda t: t[0]' },
            { id: 't_reuse', label: 'finishes[0] <= start_t' },
            { id: 't_d1', label: 'lambda t: t[1]' },
            { id: 't_d2', label: 'finishes[0] > start_t' }
          ]
        }
      ],
      '07': [
        {
          id: 'drop_07_1',
          unit_id: '07',
          title: 'Drop-In #1: Γραμμική Συγχώνευση Λιστών',
          source_tag: 'Φροντιστήριο B — Κεφ. 11 #4',
          description: 'Ολοκληρώστε τον βρόχο συγχώνευσης δύο ταξινομημένων λιστών σε χρόνο O(n1 + n2).',
          lines: [
            'def merge(l1: list[int], l2: list[int]) -> list[int]:',
            '    res = []; i = 0; j = 0',
            '    while {{s0}}:',
            '        if l1[i] <= l2[j]:',
            '            res.append(l1[i]); i += 1',
            '        else:',
            '            res.append(l2[j]); j += 1',
            '    return {{s1}}'
          ],
          slots: {
            s0: { expected: 't_cond', hint: 'Και οι δύο λίστες πρέπει να έχουν ακόμη ανεπεξέργαστα στοιχεία.' },
            s1: { expected: 't_tail', hint: 'Επισυνάπτουμε όσα στοιχεία απέμειναν από l1[i:] και l2[j:].' }
          },
          tokens: [
            { id: 't_cond', label: 'i < len(l1) and j < len(l2)' },
            { id: 't_tail', label: 'res + l1[i:] + l2[j:]' },
            { id: 't_d1', label: 'i < len(l1) or j < len(l2)' },
            { id: 't_d2', label: 'res' }
          ]
        },
        {
          id: 'drop_07_2',
          unit_id: '07',
          title: 'Drop-In #2: Σύνθεση 3 Γινομένων Karatsuba',
          source_tag: 'Σημείωση 07 — Ενότητα 3.1',
          description: 'Εφαρμόστε την αλγεβρική ταυτότητα Karatsuba ώστε I * J να υπολογίζεται με 3 αντί 4 πολλαπλασιασμούς.',
          lines: [
            'def combineKaratsuba(p1: int, p2: int, ih: int, il: int, jh: int, jl: int, pow_m: int) -> int:',
            '    p3 = {{s0}}',
            '    mid = {{s1}}',
            '    return p1 * (pow_m ** 2) + mid * pow_m + p2'
          ],
          slots: {
            s0: { expected: 't_p3', hint: 'Το τρίτο γινόμενο πολλαπλασιάζει διαφορές (I_h - I_l) και (J_l - J_h).' },
            s1: { expected: 't_mid', hint: 'Προσθέτοντας p1 + p2 αλληλοαναιρούνται οι όροι -I_h J_h - I_l J_l.' }
          },
          tokens: [
            { id: 't_p3', label: 'karatsuba(ih - il, jl - jh)' },
            { id: 't_mid', label: 'p3 + p1 + p2' },
            { id: 't_d1', label: 'p3 - p1 - p2' },
            { id: 't_d2', label: 'karatsuba(ih, jl)' }
          ]
        }
      ]
    };

    const true_false_drills = {
      '00': [
        { statement: 'Στην Πρόοδο εξετάζονται τα Κεφάλαια 1, 5, 6, 7, 8, 10 και 11 (όχι τα 2, 3, 4, 9, 12–17).', answer: true, explanation: 'Σωστό: Η ύλη της Προόδου καλύπτει αυτά τα 7 κεφάλαια με τις ρητές εξαιρέσεις (1.4.1, 5.5, Chernoff, Λήμμα 6.1, 6.5, 7.3.1, απόδειξη Huffman).' },
        { statement: 'Ο αλγόριθμος Huffman και η πολυπλοκότητά του O(n + d log d) είναι εκτός ύλης Προόδου.', answer: false, explanation: 'Λάθος: Μόνο η τυπική απόδειξη βελτιστότητας (σελ. 294–297) εξαιρείται. Ο αλγόριθμος, η ιχνηλάτηση και το O(n + d log d) εξετάζονται κανονικά.' },
        { statement: 'Η επιμερισμένη ανάλυση (amortized) στηρίζεται σε τυχαίες κατανομές πιθανότητας επί των εισόδων.', answer: false, explanation: 'Λάθος: Η επιμερισμένη ανάλυση είναι ντετερμινιστική στη χειρότερη ακολουθία (χωρίς πιθανότητες).' },
        { statement: 'Το Φράγμα Chernoff και η απόδειξη Ackermann (7.3.1) εξαιρούνται από την Πρόοδο.', answer: true, explanation: 'Σωστό: Καταγράφονται ρητά στον Πίνακα Εξαιρέσεων 2.2 της Ενότητας 00.' }
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
