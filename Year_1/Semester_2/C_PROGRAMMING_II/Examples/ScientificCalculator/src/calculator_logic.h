#ifndef CALCULATOR_LOGIC_H
#define CALCULATOR_LOGIC_H

#include <stddef.h>

typedef enum {
    DEG,
    RAD
} AngleMode;

typedef struct {
    char buffer[256];
    AngleMode angle_mode;
} Calculator;

Calculator* calculator_new(void);
void calculator_free(Calculator* calc);

void calculator_evaluate(Calculator* calc, const char* expression);
void calculator_clear(Calculator* calc);
void calculator_toggle_angle_mode(Calculator* calc);
AngleMode calculator_get_angle_mode(const Calculator* calc);

const char* calculator_get_display(const Calculator* calc);

#endif
