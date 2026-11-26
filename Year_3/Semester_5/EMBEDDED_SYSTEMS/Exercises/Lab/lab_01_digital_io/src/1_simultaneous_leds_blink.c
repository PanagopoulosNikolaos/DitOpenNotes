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
 * Lab 1 - Exercise 1: Simultaneous blinking of both onboard LEDs.
 * Red LED (LED1) is connected to P1.0 and Green LED (LED2) is connected to P4.7.
 * Both LEDs initialize in phase and toggle together at 1 Hz (50% duty cycle)
 * assuming the default MSP430F5529 MCLK frequency of ~1.048576 MHz after reset.
 */

#include <msp430.h>

/* Default MSP430F5529 MCLK after reset (FLL locked to 32768 Hz x 32 = 1.048576 MHz). */
#define MCLK_FREQ_HZ            1048576UL
#define HALF_PERIOD_1HZ_CYCLES  (MCLK_FREQ_HZ / 2UL)  /* 500 ms half-period for 1 Hz blink. */

static void configureGpio(void){
    P1DIR |= BIT0;              // Set 0x01 P1.0 (Red LED1) to output
    P4DIR |= BIT7;              // Set 0x80 P4.7 (Green LED2) to output

    P1OUT &= ~BIT0;             // Clear 0x01 P1.0 (Red LED1) to LOW for synchronized start
    P4OUT &= ~BIT7;             // Clear 0x80 P4.7 (Green LED2) to LOW for synchronized start
}

int main(void){
    /**
     * Configures LED pins, and blinks both LEDs in phase.
     *
     * Args:
     *     None.
     *
     * Returns: int(Never returns)
     */
    WDTCTL = WDTPW | WDTHOLD;

    configureGpio();

    while (1){
        P1OUT ^= BIT0;          // Toggle 0x01 P1.0 (Red LED1)
        P4OUT ^= BIT7;          // Toggle 0x80 P4.7 (Green LED2)

        __delay_cycles(HALF_PERIOD_1HZ_CYCLES);  // Hold state for 500 ms (1 Hz full period)
    }

    return 0;
}
