# 10. VHDL - Βασικά

Η VHDL (Very High Speed Integrated Circuit Hardware Description Language) είναι γλώσσα περιγραφής υλικού που επιτρέπει τη μοντελοποίηση και τη σύνθεση ψηφιακών κυκλωμάτων. Αποτελεί το εργαλείο βάσης στη σχεδίαση που κλείνει από την προδιαγραφή RTL έως την προγραμματισμό FPGA.

---

## 1. Εισαγωγή στη VHDL

### 1.1 HDL: Hardware Description Language

Η VHDL δεν είναι γλώσσα προγραμματισμού — περιγράφει υλικό. Οι εντολές εκτελούνται παράλληλα, όχι σειριακά.

### 1.2 Τυποποιήσεις

- **IEEE Std 1076** (1987, 1993, 2008) — η βασική τυποποίηση
- **IEEE Std 1164** — `std_logic` τύπος

### 1.3 Ροή Σχεδίασης

```
RTL Design (VHDL) → Simulation → Synthesis → Place & Route → Bitstream → FPGA
```

---

## 2. Δομή Αρχείου VHDL

### 2.1 Library / Use Clauses

```vhdl
library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;  -- για unsigned/signed
```

### 2.2 Entity

Ορίζει τη διεπαφή (ports) του κυκλώματος:

```vhdl
entity my_and is
    port (
        A : in  std_logic;
        B : in  std_logic;
        Y : out std_logic
    );
end entity my_and;
```

### 2.3 Architecture

Περιγράφει τη συμπεριφορά/δομή. Υπάρχουν τρεις τύποι (Κεφάλαιο 10, Ενότητα 5).

### 2.4 Configuration (Βασικά)

```vhdl
configuration cfg_my_and of my_and is
    for behavioral
    end for;
end configuration cfg_my_and;
```

---

## 3. Τύποι Δεδομένων

### 3.1 `std_logic`

9 τιμές:

| Τιμή | Σημασία |
|:---:|:---|
| `'0'` | Λογικό 0 |
| `'1'` | Λογικό 1 |
| `'Z'` | Ανοιχτή είσοδος (high impedance) |
| `'X'` | Άγνωστο |
| `'U'` | Αρχικοποίηση (uninitialized) |
| `'W'` | Weak 0 |
| `'L'` | Pull-down |
| `'H'` | Pull-up |
| `'-'` | Don't care |

### 3.2 `std_logic_vector(n downto 0)`

Διάνυσμα `std_logic`:

```vhdl
signal bus_data : std_logic_vector(7 downto 0);
```

### 3.3 `integer`, `natural`, `positive`

```vhdl
signal count : integer range 0 to 15;  -- 4-bit counter range
```

### 3.4 `boolean`, `bit`, `bit_vector`

- `boolean`: `true` / `false`
- `bit`: `'0'` / `'1'` (δεν υποστηρίζει `'Z'`)
- `bit_vector`: διάνυσμα bit

### 3.5 `signed`, `unsigned`

