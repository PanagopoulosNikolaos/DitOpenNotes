#include "calculator_logic.h"
#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include <math.h>
#include <ctype.h>

#ifndef M_PI
#define M_PI 3.14159265358979323846
#endif
#ifndef M_E
#define M_E 2.71828182845904523536
#endif

#define MAX_STACK_SIZE 100

// Stack for numbers (doubles)
typedef struct {
    double items[MAX_STACK_SIZE];
    int top;
} NumberStack;

// Stack for operators (chars)
typedef struct {
    char items[MAX_STACK_SIZE];
    int top;
} OperatorStack;

// Function prototypes for stack operations
void ns_push(NumberStack* s, double item);
double ns_pop(NumberStack* s);
void os_push(OperatorStack* s, char item);
char os_pop(OperatorStack* s);
char os_peek(OperatorStack* s);
int get_precedence(char op);
void apply_operator(NumberStack* numbers, char op, AngleMode angle_mode);
double factorial(double n);
int is_right_associative(char op);

Calculator* calculator_new(void) {
    Calculator* calc = (Calculator*)malloc(sizeof(Calculator));
    if (calc) {
        strcpy(calc->buffer, "0");
        calc->angle_mode = DEG;
    }
    return calc;
}

void calculator_free(Calculator* calc) {
    if (calc) {
        free(calc);
    }
}

void calculator_clear(Calculator* calc) {
    strcpy(calc->buffer, "0");
}

void calculator_toggle_angle_mode(Calculator* calc) {
    if (calc->angle_mode == DEG) {
        calc->angle_mode = RAD;
    } else {
        calc->angle_mode = DEG;
    }
}

AngleMode calculator_get_angle_mode(const Calculator* calc) {
    return calc ? calc->angle_mode : DEG;
}

const char* calculator_get_display(const Calculator* calc) {
    return calc->buffer;
}

void calculator_evaluate(Calculator* calc, const char* expression) {
    NumberStack numbers;
    numbers.top = -1;
    OperatorStack operators;
    operators.top = -1;

    const char* p = expression;

    while (*p) {
        if (isspace((unsigned char)*p)) { p++; continue; }
        if (isdigit((unsigned char)*p) || *p == '.') {
            char* end;
            double num = strtod(p, &end);
            ns_push(&numbers, num);
            p = end;
            continue;
        } else if (*p == 'p') {
            ns_push(&numbers, M_PI);
        } else if (*p == 'e') {
            ns_push(&numbers, M_E);
        } else if (*p == '(') {
            os_push(&operators, *p);
        } else if (*p == ')') {
            while (operators.top != -1 && os_peek(&operators) != '(') {
                apply_operator(&numbers, os_pop(&operators), calc->angle_mode);
            }
            if (operators.top != -1) {
                os_pop(&operators); // Pop '('
            } else {
                strcpy(calc->buffer, "Error: Mismatched parentheses");
                return;
            }
        } else if (isalpha((unsigned char)*p)) {
            char func[10];
            int i = 0;
            while (isalpha((unsigned char)*p) && i < 9) {
                func[i++] = *p++;
            }
            func[i] = '\0';
            os_push(&operators, func[0]); // Simple mapping NOT recommended to be changed later on
            p--; // Decrement to handle the next character correctly
        } else { // Operator
            while (operators.top != -1) {
                char top_op = os_peek(&operators);
                int top_prec = get_precedence(top_op);
                int curr_prec = get_precedence(*p);
                if (top_prec > curr_prec || (top_prec == curr_prec && !is_right_associative(*p))) {
                    apply_operator(&numbers, os_pop(&operators), calc->angle_mode);
                } else {
                    break;
                }
            }
            os_push(&operators, *p);
        }
        p++;
    }

    while (operators.top != -1) {
        if (os_peek(&operators) == '(') {
            strcpy(calc->buffer, "Error: Mismatched parentheses");
            return;
        }
        apply_operator(&numbers, os_pop(&operators), calc->angle_mode);
    }

    if (numbers.top == 0) {
        double val = ns_pop(&numbers);
        if (isnan(val)) {
            strcpy(calc->buffer, "Error: Math domain");
        } else if (!isfinite(val)) {
            strcpy(calc->buffer, "Error: Overflow");
        } else {
            snprintf(calc->buffer, sizeof(calc->buffer), "%.10g", val);
        }
    } else {
        strcpy(calc->buffer, "Error: Invalid expression");
    }
}

