library ieee;
use ieee.std_logic_1164.all;

entity SR_Latch is
  port (
    S    : in  std_logic;
    R    : in  std_logic;
    Q    : out std_logic;
    Qbar : out std_logic
  );
end entity SR_Latch;

architecture Behavioral of SR_Latch is
  signal state : std_logic := '0';
begin
  process (S, R)
  begin
    if S = '1' and R = '0' then
      state <= '1';
    elsif S = '0' and R = '1' then
      state <= '0';
    elsif S = '1' and R = '1' then
      state <= 'X';  -- Undefined state
    end if;
  end process;

  Q    <= state;
  Qbar <= not state;
end architecture Behavioral;