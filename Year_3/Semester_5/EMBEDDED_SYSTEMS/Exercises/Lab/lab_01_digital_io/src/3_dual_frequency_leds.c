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
 * Lab 1 - Exercise 3: Dual-frequency simultaneous LED blinking with 50% duty cycle.
 * Red LED (LED1, P1.0) blinks at 1 Hz (500 ms ON, 500 ms OFF).
 * Green LED (LED2, P4.7) blinks at 2 Hz (250 ms ON, 250 ms OFF).
 * Uses a 250 ms base tick (GCD of both half-periods) assuming default MCLK ~1.048576 MHz.
 */

#include <msp430.h>

/* Default MSP430F5529 MCLK after reset (FLL locked to 32768 Hz x 32 = 1.048576 MHz). */
#define MCLK_FREQ_HZ            1048576UL
#define BASE_TICK_250MS_CYCLES  (MCLK_FREQ_HZ / 4UL)  /* 250 ms base tick (2 Hz half-period). */
#define RED_TOGGLE_TICKS        2U                    /* 2 x 250 ms = 500 ms (1 Hz half-period). */

static void configureGpio(void){
    P1DIR |= BIT0;              // Set 0x01 P1.0 (Red LED1) to output
    P4DIR |= BIT7;              // Set 0x80 P4.7 (Green LED2) to output

    P1OUT |= BIT0;              // Set 0x01 P1.0 (Red LED1) to HIGH to begin ON half-cycle
    P4OUT |= BIT7;              // Set 0x80 P4.7 (Green LED2) to HIGH to begin ON half-cycle
}

int main(void){
    /**
     * Drives Red LED at 1 Hz and Green LED at 2 Hz with exact 50% duty cycles.
     *
     * Args:
     *     None.
     *
     * Returns: Returns: int(Never returns)
     */
    unsigned int tick_count = 0U;

    WDTCTL = WDTPW | WDTHOLD;

    configureGpio();

    while (1){
        __delay_cycles(BASE_TICK_250MS_CYCLES);  // Wait 250 ms base interval

        P4OUT ^= BIT7;          // Toggle 0x80 P4.7 (Green LED2) every 250 ms (2 Hz, 50% duty)
        tick_count++;

        if (tick_count >= RED_TOGGLE_TICKS){
            P1OUT ^= BIT0;      // Toggle 0x01 P1.0 (Red LED1) every 500 ms (1 Hz, 50% duty)
            tick_count = 0U;
        }
    }

    return 0;
}
