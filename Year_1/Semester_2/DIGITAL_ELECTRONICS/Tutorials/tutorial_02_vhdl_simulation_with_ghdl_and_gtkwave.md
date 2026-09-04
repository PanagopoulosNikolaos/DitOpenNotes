# Tutorial 02: VHDL Simulation Workflow with GHDL and GTKWave

## Context and Grounding
This tutorial guides students through writing synthesizable VHDL entities, constructing testbenches with simulated clock processes, compiling with the open-source GHDL toolchain, and inspecting digital waveforms in GTKWave. It directly grounds `Resources/Notes/10_vhdl_basics.md` and `Examples/VHDL_CODE_EXEC/`.

---

## 1. Toolchain Prerequisites
On a standard Linux environment, verify GHDL and GTKWave installation:
```bash
ghdl --version
gtkwave --version
```

---

## 2. Design Under Test (DUT): 4-Bit Register with Asynchronous Reset

Create `reg4.vhd`:
```vhdl
library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

entity reg4 is
    port (
        clk   : in  std_logic;
        rst_n : in  std_logic;
        load  : in  std_logic;
        d     : in  std_logic_vector(3 downto 0);
        q     : out std_logic_vector(3 downto 0)
    );
end entity reg4;

architecture behavioral of reg4 is
begin
    process(clk, rst_n)
    begin
        if rst_n = '0' then
            q <= "0000";
        elsif rising_edge(clk) then
            if load = '1' then
                q <= d;
            end if;
        end if;
    end process;
end architecture behavioral;
```

---

## 3. Testbench Entity Construction

Create `reg4_tb.vhd`:
```vhdl
library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

entity reg4_tb is
end entity reg4_tb;

architecture sim of reg4_tb is
    signal clk_tb   : std_logic := '0';
    signal rst_n_tb : std_logic := '0';
    signal load_tb  : std_logic := '0';
    signal d_tb     : std_logic_vector(3 downto 0) := "0000";
    signal q_tb     : std_logic_vector(3 downto 0);

    constant CLK_PERIOD : time := 20 ns;
begin
    -- Instantiate Design Under Test
    uut: entity work.reg4
        port map (
            clk   => clk_tb,
            rst_n => rst_n_tb,
            load  => load_tb,
            d     => d_tb,
            q     => q_tb
        );

    -- Clock Generation Process
    clk_process: process
    begin
        while now < 200 ns loop
            clk_tb <= '0';
            wait for CLK_PERIOD / 2;
            clk_tb <= '1';
            wait for CLK_PERIOD / 2;
        end loop;
        wait;
    end process;

    -- Stimulus Generation Process
    stim_process: process
    begin
        -- Assert asynchronous reset
        rst_n_tb <= '0';
        wait for 25 ns;
        rst_n_tb <= '1';

        -- Apply data without load
        d_tb <= "1010";
        load_tb <= '0';
        wait for 30 ns;

        -- Assert load
        load_tb <= '1';
        wait for 20 ns;
        load_tb <= '0';

        -- Apply new data with load
        d_tb <= "1100";
        wait for 10 ns;
        load_tb <= '1';
        wait for 20 ns;
        load_tb <= '0';

        wait;
    end process;
end architecture sim;
```

---

## 4. Compilation, Simulation, and Waveform Dump

Execute the following commands in the terminal:

```bash
# Analyze design and testbench
ghdl -a reg4.vhd
ghdl -a reg4_tb.vhd

# Elaborate top-level testbench
ghdl -e reg4_tb

# Run simulation and export VCD waveform file
ghdl -r reg4_tb --vcd=waveform.vcd --stop-time=200ns

# Launch waveform viewer
gtkwave waveform.vcd
```

In GTKWave, inspect that `q_tb` resets to `"0000"` asynchronously on `rst_n_tb = '0'`, ignores `d_tb` when `load_tb = '0'`, and updates to `d_tb` on the rising edge of `clk_tb` when `load_tb = '1'`.

