# 11. VHDL - Προχωρημένο

Η ενότητα αυτή επεκτείνει τα βασικά της VHDL σε προχωρημένες τεχνικές που απαιτούνται για τη σχεδίαση πολύπλοκων ψηφιακών συστημάτων: μοντελοποίηση συνδυαστικών και ακολουθιακών κυκλωμάτων, FSM, generics, packages, functions, testbenches και σύνθεση RTL.

---

## 1. Μοντελοποίηση Συνδυαστικών Κυκλωμάτων

### 1.1 Πύλες, MUX, Decoder

```vhdl
-- 2-to-1 MUX με when-else
Y <= A when S = '0' else B;

-- 4-to-1 MUX με with-select
with S select
    Y <= A when "00",
         B when "01",
         C when "10",
         D when others;
```

### 1.2 Full Adder: Behavioral, Dataflow, Structural

```vhdl
-- Behavioral
process(A, B, Cin)
begin
    S <= A XOR B XOR Cin;
    Cout <= (A AND B) OR (A AND Cin) OR (B AND Cin);
end process;

-- Dataflow
S <= A XOR B XOR Cin;
Cout <= (A AND B) OR (A AND Cin) OR (B AND Cin);
```

### 1.3 Sensitivity List

Για combinational: όλες οι είσοδοι. Για sequential: μόνο `clk` (και `rst` αν async).

### 1.4 Ανεπιθύμητα Latches

Αν σε `process` υπάρχει `if` χωρίς `else`, το synthesis tool μπορεί να παράγει latch. Αποφυγή: προσθήκη `else` ή χρήση default value.

---

## 2. Μοντελοποίηση Ακολουθιακών Κυκλωμάτων

### 2.1 D Flip-Flop

```vhdl
process(clk)
begin
    if rising_edge(clk) then
        Q <= D;
    end if;
end process;
```

### 2.2 Σύγχρονο vs Ασύγχρονο Reset/Preset

**Σύγχρονος reset:**
```vhdl
process(clk)
begin
    if rising_edge(clk) then
        if rst = '1' then
            Q <= (others => '0');
        elsif load = '1' then
            Q <= D;
        end if;
    end if;
end process;
```

**Ασύγχρονος reset:**
```vhdl
process(clk, rst)
begin
    if rst = '1' then
        Q <= (others => '0');
    elsif rising_edge(clk) then
        if load = '1' then
            Q <= D;
        end if;
    end if;
end process;
```

> **[Key Insight]** Ο ασύγχρονος reset είναι πιο γρήγορος αλλά πιο επικίνδυνος (μπορεί να προκαλέσει metastability). Η νεότερη σύγκλιση προτιμά σύγχρονο reset.

### 2.3 Καταχωρητές και Shift Registers

```vhdl
-- 4-bit shift right register
process(clk)
begin
    if rising_edge(clk) then
        Q <= Din & Q(3 downto 1);  -- shift right
    end if;
end process;
```

### 2.4 Μετρητές

```vhdl
-- mod-10 up counter
process(clk)
begin
    if rising_edge(clk) then
        if count = 9 then
            count <= 0;
        else
            count <= count + 1;
        end if;
    end if;
end process;
```

---

## 3. FSM σε VHDL

### 3.1 State Type

```vhdl
type state_type is (S0, S1, S2, S3);
signal current_state, next_state : state_type;
```

### 3.2 1-Process FSM

```vhdl
process(clk)
begin
    if rising_edge(clk) then
        case current_state is
            when S0 =>
                if input = '1' then
                    current_state <= S1;
                end if;
            when S1 =>
                -- ...
        end case;
    end if;
end process;
```

### 3.3 2-Process FSM

Ένα process για state register, ένα για next-state/output logic:

```vhdl
-- Process 1: State register
process(clk, rst)
begin
    if rst = '1' then
        current_state <= S0;
    elsif rising_edge(clk) then
        current_state <= next_state;
    end if;
end process;

-- Process 2: Next state + output
process(current_state, input)
begin
    case current_state is
        when S0 =>
            if input = '1' then
                next_state <= S1;
            else
                next_state <= S0;
            end if;
            output <= '0';
    end case;
end process;
```

