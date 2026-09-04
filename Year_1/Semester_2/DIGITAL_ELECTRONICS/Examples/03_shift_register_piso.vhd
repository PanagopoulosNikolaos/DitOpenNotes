-- Parallel-In Serial-Out (PISO) 4-bit Shift Register
-- Demonstrates synchronous parallel loading and serial bit shifting in VHDL.

library ieee;
use ieee.std_logic_1164.all;

entity shift_register_piso is
    port (
        clk         : in  std_logic;
        rst         : in  std_logic;
        load_enable : in  std_logic;
        shift_in    : in  std_logic;
        parallel_in : in  std_logic_vector(3 downto 0);
        serial_out  : out std_logic
    );
end entity shift_register_piso;

architecture behavioral of shift_register_piso is
    signal shift_reg : std_logic_vector(3 downto 0);
begin
    process(clk)
    begin
        if rising_edge(clk) then
            if rst = '1' then
                shift_reg <= (others => '0'); -- Resets register contents to zero
            elsif load_enable = '1' then
                shift_reg <= parallel_in;     -- Latches 4-bit parallel data word
            else
                shift_reg <= shift_in & shift_reg(3 downto 1); -- Shifts bits rightward
            end if;
        end if;
    end process;

    serial_out <= shift_reg(0); -- Exposes least significant bit as serial stream
end architecture behavioral;

