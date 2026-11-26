/*
 * Author: Nikolaos Panagopoulos
 * Date: November 2026
 * Course: Embedded Systems (5th Semester)
 * Institution: Dept. of Informatics and Telecommunications, University of Ioannina
 */
/*
 * Environment: VSCodium with PlatformIO IDE (PlatformIO Core 6.2.0, msp430-gcc 4.6.3)
 * Target MCU: TI MSP430F5529 (MSP-EXP430F5529LP LaunchPad)
 */
/*
 * Lab 1 - Exercise 5: Toggle Red LED between 1 Hz blinking and permanently OFF
 * using pushbutton S1 (P2.1).
 * Uses a 10 ms time-sliced delay loop so momentary button presses are sampled
 * responsively without being missed during a long blocking 500 ms delay.
 * Assumes default MSP430F5529 MCLK frequency of ~1.048576 MHz after reset.
 */

#include <msp430.h>

/* Default MSP430F5529 MCLK after reset (FLL locked to 32768 Hz x 32 = 1.048576 MHz). */
#define MCLK_FREQ_HZ            1048576UL
#define TICK_10MS_CYCLES        (MCLK_FREQ_HZ / 100UL)  /* ~10 ms polling and timing slice. */
#define HALF_PERIOD_1HZ_TICKS   50U                     /* 50 x 10 ms = 500 ms (1 Hz, 50% duty). */
#define DEBOUNCE_TICKS          2U                      /* 2 x 10 ms = 20 ms switch debounce. */

static void configureGpio(void){
    P1DIR |= BIT0;              // Set 0x01 P1.0 (Red LED1) to output
    P1OUT &= ~BIT0;             // Clear 0x01 P1.0 (Red LED1) to LOW (initial OFF state)

    P2DIR &= ~BIT1;             // Clear 0x02 P2.1 (Button S1) to input
    P2REN |= BIT1;              // Enable 0x02 P2.1 internal pull-up/pull-down resistor
    P2OUT |= BIT1;              // Select 0x02 P2.1 internal pull-up resistor (idle HIGH)
}

int main(void){
    /**
     * Polls button S1 (P2.1) every 10 ms and switches Red LED (P1.0) between
     * permanently OFF and 1 Hz blinking mode.
     *
     * Args:
     *     None.
     *
     * Returns: int(Never returns)
     */
    unsigned int is_blinking = 0U;        // Mode flag: 0 = permanently OFF, 1 = 1 Hz blink
    unsigned int blink_tick_count = 0U;   // Elapsed 10 ms ticks in current half-period
    unsigned int button_armed = 1U;       // 1 = waiting for press, 0 = waiting for release
    unsigned int stable_ticks = 0U;       // Consecutive matching samples for debounce

    WDTCTL = WDTPW | WDTHOLD;

    configureGpio();

    while (1){
        /* Sample active-low button state on P2.1 (0x02) with non-blocking debounce. */
        if (button_armed != 0U){
            if ((P2IN & BIT1) == 0U){
                // Read 0x02 P2.1 (Button S1): LOW when pressed
                stable_ticks++;

                if (stable_ticks >= DEBOUNCE_TICKS){
                    button_armed = 0U;      // Disarm until release to prevent repeated toggles
                    stable_ticks = 0U;
                    is_blinking = !is_blinking;
                    blink_tick_count = 0U;

                    if (is_blinking != 0U){
                        P1OUT |= BIT0;      // Set 0x01 P1.0 (Red LED1) to HIGH to start blink cycle
                    }
                    else{
                        P1OUT &= ~BIT0;     // Clear 0x01 P1.0 (Red LED1) to LOW for permanent OFF
                    }
                }
            }
            else{
                stable_ticks = 0U;
            }
        }
        else{
            if ((P2IN & BIT1) != 0U){ // Read 0x02 P2.1 (Button S1): HIGH when released
                stable_ticks++;
                if (stable_ticks >= DEBOUNCE_TICKS){

                    button_armed = 1U;      // Re-arm edge detection after stable release
                    stable_ticks = 0U;
                }
            }
            else{
                stable_ticks = 0U;
            }
        }

        /* Advance 1 Hz blink timer when blinking mode is active. */
        if (is_blinking != 0U){
            blink_tick_count++;
            if (blink_tick_count >= HALF_PERIOD_1HZ_TICKS){
                P1OUT ^= BIT0;              // Toggle 0x01 P1.0 (Red LED1) every 500 ms (1 Hz)
                blink_tick_count = 0U;
            }
        }

        __delay_cycles(TICK_10MS_CYCLES);   // Wait 10 ms before next sample and tick update
    }

    return 0;
}
