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
 * Lab 1 - Exercise 4: Red LED state toggle using pushbutton S1 (P2.1).
 * A momentary press on active-low switch P2.1 (configured with internal pull-up)
 * switches Red LED (LED1, P1.0) between permanently ON and permanently OFF.
 * Software debouncing and release waiting prevent multiple toggles per press.
 */

#include <msp430.h>

/* Default MSP430F5529 MCLK after reset (FLL locked to 32768 Hz x 32 = 1.048576 MHz). */
#define MCLK_FREQ_HZ            1048576UL
#define DEBOUNCE_DELAY_CYCLES   (MCLK_FREQ_HZ / 50UL)  /* ~20 ms mechanical switch debounce. */

static void configureGpio(void)
{
    P1DIR |= BIT0;              // Set 0x01 P1.0 (Red LED1) to output
    P1OUT &= ~BIT0;             // Clear 0x01 P1.0 (Red LED1) to LOW (initial OFF state)

    P2DIR &= ~BIT1;             // Clear 0x02 P2.1 (Button S1) to input
    P2REN |= BIT1;              // Enable 0x02 P2.1 internal pull-up/pull-down resistor
    P2OUT |= BIT1;              // Select 0x02 P2.1 internal pull-up resistor (idle HIGH)
}

int main(void){
    /**
     * Polls button S1 (P2.1) and toggles Red LED (P1.0) once per momentary press.
     *
     * Args:
     *     None.
     *
     * Returns: Returns: int(Never returns)
     */
    WDTCTL = WDTPW | WDTHOLD;

    configureGpio();

    while (1){
        if ((P2IN & BIT1) == 0U){
            __delay_cycles(DEBOUNCE_DELAY_CYCLES);  // Wait 20 ms for contact bounce to settle

            if ((P2IN & BIT1) == 0U){
                 // Confirm 0x02 P2.1 remains LOW after debounce
                P1OUT ^= BIT0;              // Toggle 0x01 P1.0 (Red LED1) between ON and OFF

                while ((P2IN & BIT1) == 0U){
                    /* Spin until button release. */
                }

                __delay_cycles(DEBOUNCE_DELAY_CYCLES);  // Debounce mechanical release bounce
            }
        }
    }

    return 0;
}
