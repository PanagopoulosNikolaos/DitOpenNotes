library ieee;
use ieee.std_logic_1164.all;

entity D_FF is
  port (
    D    : in  std_logic;
    Clk  : in  std_logic;
    Q    : out std_logic;
    Qbar : out std_logic
  );
end entity D_FF;

architecture Behavioral of D_FF is
  signal state : std_logic := '0';
begin
  process (Clk)
  begin
    if rising_edge(Clk) then
      state <= D;
    end if;
  end process;

  Q    <= state;
  Qbar <= not state;
end architecture Behavioral;