# 10. VHDL - Basics

VHDL (Very High Speed Integrated Circuit Hardware Description Language) is a hardware description language that enables the modeling and synthesis of digital circuits. It is the foundational tool in design, from RTL specification to FPGA programming.

---

## 1. Introduction to VHDL

### 1.1 HDL: Hardware Description Language

VHDL is not a programming language — it describes hardware. Commands are executed in parallel, not sequentially.

### 1.2 Standards

- **IEEE Std 1076** (1987, 1993, 2008) — the basic standard
- **IEEE Std 1164** — `std_logic` type

### 1.3 Design Flow

```
RTL Design (VHDL) → Simulation → Synthesis → Place & Route → Bitstream → FPGA
```

---

## 2. VHDL File Structure

### 2.1 Library / Use Clauses

```vhdl
library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;  -- for unsigned/signed
```

### 2.2 Entity

Defines the interface (ports) of the circuit:

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

Describes the behavior/structure. There are three types (Chapter 10, Section 5).

### 2.4 Configuration (Basics)

```vhdl
configuration cfg_my_and of my_and is
    for behavioral
    end for;
end configuration cfg_my_and;
```

---

## 3. Data Types

### 3.1 `std_logic`

9 values:

| Value | Meaning |
|:---:|:---|
| `'0'` | Logic 0 |
| `'1'` | Logic 1 |
| `'Z'` | High impedance |
| `'X'` | Unknown |
| `'U'` | Uninitialized |
| `'W'` | Weak 0 |
| `'L'` | Pull-down |
| `'H'` | Pull-up |
| `'-'` | Don't care |

### 3.2 `std_logic_vector(n downto 0)`

Vector of `std_logic`:

```vhdl
signal bus_data : std_logic_vector(7 downto 0);
```

### 3.3 `integer`, `natural`, `positive`

```vhdl
signal count : integer range 0 to 15;  -- 4-bit counter range
```

### 3.4 `boolean`, `bit`, `bit_vector`

- `boolean`: `true` / `false`
- `bit`: `'0'` / `'1'` (does not support `'Z'`)
- `bit_vector`: vector of bits

### 3.5 `signed`, `unsigned`

From `ieee.numeric_std`:
- `unsigned`: unsigned number
- `signed`: signed number (2's complement)

---

## 4. Operators

### 4.1 Logical

`and`, `or`, `not`, `nand`, `nor`, `xor`, `xnor`

### 4.2 Arithmetic

`+`, `-`, `*`, `/` (require `numeric_std`)

### 4.3 Comparison

`=`, `/=`, `<`, `>`, `<=`, `>=`

### 4.4 Shift

`shift_left`, `shift_right`, `rotate_left`, `rotate_right`

### 4.5 Concatenation

```vhdl
Y <= A & B;  -- concatenation
```

---

## 5. Architecture Styles

### 5.1 Behavioral

Using `process`, `if-else`, `case`:

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

### 5.2 Dataflow

Concurrent assignments:

```vhdl
architecture dataflow of my_and is
begin
    Y <= A and B;
end dataflow;
```

### 5.3 Structural

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

## 6. Concurrent Statements

### 6.1 Signal Assignment

```vhdl
Y <= A and B;  -- executes whenever A or B changes
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

## 7. Sequential Statements (Inside Process)

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

- **Signal (`<=`):** Updated at the end of the process (delta cycle)
- **Variable (`:=`):** Updated immediately within process

> **[Key Insight]** Common user error: if you use signal instead of variable in a process, the value does not "change" within the same execution of the process — this leads to incorrect behavior.

---

## Solved Exercises

### Exercise 1: 2-to-1 MUX with Dataflow

**Problem:** Implement a 2-to-1 MUX with dataflow.

**Solution:**
```vhdl
Y <= A when S = '0' else B;
```

### Exercise 2: 4-Bit Register with Behavioral

**Problem:** Implement a 4-bit register with parallel load.

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

**Problem:** Implement a 3-to-8 decoder.

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

**Problem:** Implement a half adder structurally.

**Solution:**
```vhdl
architecture structural of half_adder is
begin
    S <= A XOR B;
    C <= A AND B;
end structural;
```

### Exercise 5: Signal vs Variable

**Problem:** Explain the difference.

**Solution:**
```vhdl
-- Signal: the value does not change inside the process
process(clk)
begin
    if rising_edge(clk) then
        a_sig <= '1';
        b_sig <= a_sig;  -- b_sig = '0' (old value)
    end if;
end process;

-- Variable: the value changes immediately
process(clk)
    variable v : std_logic := '0';
begin
    if rising_edge(clk) then
        v := '1';
        -- v = '1' now
    end if;
end process;
```

### Exercise 6: Full Adder Dataflow

**Problem:** Implement a full adder with dataflow.

**Solution:**
```vhdl
S <= A XOR B XOR Cin;
Cout <= (A AND B) OR (A AND Cin) OR (B AND Cin);
```

### Exercise 7: Priority Encoder Behavioral

**Problem:** Implement a 4-to-2 priority encoder.

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

**Problem:** Implement a tri-state buffer.

**Solution:**
```vhdl
Y <= A when EN = '1' else 'Z';
```

---

## Exam Tip: Sensitivity List

For **combinational logic**, the sensitivity list must include all inputs. If any input is missing, the behavior is unpredictable. In a process for `rising_edge(clk)`, the sensitivity list is `process(clk)` (and `process(clk, rst)` if there is an async reset). Never use `process(all)` in VHDL-93 — `process(all)` is used in VHDL-2008.
