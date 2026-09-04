-------------------------------------------------------------------------------
-- Combinational 4-bit ripple-carry adder/subtractor with overflow detection.
-- When sub = '0', calculates A + B.
-- When sub = '1', calculates A - B using two's complement.
-------------------------------------------------------------------------------

library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

entity adder_subtractor_4bit is
    port (
        a_in     : in  std_logic_vector(3 downto 0);
        b_in     : in  std_logic_vector(3 downto 0);
        sub_ctrl : in  std_logic; -- '0' for ADD, '1' for SUB
        sum_out  : out std_logic_vector(3 downto 0);
        cout     : out std_logic;
        overflow : out std_logic
    );
end entity adder_subtractor_4bit;

architecture structural of adder_subtractor_4bit is
    signal b_xor : std_logic_vector(3 downto 0);
    signal carry : std_logic_vector(4 downto 0);
begin
    -- Initial carry-in equals sub_ctrl for two's complement increment
    carry(0) <= sub_ctrl;

    -- Invert B bits conditionally based on sub_ctrl
    gen_xor: for i in 0 to 3 generate
        b_xor(i) <= b_in(i) xor sub_ctrl;
    end generate gen_xor;

    -- Full adder stages
    gen_fa: for i in 0 to 3 generate
        sum_out(i) <= a_in(i) xor b_xor(i) xor carry(i);
        carry(i + 1) <= (a_in(i) and b_xor(i)) or (carry(i) and (a_in(i) xor b_xor(i)));
    end generate gen_fa;

    cout <= carry(4);

    -- Overflow occurs when carry into sign bit differs from carry out
    overflow <= carry(4) xor carry(3);
end architecture structural;

