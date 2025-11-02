library ieee;
use ieee.std_logic_1164.all;

entity JK_FF is
  port (
    J    : in  std_logic;
    K    : in  std_logic;
    Clk  : in  std_logic;
    Q    : out std_logic;
    Qbar : out std_logic
  );
end entity JK_FF;

architecture Behavioral of JK_FF is
  signal state : std_logic := '0';
begin
  process (Clk)
  begin
    if rising_edge(Clk) then
      if J = '0' and K = '0' then
        -- Hold state
        state <= state;
      elsif J = '0' and K = '1' then
        -- Reset
        state <= '0';
      elsif J = '1' and K = '0' then
        -- Set
        state <= '1';
      else  -- J = '1' and K = '1'
        -- Toggle
        state <= not state;
      end if;
    end if;
  end process;

  Q    <= state;
  Qbar <= not state;
end architecture Behavioral;