### 3.4 3-Process FSM

Ένα για state register, ένα για next-state, ένα για outputs. Πιο ξεκάθαρη δομή.

### 3.5 One-Hot Encoding

```vhdl
attribute fsm_encoding : string;
attribute fsm_encoding of current_state : signal is "one-hot";
```

---

## 4. Γενικοί Σχεδιασμοί (Generics)

### 4.1 Generic Parameters

```vhdl
entity n_adder is
    generic (N : integer := 8);
    port (
        A, B : in  std_logic_vector(N-1 downto 0);
        Sum  : out std_logic_vector(N downto 0)
    );
end entity;
```

### 4.2 N-bit Register με Generic

```vhdl
entity n_register is
    generic (N : integer := 8);
    port (
        clk, load : in  std_logic;
        D : in  std_logic_vector(N-1 downto 0);
        Q : out std_logic_vector(N-1 downto 0)
    );
end entity;
```

### 4.3 Generate Statement

```vhdl
gen_bits: for i in 0 to N-1 generate
    U: xor_gate port map (A => A(i), B => B(i), Y => Y(i));
end generate;
```

---

## 5. Πακέτα & Βιβλιοθήκες

### 5.1 Package Definition

```vhdl
package my_types is
    constant N : integer := 8;
    type word_t is std_logic_vector(N-1 downto 0);
    function reverse(x : word_t) return word_t;
end package my_types;
```

### 5.2 ieee.numeric_std

```vhdl
use ieee.numeric_std.all;

signal a, b : unsigned(7 downto 0);
signal sum  : unsigned(8 downto 0);
sum <= resize(a, 9) + resize(b, 9);
```

> **[Key Insight]** Χρησιμοποιήστε πάντα `ieee.numeric_std` αντί `ieee.std_logic_arith`. Το `numeric_std` είναι IEEE standard, το `std_logic_arith` είναι third-party.

---

## 6. Subprograms

### 6.1 Functions

```vhdl
function and_reduce(x : std_logic_vector) return std_logic is
    variable result : std_logic := '1';
begin
    for i in x'range loop
        result := result and x(i);
    end loop;
    return result;
end function;
```

### 6.2 Procedures

```vhdl
procedure swap(a, b : inout std_logic_vector(7 downto 0)) is
    variable temp : std_logic_vector(7 downto 0);
begin
    temp := a;
    a := b;
    b := temp;
end procedure;
```

---

## 7. Testbenches

### 7.1 Entity χωρίς Ports

```vhdl
entity tb_my_design is
end entity tb_my_design;
```

### 7.2 Component Instantiation του DUT

```vhdl
DUT: my_design port map (
    clk => clk,
    A => A,
    Y => Y
);
```

### 7.3 Παραγωγή Ρολογιού

```vhdl
clk_process: process
begin
    clk <= '0'; wait for 5 ns;
    clk <= '1'; wait for 5 ns;
end process;
```

### 7.4 Assert / Report

```vhdl
assert Y = expected
    report "Mismatch at time " & time'image(now)
    severity error;
```

### 7.5 Simulation vs Synthesis

Non-synthesizable constructs: `wait for`, `report`, `assert`, `file I/O`.

---

## 8. RTL Σύνθεση

### 8.1 Synthesizable Subset

- `process(clk)` → Flip-Flop
- `process(a, b)` → Combinational logic
- Δεν συντίθεται: `wait for`, μη απλές δομές βρόχων

### 8.2 Setup/Hold Time

- **Setup time ($t_{su}$):** Χρόνος πριν την ακμή που τα δεδομένα πρέπει να είναι σταθερά
- **Hold time ($t_h$):** Χρόνος μετά την ακμή που τα δεδομένα πρέπει να παραμείνουν σταθερά

### 8.3 Critical Path

Το πιο αργό μονοπάτι στο κύκλωμα — καθορίζει τη μέγιστη συχνότητα ρολογιού.

---

## Solved Exercises

### Exercise 1: 2-Process FSM σε VHDL