Από `ieee.numeric_std`:
- `unsigned`: απρόσημος αριθμός
- `signed`: πρόσημος αριθμός (2's complement)

---

## 4. Τελεστές

### 4.1 Λογικοί

`and`, `or`, `not`, `nand`, `nor`, `xor`, `xnor`

### 4.2 Αριθμητικοί

`+`, `-`, `*`, `/` (απαιτούν `numeric_std`)

### 4.3 Σύγκρισης

`=`, `/=`, `<`, `>`, `<=`, `>=`

### 4.4 Ολίσθησης

`shift_left`, `shift_right`, `rotate_left`, `rotate_right`

### 4.5 Συνένωση

```vhdl
Y <= A & B;  -- concatenation
```

---

## 5. Στυλ Αρχιτεκτονικής

### 5.1 Behavioral (Συμπεριφορικό)

Χρήση `process`, `if-else`, `case`:

```vhdl
architecture behavioral of my_and is
begin
    process(A, B)
    begin
        if A = '1' and B = '1' then
            Y <= '1';
        else
            Y <= '0';
        end if;
    end process;
end behavioral;
```

### 5.2 Dataflow (Ροή Δεδομένων)

Ταυτόχρονες αναθέσεις:

```vhdl
architecture dataflow of my_and is
begin
    Y <= A and B;
end dataflow;
```

### 5.3 Structural (Δομικό)

Component instantiation:

```vhdl
architecture structural of my_circuit is
    component my_and
        port(A, B: in std_logic; Y: out std_logic);
    end component;
    signal s1 : std_logic;
begin
    U1: my_and port map (A => A, B => B, Y => s1);
end structural;
```

---

## 6. Ταυτόχρονες Εντολές (Concurrent Statements)

### 6.1 Signal Assignment

```vhdl
Y <= A and B;  -- εκτελείται πάντα όταν αλλάζει A ή B
```

### 6.2 `when-else`

```vhdl
Y <= A when S = '0' else B;  -- 2-to-1 MUX
```

### 6.3 `with-select`

```vhdl
with S select
    Y <= A when "00",
         B when "01",
         C when "10",
         D when others;
```

---

## 7. Ακολουθιακές Εντολές (Εντός Process)

### 7.1 `if-then-elsif-else`

```vhdl
process(clk)
begin
    if rising_edge(clk) then
        if sel = "00" then
            Q <= A;
        elsif sel = "01" then
            Q <= B;
        else
            Q <= C;
        end if;
    end if;
end process;
```

### 7.2 `case-when`

```vhdl
case sel is
    when "00" => Q <= A;
    when "01" => Q <= B;
    when others => Q <= (others => '0');
end case;
```

### 7.3 Loops

```vhdl
for i in 0 to 7 loop
    temp(i) := input(7-i);
end loop;
```

### 7.4 Variable vs Signal

- **Signal (`<=`):** Ενημερώνεται στο τέλος του process (delta cycle)
- **Variable (`:=`):** Ενημερώνεται άμεσα εντός process

> **[Key Insight]** Σφάλμα χρήστη: αν χρησιμοποιήσετε signal αντί variable σε ένα process, η τιμή δεν "αλλάζει" μέσα στην ίδια εκτέλεση του process — αυτό οδηγεί σε λανθασμένη συμπεριφορά.

---

## Solved Exercises

### Exercise 1: 2-to-1 MUX με Dataflow

**Problem:** Να υλοποιηθεί 2-to-1 MUX με dataflow.

**Solution:**
```vhdl
Y <= A when S = '0' else B;
```

### Exercise 2: 4-Bit Register με Behavioral

**Problem:** Να υλοποιηθεί 4-bit register με parallel load.

**Solution:**
```vhdl
process(clk)
begin
    if rising_edge(clk) then
        if load = '1' then
            Q <= D;
        end if;
    end if;
end process;
```

### Exercise 3: 3-to-8 Decoder

**Problem:** Να υλοποιηθεί 3-to-8 decoder.

**Solution:**
```vhdl
architecture behavioral of decoder3to8 is
begin
    process(A)
    begin
        Y <= (others => '0');
        case A is
            when "000" => Y(0) <= '1';
            when "001" => Y(1) <= '1';
            when others => null;
        end case;
    end process;
end behavioral;
```

### Exercise 4: Half Adder Structural

**Problem:** Να υλοποιηθεί half adder structural.

**Solution:**
```vhdl
architecture structural of half_adder is
begin
    S <= A XOR B;
    C <= A AND B;
end structural;
```

### Exercise 5: Signal vs Variable

**Problem:** Να εξηγηθεί η διαφορά.

**Solution:**
```vhdl
-- Signal: η τιμή δεν αλλάζει μέσα στο process
process(clk)
begin
    if rising_edge(clk) then
        a_sig <= '1';
        b_sig <= a_sig;  -- b_sig = '0' (παλιά τιμή)
    end if;
end process;

-- Variable: η τιμή αλλάζει άμεσα
process(clk)
    variable v : std_logic := '0';
begin
    if rising_edge(clk) then
        v := '1';
        -- v = '1' τώρα
    end if;
end process;
```

### Exercise 6: Full Adder Dataflow

**Problem:** Να υλοποιηθεί full adder με dataflow.

**Solution:**
```vhdl
S <= A XOR B XOR Cin;
Cout <= (A AND B) OR (A AND Cin) OR (B AND Cin);
```

### Exercise 7: Priority Encoder Behavioral

**Problem:** Να υλοποιηθεί 4-to-2 priority encoder.

**Solution:**
```vhdl
process(D)
begin
    if D(3) = '1' then
        Y <= "11";
    elsif D(2) = '1' then
        Y <= "10";
    elsif D(1) = '1' then
        Y <= "01";
    else
        Y <= "00";
    end if;
end process;
```

### Exercise 8: Tri-State Buffer

**Problem:** Να υλοποιηθεί tri-state buffer.

**Solution:**
```vhdl
Y <= A when EN = '1' else 'Z';
```

---

## Exam Tip: Sensitivity List

Για **combinational logic**, η sensitivity list πρέπει να περιλαμβάνει όλες τις εισόδους. Αν λείπει κάποια είσοδος, η συμπεριφορά είναι απρόβλεπτη. Σε process για `rising_edge(clk)`, η sensitivity list είναι `process(clk)` (και `process(clk, rst)` αν υπάρχει async reset). Ποτέ `process(all)` σε VHDL-93 — χρησιμοποιείται `process(all)` στο VHDL-2008.