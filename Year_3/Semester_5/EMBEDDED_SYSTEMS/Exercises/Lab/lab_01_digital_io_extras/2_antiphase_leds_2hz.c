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
 * Lab 1 - Exercise 2: Simultaneous blinking of both onboard LEDs with 180-degree
 * phase difference at 2 Hz.
 * Red LED (LED1, P1.0) starts HIGH and Green LED (LED2, P4.7) starts LOW.
 * Both toggle every 250 ms (T = 500 ms -> f = 2 Hz, 50% duty cycle) assuming
 * the default MSP430F5529 MCLK frequency of ~1.048576 MHz after reset.
 */

#include <msp430.h>

/* Default MSP430F5529 MCLK after reset (FLL locked to 32768 Hz x 32 = 1.048576 MHz). */
#define MCLK_FREQ_HZ            1048576UL
#define HALF_PERIOD_2HZ_CYCLES  (MCLK_FREQ_HZ / 4UL)  /* 250 ms half-period for 2 Hz blink. */

static void configureGpio(void){
    P1DIR |= BIT0;              // Set 0x01 P1.0 (Red LED1) to output
    P4DIR |= BIT7;              // Set 0x80 P4.7 (Green LED2) to output

    P1OUT |= BIT0;              // Set 0x01 P1.0 (Red LED1) to HIGH for 180-degree phase offset
    P4OUT &= ~BIT7;             // Clear 0x80 P4.7 (Green LED2) to LOW for 180-degree phase offset
}

int main(void){
    /**
     * Sets opposing LED states, and alternates both at 2 Hz.
     *
     * Args:
     *     None.
     *
     * Returns:Returns: int(Never returns)
     */
    WDTCTL = WDTPW | WDTHOLD;

    configureGpio();

    while (1){
        __delay_cycles(HALF_PERIOD_2HZ_CYCLES);  // Hold opposite states for 250 ms (2 Hz period)

        P1OUT ^= BIT0;          // Toggle 0x01 P1.0 (Red LED1)
        P4OUT ^= BIT7;          // Toggle 0x80 P4.7 (Green LED2)
    }

    return 0;
}