// Stack implementations
void ns_push(NumberStack* s, double item) {
    if (s->top < MAX_STACK_SIZE - 1) {
        s->items[++s->top] = item;
    }
}

double ns_pop(NumberStack* s) {
    if (s->top > -1) {
        return s->items[s->top--];
    }
    return 0.0; // Should handle error
}

void os_push(OperatorStack* s, char item) {
    if (s->top < MAX_STACK_SIZE - 1) {
        s->items[++s->top] = item;
    }
}

char os_pop(OperatorStack* s) {
    if (s->top > -1) {
        return s->items[s->top--];
    }
    return '\0'; // Should handle error
}

char os_peek(OperatorStack* s) {
    if (s->top > -1) {
        return s->items[s->top];
    }
    return '\0'; // Should handle error
}

int get_precedence(char op) {
    switch (op) {
        case '+': case '-': return 1;
        case '*': case '/': case '%': return 2;
        case '^': return 3; // exponent should be right-associative
        case 's': case 'c': case 't': case 'l': case 'L': case 'q': case '!': case 'S': case 'C': case 'T': case 'E': case 'R': case 'N': return 4;
        default: return 0;
    }
}
int is_right_associative(char op) {
    return op == '^';
}

void apply_operator(NumberStack* numbers, char op, AngleMode angle_mode) {
    double a, b;
    switch (op) {
        case '+': b = ns_pop(numbers); a = ns_pop(numbers); ns_push(numbers, a + b); break;
        case '-': b = ns_pop(numbers); a = ns_pop(numbers); ns_push(numbers, a - b); break;
        case '*': b = ns_pop(numbers); a = ns_pop(numbers); ns_push(numbers, a * b); break;
        case '/': b = ns_pop(numbers); a = ns_pop(numbers); ns_push(numbers, b == 0.0 ? NAN : a / b); break;
        case '%': b = ns_pop(numbers); a = ns_pop(numbers); ns_push(numbers, b == 0.0 ? NAN : fmod(a, b)); break;
        case '^': b = ns_pop(numbers); a = ns_pop(numbers); ns_push(numbers, pow(a, b)); break;

        case 's': a = ns_pop(numbers); ns_push(numbers, angle_mode == DEG ? sin(a * M_PI / 180.0) : sin(a)); break;
        case 'c': a = ns_pop(numbers); ns_push(numbers, angle_mode == DEG ? cos(a * M_PI / 180.0) : cos(a)); break;
        case 't': a = ns_pop(numbers); ns_push(numbers, angle_mode == DEG ? tan(a * M_PI / 180.0) : tan(a)); break;

        case 'S': a = ns_pop(numbers); ns_push(numbers, angle_mode == DEG ? asin(a) * 180.0 / M_PI : asin(a)); break;
        case 'C': a = ns_pop(numbers); ns_push(numbers, angle_mode == DEG ? acos(a) * 180.0 / M_PI : acos(a)); break;
        case 'T': a = ns_pop(numbers); ns_push(numbers, angle_mode == DEG ? atan(a) * 180.0 / M_PI : atan(a)); break;

        case 'l': a = ns_pop(numbers); ns_push(numbers, (a <= 0.0) ? NAN : log(a)); break;
        case 'L': a = ns_pop(numbers); ns_push(numbers, (a <= 0.0) ? NAN : log10(a)); break;
        case 'q': a = ns_pop(numbers); ns_push(numbers, (a < 0.0) ? NAN : sqrt(a)); break;
        case '!': a = ns_pop(numbers); ns_push(numbers, factorial(a)); break;
        case 'E': a = ns_pop(numbers); ns_push(numbers, exp(a)); break;
        case 'R': a = ns_pop(numbers); ns_push(numbers, a == 0.0 ? NAN : 1.0 / a); break;
        case 'N': a = ns_pop(numbers); ns_push(numbers, -a); break;
        default: break;
    }
}

double factorial(double n) {
    if (n < 0 || floor(n) != n) return NAN; // Only defined for non-negative integers
    if (n == 0) return 1;
    double result = 1;
    int ni = (int)n;
    for (int i = 1; i <= ni; i++) {
        result *= i;
        if (!isfinite(result)) return NAN;
    }
    return result;
}
