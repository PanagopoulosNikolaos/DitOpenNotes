-- Synchronous Moore Finite State Machine for Sequence Detection ('101')
-- Demonstrates two-process FSM architecture with enumerated state types.

library ieee;
use ieee.std_logic_1164.all;

entity fsm_sequence_detector is
    port (
        clk         : in  std_logic;
        rst         : in  std_logic;
        serial_in   : in  std_logic;
        detected    : out std_logic
    );
end entity fsm_sequence_detector;

architecture behavioral of fsm_sequence_detector is
    type StateType is (State_IDLE, State_GOT_1, State_GOT_10, State_MATCH_101);
    signal current_state, next_state : StateType;
begin
    -- Synchronous State Register Process
    process(clk)
    begin
        if rising_edge(clk) then
            if rst = '1' then
                current_state <= State_IDLE; -- Initializes state register upon system reset
            else
                current_state <= next_state; -- Updates state on rising clock edge
            end if;
        end if;
    end process;

    -- Combinational Next-State and Output Logic Process
    process(current_state, serial_in)
    begin
        case current_state is
            when State_IDLE =>
                detected <= '0';
                if serial_in = '1' then
                    next_state <= State_GOT_1;
                else
                    next_state <= State_IDLE;
                end if;

            when State_GOT_1 =>
                detected <= '0';
                if serial_in = '0' then
                    next_state <= State_GOT_10;
                else
                    next_state <= State_GOT_1;
                end if;

            when State_GOT_10 =>
                detected <= '0';
                if serial_in = '1' then
                    next_state <= State_MATCH_101;
                else
                    next_state <= State_IDLE;
                end if;

            when State_MATCH_101 =>
                detected <= '1'; -- Asserts recognition flag in matching state
                if serial_in = '0' then
                    next_state <= State_GOT_10; -- Supports overlapping recognition
                else
                    next_state <= State_GOT_1;
                end if;

            when others =>
                detected <= '0';
                next_state <= State_IDLE;
        end case;
    end process;
end architecture behavioral;

