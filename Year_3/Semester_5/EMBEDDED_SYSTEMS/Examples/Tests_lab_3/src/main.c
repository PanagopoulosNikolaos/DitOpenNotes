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
 * Lab 1 - Exercise 4 (interrupt version): Red LED state toggle using pushbutton S1.
 * A falling edge on active-low S1 (P2.1, internal pull-up) toggles Red LED (P1.0)
 * between permanently ON and permanently OFF inside the Port 2 ISR.
 */

#include <msp430.h>

#define MCLK_FREQ_HZ            1048576UL
#define DEBOUNCE_DELAY_CYCLES   (MCLK_FREQ_HZ / 50UL)  /* ~20 ms switch debounce. */

int main(void)
{
    WDTCTL = WDTPW | WDTHOLD;

    P1DIR |= BIT0;              // P1.0 Red LED1 -> output
    P1OUT &= ~BIT0;             // Start with LED OFF

    P2DIR &= ~BIT1;             // P2.1 Button S1 -> input
    P2REN |= BIT1;              // Enable internal pull-up/pull-down
    P2OUT |= BIT1;              // Select pull-up (idle HIGH)
    P2IES |= BIT1;              // Interrupt on HIGH-to-LOW (button press)
    P2IFG &= ~BIT1;             // Clear pending flag before enabling interrupt
    P2IE |= BIT1;               // Enable P2.1 interrupt

    __bis_SR_register(GIE);     // Global interrupt enable

    while (1)
    {
        __bis_SR_register(LPM0_bits + GIE);  // Sleep until S1 is pressed
    }

    return 0;
}

#pragma vector = PORT2_VECTOR
__interrupt void Port_2(void)
{
    __delay_cycles(DEBOUNCE_DELAY_CYCLES);  // Ignore contact bounce
    P1OUT ^= BIT0;                          // Toggle Red LED1
    P2IFG &= ~BIT1;                         // Clear interrupt flag
}
