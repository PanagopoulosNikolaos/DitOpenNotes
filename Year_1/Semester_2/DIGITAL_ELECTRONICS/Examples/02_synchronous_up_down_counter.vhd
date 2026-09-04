-------------------------------------------------------------------------------
-- Synchronous 4-bit up/down binary counter with asynchronous reset,
-- synchronous parallel load, and terminal count output.
-------------------------------------------------------------------------------

library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.NUMERIC_STD.ALL;

entity up_down_counter_4bit is
    port (
        clk      : in  std_logic;
        rst_n    : in  std_logic; -- Asynchronous active-low reset
        load     : in  std_logic; -- Synchronous parallel load enable
        up_down  : in  std_logic; -- '1' for Count Up, '0' for Count Down
        data_in  : in  std_logic_vector(3 downto 0);
        count    : out std_logic_vector(3 downto 0);
        tc       : out std_logic  -- Terminal count asserted on 15 (up) or 0 (down)
    );
end entity up_down_counter_4bit;

architecture behavioral of up_down_counter_4bit is
    signal count_reg : unsigned(3 downto 0);
begin
    process(clk, rst_n)
    begin
        if rst_n = '0' then
            count_reg <= (others => '0');
        elsif rising_edge(clk) then
            if load = '1' then
                count_reg <= unsigned(data_in);
            elsif up_down = '1' then
                count_reg <= count_reg + 1;
            else
                count_reg <= count_reg - 1;
            end if;
        end if;
    end process;

    count <= std_logic_vector(count_reg);

    -- Terminal count logic
    tc <= '1' when (up_down = '1' and count_reg = 15) or
                   (up_down = '0' and count_reg = 0)
              else '0';
end architecture behavioral;

