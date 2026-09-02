# Εργαστηριακός Οδηγός 2: Προσομοίωση VHDL με GHDL και Προβολή Κυματομορφών με GTKWave

## 1. Σκοπός Εργαστηρίου
Εκμάθηση της ροής εργασίας (workflow) προσομοίωσης ψηφιακών σχεδίων VHDL ανοικτού κώδικα με χρήση του μεταγλωττιστή `GHDL` και του αναλυτή κυματομορφών `GTKWave`.

---

## 2. Κώδικας Σχεδίασης: 4-bit Σύγχρονος Μετρητής (Up-Counter)

Αποθηκεύστε ως `counter_4bit.vhd`:

```vhdl
library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.NUMERIC_STD.ALL;

entity counter_4bit is
    Port (
        clk    : in  STD_LOGIC;
        reset  : in  STD_LOGIC;
        enable : in  STD_LOGIC;
        count  : out STD_LOGIC_VECTOR(3 downto 0)
    );
end counter_4bit;

architecture Behavioral of counter_4bit is
    signal count_reg : unsigned(3 downto 0) := (others => '0');
begin
    process(clk, reset)
    begin
        if reset = '1' then
            count_reg <= (others => '0');
        elsif rising_edge(clk) then
            if enable = '1' then
                count_reg <= count_reg + 1;
            end if;
        end if;
    end process;

    count <= std_logic_vector(count_reg);
end Behavioral;
```

---

## 3. Testbench VHDL

Αποθηκεύστε ως `counter_4bit_tb.vhd`:

```vhdl
library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

entity counter_4bit_tb is
end counter_4bit_tb;

architecture Sim of counter_4bit_tb is
    signal clk    : STD_LOGIC := '0';
    signal reset  : STD_LOGIC := '1';
    signal enable : STD_LOGIC := '0';
    signal count  : STD_LOGIC_VECTOR(3 downto 0);

    constant CLK_PERIOD : time := 10 ns;
begin
    uut: entity work.counter_4bit
        port map (clk => clk, reset => reset, enable => enable, count => count);

    clk_process: process
    begin
        clk <= '0';
        wait for CLK_PERIOD / 2;
        clk <= '1';
        wait for CLK_PERIOD / 2;
    end process;

    stim_process: process
    begin
        wait for 20 ns;
        reset <= '0';
        enable <= '1';
        wait for 200 ns;
        enable <= '0';
        wait for 50 ns;
        wait;
    end process;
end Sim;
```

---

## 4. Εντολές Μεταγλώττισης και Προσομοίωσης

```bash
# Ανάλυση και μεταγλώττιση
ghdl -a counter_4bit.vhd counter_4bit_tb.vhd

# Δημιουργία εκτελέσιμου προσομοίωσης
ghdl -e counter_4bit_tb

# Εκτέλεση και παραγωγή αρχείου κυματομορφών VCD
ghdl -r counter_4bit_tb --vcd=wave.vcd --stop-time=300ns

# Προβολή κυματομορφών στο GTKWave
gtkwave wave.vcd
```