**Problem:** Να υλοποιηθεί FSM ανιχνευτή "101" με 2-process στυλ.

**Solution:**
```vhdl
-- State register
process(clk, rst)
begin
    if rst = '1' then
        current_state <= S0;
    elsif rising_edge(clk) then
        current_state <= next_state;
    end if;
end process;

-- Next state + output
process(current_state, x)
begin
    output <= '0';
    case current_state is
        when S0 => next_state <= S1 when x = '1' else S0;
        when S1 => next_state <= S2 when x = '0' else S1;
        when S2 =>
            if x = '1' then
                next_state <= S1;
                output <= '1';
            else
                next_state <= S0;
            end if;
    end case;
end process;
```

### Exercise 2: N-bit Adder με Generic

**Problem:** Να σχεδιαστεί N-bit adder με generic.

**Solution:**
```vhdl
entity n_adder is
    generic (N : integer := 8);
    port (A, B : in std_logic_vector(N-1 downto 0);
          Cout : out std_logic;
          Sum  : out std_logic_vector(N-1 downto 0));
end entity;
```

### Exercise 3: Testbench για Full Adder

**Problem:** Να γραφεί testbench για full adder.

**Solution:**
```vhdl
entity tb_full_adder is end entity;
architecture sim of tb_full_adder is
    signal A, B, Cin, S, Cout : std_logic;
begin
    DUT: entity work.full_adder port map (A, B, Cin, S, Cout);
    stim: process
    begin
        A <= '0'; B <= '0'; Cin <= '0'; wait for 10 ns;
        assert (S = '0' and Cout = '0');
        -- ... all 8 combinations
    end process;
end architecture;
```

### Exercise 4: Generate Statement

**Problem:** Να χρησιμοποιηθεί generate για N-bit inverter chain.

**Solution:**
```vhdl
gen: for i in 0 to N-1 generate
    inv_i: entity work.inverter port map (A => input(i), Y => output(i));
end generate;
```

### Exercise 5: Shift Register Structural

**Problem:** Να υλοποιηθεί 4-bit SIPO shift register structural.

**Solution:**
```vhdl
gen_ff: for i in 0 to 3 generate
    FF: d_ff port map (clk => clk, D => D_in(i), Q => Q(i));
end generate;
```
με σωστή σύνδεση: `D_in(0) <= serial_in`, `D_in(i) <= Q(i-1)` για $i > 0$.

### Exercise 6: Variable σε Process

**Problem:** Να εξηγηθεί γιατί η variable χρησιμοποιείται σε accumulator.

**Solution:**
```vhdl
process(clk)
    variable acc : unsigned(15 downto 0) := (others => '0');
begin
    if rising_edge(clk) then
        acc := acc + unsigned(input);  -- άμεση ενημέρωση
        Q <= std_logic_vector(acc);
    end if;
end process;
```

### Exercise 7: Package με Constants

**Problem:** Να δημιουργηθεί package με σταθερές για project.

**Solution:**
```vhdl
package project_constants is
    constant DATA_WIDTH : integer := 8;
    constant ADDR_WIDTH : integer := 4;
    constant CLK_PERIOD : time := 10 ns;
end package;
```

### Exercise 8: Async vs Sync Reset συγκριση

**Problem:** Πότε προτιμάται async και πότε sync reset;

**Solution:**
- **Async:** Όταν η επαναφορά πρέπει να γίνει άμεσα χωρίς clock (εξωτερικό επεισόδιο)
- **Sync:** Όταν η επαναφορά πρέπει να συγχρονιστεί με τον clock (πιο ασφαλής, πολύχρηστη σε σύγχρονα συστήματα)

---

## Exam Tip: Non-Synthesizable Constructs

Σε εξέταση, αν σας ζητηθεί να γράψετε testbench, χρησιμοποιήστε `wait for` για χρονισμό και `assert` για έλεγχο. Αν σας ζητηθεί synthesizable κώδικας, ποτέ `wait for` μέσα σε process — χρησιμοποιήστε `rising_edge(clk)`. Αυτή η διάκριση είναι θεμελιώδης στις εξετάσεις.