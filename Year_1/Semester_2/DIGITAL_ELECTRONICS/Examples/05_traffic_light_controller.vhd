-- Four-Phase Traffic Light Controller with Timer in VHDL
-- Controls North-South and East-West signals with dedicated green, yellow, and red intervals.

library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;

entity traffic_light_controller is
    port (
        clk         : in  std_logic;
        rst         : in  std_logic;
        ns_lights   : out std_logic_vector(2 downto 0); -- [Red, Yellow, Green]
        ew_lights   : out std_logic_vector(2 downto 0)  -- [Red, Yellow, Green]
    );
end entity traffic_light_controller;

architecture behavioral of traffic_light_controller is
    type PhaseType is (Phase_NS_GREEN, Phase_NS_YELLOW, Phase_EW_GREEN, Phase_EW_YELLOW);
    signal current_phase : PhaseType;
    signal timer_count   : unsigned(3 downto 0);

    -- Timing threshold parameters in clock cycles
    constant GREEN_DURATION  : unsigned(3 downto 0) := "1010"; -- 10 clock ticks
    constant YELLOW_DURATION : unsigned(3 downto 0) := "0011"; -- 3 clock ticks
begin
    process(clk)
    begin
        if rising_edge(clk) then
            if rst = '1' then
                current_phase <= Phase_NS_GREEN;
                timer_count   <= (others => '0');
            else
                case current_phase is
                    when Phase_NS_GREEN =>
                        if timer_count >= GREEN_DURATION then
                            current_phase <= Phase_NS_YELLOW;
                            timer_count   <= (others => '0');
                        else
                            timer_count <= timer_count + 1;
                        end if;

                    when Phase_NS_YELLOW =>
                        if timer_count >= YELLOW_DURATION then
                            current_phase <= Phase_EW_GREEN;
                            timer_count   <= (others => '0');
                        else
                            timer_count <= timer_count + 1;
                        end if;

                    when Phase_EW_GREEN =>
                        if timer_count >= GREEN_DURATION then
                            current_phase <= Phase_EW_YELLOW;
                            timer_count   <= (others => '0');
                        else
                            timer_count <= timer_count + 1;
                        end if;

                    when Phase_EW_YELLOW =>
                        if timer_count >= YELLOW_DURATION then
                            current_phase <= Phase_NS_GREEN;
                            timer_count   <= (others => '0');
                        else
                            timer_count <= timer_count + 1;
                        end if;

                    when others =>
                        current_phase <= Phase_NS_GREEN;
                        timer_count   <= (others => '0');
                end case;
            end if;
        end if;
    end process;

    -- Output decoding logic: [Red, Yellow, Green]
    process(current_phase)
    begin
        case current_phase is
            when Phase_NS_GREEN =>
                ns_lights <= "001"; -- NS Green
                ew_lights <= "100"; -- EW Red

            when Phase_NS_YELLOW =>
                ns_lights <= "010"; -- NS Yellow
                ew_lights <= "100"; -- EW Red

            when Phase_EW_GREEN =>
                ns_lights <= "100"; -- NS Red
                ew_lights <= "001"; -- EW Green

            when Phase_EW_YELLOW =>
                ns_lights <= "100"; -- NS Red
                ew_lights <= "010"; -- EW Yellow

            when others =>
                ns_lights <= "100";
                ew_lights <= "100";
        end case;
    end process;
end architecture behavioral;

